# 🚀 DevLoop - Demo de Processamento de Dados

Este é um projeto **DEMO** desenvolvido pela **DevLoop**, com objetivo de demonstrar nossa capacidade técnica em automação, processamento de dados e containerização.

---

## 📦 Sobre o Projeto

- ✅ Agente automatizado de processamento de dados.
- ✅ Totalmente containerizado com **Docker e Docker Compose**.
- ✅ Gera dados fictícios, processa, analisa e gera relatórios (`.json` e `.csv`).
- ✅ Fácil de executar em qualquer ambiente.

---

## 🏗️ Arquitetura


```sh
.
├── 🐳 docker-compose.yml   # Orquestra os serviços da aplicação
├── 🐳 Dockerfile           # Define a imagem do container do agente
├── 🐍 main.py              # Ponto de entrada da aplicação
├── 🐍 job_example.py       # Contém a lógica de processamento dos dados
├── 📋 requirements.txt     # Lista de dependências Python
├── ⚙️ .env.example         # Exemplo de arquivo de variáveis de ambiente
├── 🌐 nginx.conf           # Configuração de um serviço Nginx (exemplo)
├── 📖 README.md            # Esta documentação
└── 🚀 run.sh / run.bat    # Scripts para facilitar a execução
```

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para executar o projeto em seu ambiente local.

### Pré-requisitos

- **Docker**: [Instruções de instalação](https://docs.docker.com/get-docker/)
- **Docker Compose**: Geralmente incluído na instalação do Docker.
- **Git**: Para clonar o repositório.

### ⚙️ Passos para Execução

1.  **Clone o Repositório**

    ```bash
    git clone https://github.com/DevLoop-ops/Docker-Hub.git
    cd Docker-Hub
    ```

2.  **Configure as Variáveis de Ambiente**

    Copie o arquivo de exemplo para criar seu próprio arquivo de configuração.

    ```bash
    cp .env.example .env
    ```
    *Nenhuma alteração é necessária para a execução padrão.*

3.  **Inicie a Aplicação com Docker Compose**

    Este comando irá construir as imagens e iniciar os containers.

    ```bash
    docker-compose up --build
    ```
    Para executar em modo "detached" (em segundo plano):
    ```bash
    docker-compose up --build -d
    ```

4.  **Acompanhe os Logs**

    Para ver a saída do agente em tempo real:
    ```bash
    docker-compose logs -f data-agent
    ```

5.  **Parar a Aplicação**

    ```bash
    docker-compose down
    ```

---

## 📊 O que o Job Faz?

O agente executa um processo simples de ETL (Extração, Transformação e Carga):

1.  **Extração**: Gera 100 registros de vendas fictícios. Se um arquivo de dados já existir, ele será utilizado.
2.  **Transformação**: Utiliza o `pandas` para calcular métricas importantes:
    -   **Receita Total**: Soma do valor de todas as vendas.
    -   **Total de Vendas**: Número total de transações.
    -   **Ticket Médio**: Valor médio por transação.
    -   **Top 5 Produtos**: Produtos que mais geraram receita.
    -   **Performance por Categoria**: Receita agrupada por categoria.
3.  **Carga**:
    -   Exibe os resultados em tabelas formatadas no terminal.
    -   Salva um relatório executivo em `.json` e os dados brutos em `.csv` no diretório `reports/`.

---

## 🧪 Testes e Validação

Para validar que tudo está funcionando corretamente:

1.  **Verifique a Saída do Terminal**: Após a execução, você verá o banner da aplicação, os logs de processamento e as tabelas de resultados.
2.  **Verifique os Arquivos Gerados**:
    -   `data/sales_data.json`: Arquivo com os dados de vendas gerados.
    -   `reports/`: Diretório contendo os relatórios em `.json` e `.csv`.
    -   `logs/agent.log`: Arquivo de log com o histórico da execução.

### Comandos Úteis para Debug

```bash
# Listar containers em execução
docker-compose ps

# Acessar o shell do container do agente
docker-compose exec data-agent bash

# Limpar todos os dados (volumes, redes, etc.)
docker-compose down -v --rmi all
```

---

## 🔧 Configuração e Desenvolvimento

### Variáveis de Ambiente

O comportamento do agente pode ser ajustado através do arquivo `.env`:

| Variável      | Descrição                           | Padrão       |
|---------------|---------------------------------------|--------------|
| `ENVIRONMENT` | Define o ambiente de execução.        | `production` |
| `LOG_LEVEL`   | Define o nível de detalhe dos logs.   | `INFO`       |
| `DATA_SOURCE` | Nome do arquivo de dados a ser usado. | `sales_data` |

### Estrutura do Código

-   **`main.py`**: Orquestra a execução, exibe o banner e gerencia o logging.
-   **`job_example.py`**: A classe `SalesDataProcessor` contém toda a lógica de negócio. Para adicionar novas métricas ou relatórios, este é o lugar para editar.

---

## 📄 Licença

Este projeto é uma demonstração técnica. Sinta-se à vontade para usá-lo para fins educacionais e de avaliação.

---
