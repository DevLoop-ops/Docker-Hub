#!/bin/bash

# Script de execução do Agente de Processamento de Dados
# Autor: Engenheiro de Software Sênior
# Versão: 1.0.0

set -e

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para exibir mensagens coloridas
print_message() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}================================${NC}"
    echo -e "${BLUE}  AGENTE DE PROCESSAMENTO DE DADOS${NC}"
    echo -e "${BLUE}================================${NC}"
}

# Verificar se Docker está instalado
check_docker() {
    if ! command -v docker &> /dev/null; then
        print_error "Docker não está instalado. Por favor, instale o Docker primeiro."
        exit 1
    fi
    
    if ! command -v docker-compose &> /dev/null; then
        print_error "Docker Compose não está instalado. Por favor, instale o Docker Compose primeiro."
        exit 1
    fi
    
    print_message "Docker e Docker Compose encontrados!"
}

# Configurar ambiente
setup_environment() {
    if [ ! -f ".env" ]; then
        if [ -f "env.example" ]; then
            print_message "Criando arquivo .env a partir do env.example..."
            cp env.example .env
        else
            print_warning "Arquivo env.example não encontrado. Criando .env básico..."
            cat > .env << EOF
ENVIRONMENT=production
LOG_LEVEL=INFO
DATA_SOURCE=sales_data
EOF
        fi
    fi
    
    # Criar diretórios necessários
    mkdir -p data logs reports
    print_message "Ambiente configurado!"
}

# Função principal
main() {
    print_header
    
    # Verificar dependências
    check_docker
    
    # Configurar ambiente
    setup_environment
    
    # Verificar argumentos
    case "${1:-up}" in
        "up")
            print_message "Iniciando o agente com Docker Compose..."
            docker-compose up --build
            ;;
        "up-d")
            print_message "Iniciando o agente em background..."
            docker-compose up -d --build
            print_message "Agente iniciado! Use 'docker-compose logs -f data-agent' para ver os logs."
            ;;
        "down")
            print_message "Parando o agente..."
            docker-compose down
            ;;
        "logs")
            print_message "Exibindo logs do agente..."
            docker-compose logs -f data-agent
            ;;
        "restart")
            print_message "Reiniciando o agente..."
            docker-compose down
            docker-compose up --build
            ;;
        "clean")
            print_message "Limpando tudo (containers, volumes, imagens)..."
            docker-compose down -v --rmi all
            print_message "Limpeza concluída!"
            ;;
        "status")
            print_message "Status dos containers:"
            docker-compose ps
            ;;
        "shell")
            print_message "Abrindo shell no container do agente..."
            docker-compose exec data-agent bash
            ;;
        "help"|"-h"|"--help")
            echo "Uso: $0 [comando]"
            echo ""
            echo "Comandos disponíveis:"
            echo "  up        - Iniciar o agente (padrão)"
            echo "  up-d      - Iniciar em background"
            echo "  down      - Parar o agente"
            echo "  logs      - Ver logs em tempo real"
            echo "  restart   - Reiniciar o agente"
            echo "  clean     - Limpar tudo (containers, volumes, imagens)"
            echo "  status    - Ver status dos containers"
            echo "  shell     - Abrir shell no container"
            echo "  help      - Mostrar esta ajuda"
            ;;
        *)
            print_error "Comando desconhecido: $1"
            echo "Use '$0 help' para ver os comandos disponíveis."
            exit 1
            ;;
    esac
}

# Executar função principal
main "$@" 