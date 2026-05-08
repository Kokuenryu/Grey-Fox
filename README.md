# 🦊 GreyFox v2

![GreyFox Logo](greyfox.png)

**GreyFox** é uma ferramenta minimalista de Red Team focada em reconhecimento de rede e movimentação lateral automatizada. Desenvolvida para ambientes Linux (NixOS/Arch) e Windows.

## 🚀 Funcionalidades
- **Smart Looting**: Varredura automática em busca de chaves SSH, arquivos `.env` e históricos de shell.
- **Session-Based Results**: Organiza cada execução em pastas separadas (`scan1`, `scan2`...) dentro de `/results`.
- **Fast Network Discovery**: Scanner multi-thread para identificação de portas críticas (22, 80, 445, 3389).
- **Lateral Movement**: Tentativa de autenticação automática utilizando as chaves coletadas.

## 🛠️ Como usar
1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/GreyFox.git](https://github.com/seu-usuario/GreyFox.git)
   python main.py

## ⚠️ Aviso Legal
Este software foi criado para fins educacionais e testes de penetração autorizados. O uso indevido desta ferramenta para atividades ilícitas é de total responsabilidade do usuário.
