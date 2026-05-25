# Explicação do Diagrama de Arquitetura Docker + FastAPI

Este documento descreve as relações e o fluxo de dados entre os componentes do nosso projeto utilizando Docker e Docker Compose, servindo como guia explicativo para o diagrama em anexo.

---

## 1. Descrição dos Componentes e suas Relações

* **main.py:** Contém o código-fonte bruto da nossa aplicação FastAPI. Ele define as rotas e a lógica de funcionamento do sistema.
* **Dockerfile:** É a nossa "receita de bolo". Ele lê o `main.py` e suas dependências para instruir o Docker Engine sobre como construir o ambiente ideal para o app rodar de forma isolada.
* **Imagem Docker:** É o resultado gerado após a execução do comando `docker build` no Dockerfile. Um artefato estático, imutável, que empacota o Python, as bibliotecas e o nosso código.
* **docker-compose.yml:** O maestro do sistema. Ele define as regras de como a Imagem Docker se tornará um contêiner ativo, gerenciando portas de rede, variáveis de ambiente e volumes sem precisarmos digitar comandos longos no terminal.
* **Container em Execução:** A instância real, viva e isolada da nossa Imagem Docker rodando na memória RAM da máquina.
* **Porta Exposta / Mapeada:** A ponte de comunicação. O contêiner roda internamente na porta `8000`, e o Docker Compose mapeia essa porta para a porta `8000` da nossa máquina física (Host).

---

## 2. Fluxo de Requisições (Como os dados trafegam)

1. O **Cliente Externo** (Navegador ou Insomnia) faz uma requisição acessando a URL `http://localhost:8000`.
2. A requisição bate na **Máquina Host**, que identifica que a porta `8000` está mapeada para um serviço do Docker.
3. O Docker redireciona esse tráfego para dentro do **Container em Execução**, entregando a requisição na porta interna do servidor Uvicorn/FastAPI.
4. O código no **main.py** processa a requisição e faz o caminho inverso para devolver a resposta de sucesso ao usuário.