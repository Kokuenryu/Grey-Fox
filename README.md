# 🦊 GreyFox v2.0 - Network Auditor

**GreyFox** é um framework leve e modular para auditoria de rede e segurança ofensiva (Red Team), desenvolvido inteiramente em **Python Nativo**. Ele foi projetado para identificar dispositivos ativos, mapear superfícies de ataque e detectar arquivos sensíveis expostos em servidores locais.

## 🚀 Funcionalidades

- **Scanner de Rede Multi-threaded:** Utiliza o processamento paralelo do Python para escanear redes inteiras (/24) em segundos.
- **Auditoria de Vulnerabilidades Web:** Busca automaticamente por arquivos críticos expostos, como:
    - Configurações de ambiente (`.env`)
    - Repositórios expostos (`.git`)
    - Backups de bancos de dados (`.sql`)
    - Chaves SSH e credenciais de nuvem (`.aws/credentials`).
- **Exfiltração de Evidências (Looting):** Faz o download automático de arquivos vulneráveis para análise posterior.
- **Relatórios Dual-Output:**
    - **JSON:** Para integração com outras ferramentas de Red Team.
    - **HTML Dashboard:** Um relatório visual moderno e intuitivo para apresentação de resultados.
- **Nativo e Portátil:** Zero dependências externas (`pip install` não é necessário).

## 🛠️ Como Usar

1. **Clone o repositório:**
```bash
   git clone [https://github.com/seu-usuario/greyfox.git](https://github.com/seu-usuario/greyfox.git)
   cd greyfox

```markdown
# 🦊 GreyFox v2.0 - Network Auditor

**GreyFox** é um framework leve e modular para auditoria de rede e segurança ofensiva (Red Team), desenvolvido inteiramente em **Python Nativo**. Ele foi projetado para identificar dispositivos ativos, mapear superfícies de ataque e detectar arquivos sensíveis expostos em servidores locais.

## 🚀 Funcionalidades

- **Scanner de Rede Multi-threaded:** Utiliza o processamento paralelo do Python para escanear redes inteiras (/24) em segundos.
- **Auditoria de Vulnerabilidades Web:** Busca automaticamente por arquivos críticos expostos, como:
    - Configurações de ambiente (`.env`)
    - Repositórios expostos (`.git`)
    - Backups de bancos de dados (`.sql`)
    - Chaves SSH e credenciais de nuvem (`.aws/credentials`).
- **Exfiltração de Evidências (Looting):** Faz o download automático de arquivos vulneráveis para análise posterior.
- **Relatórios Dual-Output:**
    - **JSON:** Para integração com outras ferramentas de Red Team.
    - **HTML Dashboard:** Um relatório visual moderno e intuitivo para apresentação de resultados.
- **Nativo e Portátil:** Zero dependências externas (`pip install` não é necessário).

## 🛠️ Como Usar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Kokuenryu/Grey-Fox.git
   cd greyfox

```

2. **Configure sua rede:**
Abra o arquivo `greyfox.py` e altere o prefixo da rede na última linha:
```python
auditor = GreyFoxAuditor("192.168.1") # Substitua pelo seu prefixo

```

3. **Execute o script:**
```bash
python3 greyfox.py

```



## 📂 Estrutura de Resultados

Após cada execução, o GreyFox cria uma pasta dentro de `audit_results/` com o timestamp da sessão:

```text
audit_results/
└── 20260509_120000/
    ├── dashboard.html      <-- Relatório visual
    ├── audit_report.json   <-- Dados brutos para análise
    └── network_loot/       <-- Arquivos sensíveis coletados da rede

```

## ⚖️ Aviso Legal (Disclaimer)

Esta ferramenta foi desenvolvida exclusivamente para fins de **educação e testes de segurança autorizados**. O uso do GreyFox contra redes ou sistemas sem permissão explícita é ilegal e antiético. O autor não se responsabiliza pelo uso indevido deste software.

---

*Desenvolvido por [Henrique Keise]*
