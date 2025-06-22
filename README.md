# 🚀 Agente de Processamento de Dados - Desenvolvido pela DevLoop

> **Prova de Capacidade Técnica** - Um sistema containerizado para processamento e análise de dados de vendas, demonstrando expertise em automação e engenharia de software.

![DevLoop Banner](C:\Users\Sthev\Documents\CEO_DevLoop\Projetos\LOGO DevLoops\Redes Sociais Imagem\.PNG\Imagem-para-insta-e-outros.png) 

---

## 🏢 Sobre a DevLoop

**DevLoop** é uma empresa de tecnologia especializada em criar soluções de software sob medida. Nossa missão é transformar desafios de negócio em sistemas eficientes, escaláveis e robustos.

- **Website**: `devloop.com.br` (site fictício)
- **Contato**: `contato@devloop.com.br`

---

## 📋 Descrição do Projeto

Este projeto apresenta um **agente automatizado** que simula o processamento de um lote de dados de vendas. O sistema é totalmente containerizado com Docker e Docker Compose, seguindo as melhores práticas de desenvolvimento para garantir portabilidade e facilidade de deploy.

### 🎯 Funcionalidades Principais

- ✅ **Geração de Dados Fictícios**: Cria um conjunto de dados de vendas realista para demonstração.
- ✅ **Processamento com Pandas**: Utiliza a biblioteca `pandas` para análise e manipulação dos dados.
- ✅ **Relatórios Executivos**: Gera um resumo claro e conciso com as principais métricas de negócio.
- ✅ **Output Visual**: Apresenta os resultados de forma organizada e colorida no terminal.
- ✅ **Logging Estruturado**: Registra todos os passos importantes da execução para monitoramento.
- ✅ **Containerização Completa**: Todo o ambiente é gerenciado pelo Docker, garantindo consistência.
- ✅ **Exportação de Relatórios**: Salva os dados processados e relatórios em arquivos (`.json` e `.csv`).
- ✅ **Configuração Flexível**: Utiliza variáveis de ambiente para facilitar a configuração.

---

## 🏗️ Arquitetura do Sistema

A estrutura do projeto foi pensada para ser modular e de fácil entendimento:

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

**🎯 Objetivo Alcançado**: Um sistema profissional, containerizado e funcional, pronto para demonstrar a competência técnica da **DevLoop**.

---

# 🚀 Agente de Processamento de Dados - Sistema de Relatórios de Vendas

> **Prova de Capacidade Técnica** - Sistema containerizado para processamento e análise de dados de vendas

## 📋 Descrição do Projeto

Este projeto demonstra um **agente automatizado** que processa dados de vendas e gera relatórios executivos detalhados. O sistema é totalmente containerizado com Docker, seguindo as melhores práticas de engenharia de software.

### 🎯 Funcionalidades Principais

- ✅ **Geração de dados fictícios** de vendas para demonstração
- ✅ **Processamento e análise** de dados com pandas
- ✅ **Relatórios executivos** com métricas de negócio
- ✅ **Output colorido** no terminal para melhor experiência
- ✅ **Logging estruturado** para monitoramento
- ✅ **Containerização completa** com Docker
- ✅ **Arquivos de saída** em JSON e CSV
- ✅ **Configuração via variáveis de ambiente**

## 🏗️ Arquitetura do Sistema

```
📁 Projeto/
├── 🐳 docker-compose.yml      # Orquestração dos containers
├── 🐳 Dockerfile              # Imagem do agente Python
├── 🐍 main.py                 # Script principal do agente
├── 🐍 job_example.py          # Lógica de processamento
├── 📋 requirements.txt        # Dependências Python
├── ⚙️ env.example             # Variáveis de ambiente
├── 🌐 nginx.conf              # Configuração da API mock
└── 📖 README.md               # Documentação
```

## 🚀 Como Executar

### Pré-requisitos

- **Docker** (versão 20.10+)
- **Docker Compose** (versão 2.0+)
- **Git** (para clonar o repositório)

### 🐳 Execução com Docker Compose (Recomendado)

1. **Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd data-processing-agent
```

2. **Configure as variáveis de ambiente:**
```bash
cp env.example .env
# Edite o arquivo .env conforme necessário
```

3. **Execute o sistema:**
```bash
docker-compose up --build
```

4. **Para executar em background:**
```bash
docker-compose up -d --build
```

5. **Para visualizar logs:**
```bash
docker-compose logs -f data-agent
```

### 🐳 Execução com Imagem Docker Pública (Simulada)

Se você tivesse uma imagem pública no Docker Hub, seria assim:

```bash
# Pull da imagem (simulado)
docker pull seu-usuario/data-agent:latest

# Execução
docker run -d \
  --name data-processing-agent \
  -e ENVIRONMENT=production \
  -e LOG_LEVEL=INFO \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/logs:/app/logs \
  seu-usuario/data-agent:latest
```

### 🐍 Execução Local (Desenvolvimento)

1. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

2. **Configure as variáveis de ambiente:**
```bash
cp env.example .env
```

3. **Execute o agente:**
```bash
python main.py
```

## 📊 O que o Job Faz

### 🔄 Processo de Execução

1. **Inicialização**: Carrega configurações e prepara o ambiente
2. **Geração de Dados**: Cria 100 registros fictícios de vendas
3. **Processamento**: Analisa os dados com pandas
4. **Análise**: Calcula métricas de negócio
5. **Relatório**: Exibe resultados formatados no terminal
6. **Exportação**: Salva relatórios em JSON e CSV

### 📈 Métricas Calculadas

- **💰 Receita Total**: Soma de todas as vendas
- **📦 Total de Vendas**: Quantidade de transações
- **📈 Ticket Médio**: Valor médio por venda
- **🏆 Top 5 Produtos**: Produtos com maior receita
- **📂 Performance por Categoria**: Análise por categoria
- **💳 Métodos de Pagamento**: Distribuição dos pagamentos
- **🗺️ Vendas por Região**: Análise geográfica

### 📁 Arquivos Gerados

- `data/sales_data.json`: Dados brutos das vendas
- `reports/sales_report_YYYYMMDD_HHMMSS.json`: Relatório executivo
- `reports/sales_data_YYYYMMDD_HHMMSS.csv`: Dados em formato CSV
- `logs/agent.log`: Logs de execução

## 🧪 Testes e Validação

### ✅ Verificar se está funcionando

1. **Execute o sistema:**
```bash
docker-compose up --build
```

2. **Verifique a saída no terminal** - você deve ver:
   - Banner colorido de inicialização
   - Logs de processamento
   - Tabelas com métricas de vendas
   - Confirmação de arquivos salvos

3. **Verifique os arquivos gerados:**
```bash
ls -la data/
ls -la reports/
ls -la logs/
```

### 🔍 Comandos úteis para debug

```bash
# Ver logs em tempo real
docker-compose logs -f data-agent

# Entrar no container
docker-compose exec data-agent bash

# Verificar status dos containers
docker-compose ps

# Parar todos os serviços
docker-compose down

# Limpar tudo (incluindo volumes)
docker-compose down -v --rmi all
```

## ⚙️ Configuração

### Variáveis de Ambiente

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| `ENVIRONMENT` | Ambiente de execução | `production` |
| `LOG_LEVEL` | Nível de logging | `INFO` |
| `DATA_SOURCE` | Fonte dos dados | `sales_data` |
| `BATCH_SIZE` | Tamanho do lote | `100` |

### Personalização

Para personalizar o comportamento:

1. **Edite o arquivo `.env`:**
```bash
cp env.example .env
nano .env
```

2. **Modifique `job_example.py`** para alterar a lógica de processamento

3. **Ajuste `main.py`** para modificar o fluxo principal

## 📦 Estrutura de Dados

### Exemplo de Registro de Venda

```json
{
  "id": 1,
  "product_name": "Smartphone Galaxy S23",
  "category": "Eletrônicos",
  "price": 2999.99,
  "quantity": 2,
  "total_amount": 5999.98,
  "customer_name": "João Silva",
  "customer_email": "joao.silva@email.com",
  "sale_date": "2024-01-15",
  "payment_method": "Cartão de Crédito",
  "region": "São Paulo"
}
```

## 🔧 Desenvolvimento

### Estrutura do Código

- **`main.py`**: Ponto de entrada, configuração e orquestração
- **`job_example.py`**: Lógica de negócio e processamento de dados
- **`SalesDataProcessor`**: Classe principal com métodos de análise

### Adicionando Novas Funcionalidades

1. **Novas métricas**: Adicione métodos na classe `SalesDataProcessor`
2. **Novos formatos**: Implemente novos métodos de exportação
3. **Integrações**: Use as variáveis de ambiente para APIs externas

## 🐛 Troubleshooting

### Problemas Comuns

**❌ Erro: "Permission denied"**
```bash
# Solução: Ajustar permissões
sudo chown -R $USER:$USER data/ logs/ reports/
```

**❌ Erro: "Port already in use"**
```bash
# Solução: Parar serviços conflitantes
docker-compose down
sudo lsof -ti:8080 | xargs kill -9
```

**❌ Erro: "Module not found"**
```bash
# Solução: Rebuild da imagem
docker-compose down
docker-compose build --no-cache
docker-compose up
```

## 📞 Suporte

Para dúvidas ou problemas:

1. **Verifique os logs**: `docker-compose logs data-agent`
2. **Consulte a documentação**: Este README
3. **Teste localmente**: Execute `python main.py` diretamente

## 📄 Licença

Este projeto é uma demonstração técnica. Use conforme necessário para fins educacionais e de avaliação.

---

**🎯 Objetivo Alcançado**: Sistema profissional, containerizado e funcional para prova de capacidade técnica! #
