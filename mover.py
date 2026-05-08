import subprocess

def try_move(ip, key_path):
    """Tenta executar um comando remoto para validar o acesso."""
    try:
        # Tenta logar como root (comum em servidores/IoT) ou usuário atual
        cmd = [
            "ssh", "-i", key_path,
            "-o", "BatchMode=yes",
            "-o", "StrictHostKeyChecking=no",
            "-o", "ConnectTimeout=2",
            f"root@{ip}", "hostname"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0
    except Exception:
        return False