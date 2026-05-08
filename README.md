# 🦊 GreyFox v2

<p align="center">
  <img src="greyfox.png" width="250" alt="GreyFox Logo">
</p>

**GreyFox** é uma ferramenta minimalista de Red Team focada em reconhecimento de rede e movimentação lateral automatizada. Projetada para ser leve, eficiente e organizada, com suporte total para ambientes Linux (**NixOS**/Arch) e Windows.

## 🚀 Funcionalidades

- **Smart Looting**: Varredura inteligente em busca de chaves SSH (RSA/Ed25519), arquivos `.env` e logs de terminal.
- **Session-Based Results**: Cada execução gera uma nova subpasta (`results/scan1`, `results/scan2`...) mantendo seus dados organizados e protegidos.
- **Fast Network Discovery**: Scanner multi-thread otimizado para identificar serviços críticos como SSH (22), HTTP (80), SMB (445) e RDP (3389).
- **Lateral Movement**: Automação de tentativas de acesso utilizando as credenciais e chaves coletadas durante a fase de looting.

## ⚙️ Configuração Prévia

Antes de rodar a ferramenta, você deve ajustar o prefixo da rede que deseja escanear:

1. Abra o arquivo `main.py`.
2. No bloco `# 3. Scanning`, altere a variável `network_prefix` para o IP da sua sub-rede.
   - Exemplo: `network_prefix = "192.168.68"`

## 🛠️ Como usar

1. **Clonar o repositório:**
```bash
   git clone [https://github.com/Kokuenryu/Grey-Fox.git](https://github.com/Kokuenryu/Grey-Fox.git)
   cd Grey-Fox
   

```

2. **Executar a ferramenta:**
```bash
python main.py


```



```

*Nota para usuários NixOS: Você pode rodar dentro de um `nix-shell -p python3` para garantir as dependências.*

## 📂 Estrutura de Resultados

Os dados coletados são organizados da seguinte forma:
```text
results/
└── scanX/
    ├── bash_history.txt    # Histórico de comandos coletado
    ├── key_id_rsa          # Chaves privadas encontradas
    ├── targets_found.txt   # Lista de IPs e portas ativos na rede
    └── pwned_hosts.txt     # Log de acessos bem-sucedidos

```

## ⚠️ Aviso Legal

Este software foi criado exclusivamente para fins educacionais e testes de penetração autorizados. O uso desta ferramenta em sistemas sem permissão explícita é ilegal. O desenvolvedor não se responsabiliza por qualquer uso indevido ou danos causados por este programa.
