import socket
import urllib.request
import urllib.error
import json
import os
import concurrent.futures
from datetime import datetime

# Logo Estilo Old School Terminal
LOGO = r"""
  ________                      ___________              
 /  _____/______   ____ ___.__.\_   _____/______  ___  
/   \  __\_  __ \_/ __ <   |  | |    __) \_  __ \ \  \/ /  
\    \_\  \  | \/\  ___/\___  | |     \   |  | \/  >    <   
 \______  /__|    \___  > ____| \___  /   |__|    /__/\_ \  
        \/            \/\/          \/                  \/  
                                [ v2.0 - Network Auditor ]
"""

class GreyFoxAuditor:
    def __init__(self, network_prefix):
        self.network_prefix = network_prefix
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.base_path = os.path.join("audit_results", self.timestamp)
        self.loot_path = os.path.join(self.base_path, "network_loot")
        self.report_data = {"timestamp": self.timestamp, "summary": [], "total_vulns": 0}
        
        self.target_files = [
            "/.env", "/.git/config", "/backup.sql", "/config.php", 
            "/.ssh/id_rsa", "/.aws/credentials", "/docker-compose.yml"
        ]
        
        os.makedirs(self.loot_path, exist_ok=True)

    def print_banner(self):
        print("\033[94m" + LOGO + "\033[0m")
        print(f"[*] Sessão iniciada em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"[*] Alvo: Redes {self.network_prefix}.0/24\n" + "-"*55)

    def check_http_vulnerability(self, ip, port):
        vulns = []
        for path in self.target_files:
            url = f"http://{ip}:{port}{path}"
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'GreyFox/2.0'})
                with urllib.request.urlopen(req, timeout=1) as response:
                    if response.status == 200:
                        content = response.read()
                        file_name = f"{ip}_{port}_{path.replace('/', '_').lstrip('_')}"
                        with open(os.path.join(self.loot_path, file_name), "wb") as f:
                            f.write(content)
                        vulns.append({"type": "Arquivo Exposto", "url": url, "file": file_name})
            except:
                continue
        return vulns

    def scan_host(self, ip):
        ports = [21, 22, 80, 443, 445, 8080]
        host_results = {"ip": ip, "ports": [], "vulns": []}
        
        for port in ports:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.3)
                    if s.connect_ex((ip, port)) == 0:
                        host_results["ports"].append(port)
                        if port in [80, 8080, 443]:
                            found = self.check_http_vulnerability(ip, port)
                            host_results["vulns"].extend(found)
            except:
                continue
        
        if host_results["ports"]:
            vuln_count = len(host_results["vulns"])
            status = f"[\033[91m!\033[0m] {vuln_count} VULNS" if vuln_count > 0 else "[\033[92mSAFE\033[0m]"
            print(f"{status} Host: {ip} | Portas: {host_results['ports']}")
            return host_results
        return None

    def run(self):
        self.print_banner()
        ips = [f"{self.network_prefix}.{i}" for i in range(1, 255)]
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            results = list(executor.map(self.scan_host, ips))
        
        self.report_data["summary"] = [r for r in results if r is not None]
        self.report_data["total_vulns"] = sum(len(r["vulns"]) for r in self.report_data["summary"])
        self.save_reports()

    def save_reports(self):
        json_path = os.path.join(self.base_path, "audit_report.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(self.report_data, f, indent=4)
        
        self.generate_html(os.path.join(self.base_path, "dashboard.html"))
        print(f"\n" + "="*55)
        print(f"[*] Auditoria Finalizada! Total de Falhas: {self.report_data['total_vulns']}")
        print(f"[*] Dashboard: {self.base_path}/dashboard.html")

    def generate_html(self, output_path):
        rows = ""
        for host in self.report_data["summary"]:
            ip, ports = host["ip"], ", ".join(map(str, host["ports"]))
            if not host["vulns"]:
                rows += f"<tr><td>{ip}</td><td>{ports}</td><td><span class='safe'>Limpo</span></td><td>-</td></tr>"
            else:
                for v in host["vulns"]:
                    rows += f"<tr><td>{ip}</td><td>{ports}</td><td><span class='vuln'>{v['type']}</span></td><td><a href='{v['url']}'>{v['url']}</a></td></tr>"

        html_template = f"""
        <html><head><meta charset='UTF-8'><style>
            body {{ font-family: 'Segoe UI', sans-serif; background: #0f172a; color: #e2e8f0; padding: 40px; }}
            .container {{ max-width: 1100px; margin: auto; background: #1e293b; padding: 25px; border-radius: 10px; border: 1px solid #334155; }}
            h1 {{ color: #38bdf8; border-bottom: 2px solid #38bdf8; padding-bottom: 10px; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            th {{ background: #334155; padding: 12px; text-align: left; color: #38bdf8; }}
            td {{ padding: 12px; border-bottom: 1px solid #334155; }}
            .vuln {{ background: #ef4444; color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 0.8em; }}
            .safe {{ background: #22c55e; color: white; padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 0.8em; }}
            a {{ color: #38bdf8; text-decoration: none; }}
        </style></head><body><div class='container'><h1>GreyFox v2.0 - Auditor Report</h1><p>Vulnerabilidades Totais: {self.report_data['total_vulns']}</p><table><thead><tr><th>Host</th><th>Portas</th><th>Status</th><th>Detalhes</th></tr></thead><tbody>{rows}</tbody></table></div></body></html>"""
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_template)

if __name__ == "__main__":
    auditor = GreyFoxAuditor("192.168.1") # Altere para o prefixo da sua rede
    auditor.run()