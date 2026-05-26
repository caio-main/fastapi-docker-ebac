# Explicação do Diagrama de Arquitetura Docker + FastAPI (Versão Corrigida)

Este documento descreve revisões na arquitetura e no fluxo de dados entre os componentes do projeto utilizando Docker e Docker Compose, corrigindo os pontos de relacionamento de conceitos e mapeamento de rede.

---

## 1. Ajustes Conceituais de Componentes

* **main.py e Dockerfile:** O código-fonte (`main.py`) é estruturado pelo `Dockerfile`, que define os passos de instalação e execução.
* **Imagem Docker:** Gerada a partir do `Dockerfile`. É um artefato estático e imutável.
* **docker-compose.yml (Orquestrador):** Corrigindo o fluxo conceitual, o Compose não é gerado pela imagem. Ele **consome e utiliza a Imagem Docker** (ou gerencia seu build) para orquestrar e subir os serviços automaticamente com o comando `docker compose up`.
* **Container em Execução:** A instância isolada e ativa da aplicação FastAPI na memória, instanciada diretamente pela ação do Docker Compose.

---

## 2. Fluxo de Portas e Requisições (Mapeamento Host x Container)

Para tornar explícito o isolamento de redes e o mapeamento de portas (`- 8000:8000`), o tráfego foi mapeado visualmente em camadas distintas:

1. **Origem:** O **Cliente Externo** faz uma requisição HTTP via navegador ou Insomnia disparando para `http://localhost:8000`.
2. **Máquina Host:** A requisição chega primeiro na porta física **8000 da Máquina Host** (computador local).
3. **Mapeamento de Porta (Docker Net):** O Docker intercepta essa entrada na porta do Host e, seguindo as regras do `docker-compose.yml`, redireciona o tráfego para a **Porta Interna 8000 do Container**.
4. **Destino:** A aplicação FastAPI recebe o dado na porta interna do container, processa e devolve a resposta pelo mesmo caminho.