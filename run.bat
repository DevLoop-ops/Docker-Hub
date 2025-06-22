@echo off
REM Script de execução do Agente de Processamento de Dados para Windows
REM Autor: Engenheiro de Software Sênior
REM Versão: 1.0.0

setlocal enabledelayedexpansion

REM Cores para output (Windows)
set "RED=[91m"
set "GREEN=[92m"
set "YELLOW=[93m"
set "BLUE=[94m"
set "NC=[0m"

REM Função para exibir mensagens coloridas
:print_message
echo %GREEN%[INFO]%NC% %~1
goto :eof

:print_warning
echo %YELLOW%[WARNING]%NC% %~1
goto :eof

:print_error
echo %RED%[ERROR]%NC% %~1
goto :eof

:print_header
echo %BLUE%================================%NC%
echo %BLUE%  AGENTE DE PROCESSAMENTO DE DADOS%NC%
echo %BLUE%================================%NC%
goto :eof

REM Verificar se Docker está instalado
:check_docker
docker --version >nul 2>&1
if errorlevel 1 (
    call :print_error "Docker não está instalado. Por favor, instale o Docker primeiro."
    exit /b 1
)

docker-compose --version >nul 2>&1
if errorlevel 1 (
    call :print_error "Docker Compose não está instalado. Por favor, instale o Docker Compose primeiro."
    exit /b 1
)

call :print_message "Docker e Docker Compose encontrados!"
goto :eof

REM Configurar ambiente
:setup_environment
if not exist ".env" (
    if exist "env.example" (
        call :print_message "Criando arquivo .env a partir do env.example..."
        copy env.example .env >nul
    ) else (
        call :print_warning "Arquivo env.example não encontrado. Criando .env básico..."
        (
            echo ENVIRONMENT=production
            echo LOG_LEVEL=INFO
            echo DATA_SOURCE=sales_data
        ) > .env
    )
)

REM Criar diretórios necessários
if not exist "data" mkdir data
if not exist "logs" mkdir logs
if not exist "reports" mkdir reports

call :print_message "Ambiente configurado!"
goto :eof

REM Função principal
:main
call :print_header

REM Verificar dependências
call :check_docker
if errorlevel 1 exit /b 1

REM Configurar ambiente
call :setup_environment

REM Verificar argumentos
set "command=%~1"
if "%command%"=="" set "command=up"

if "%command%"=="up" (
    call :print_message "Iniciando o agente com Docker Compose..."
    docker-compose up --build
) else if "%command%"=="up-d" (
    call :print_message "Iniciando o agente em background..."
    docker-compose up -d --build
    call :print_message "Agente iniciado! Use 'docker-compose logs -f data-agent' para ver os logs."
) else if "%command%"=="down" (
    call :print_message "Parando o agente..."
    docker-compose down
) else if "%command%"=="logs" (
    call :print_message "Exibindo logs do agente..."
    docker-compose logs -f data-agent
) else if "%command%"=="restart" (
    call :print_message "Reiniciando o agente..."
    docker-compose down
    docker-compose up --build
) else if "%command%"=="clean" (
    call :print_message "Limpando tudo (containers, volumes, imagens)..."
    docker-compose down -v --rmi all
    call :print_message "Limpeza concluída!"
) else if "%command%"=="status" (
    call :print_message "Status dos containers:"
    docker-compose ps
) else if "%command%"=="shell" (
    call :print_message "Abrindo shell no container do agente..."
    docker-compose exec data-agent bash
) else if "%command%"=="help" (
    echo Uso: %~nx0 [comando]
    echo.
    echo Comandos disponíveis:
    echo   up        - Iniciar o agente (padrão)
    echo   up-d      - Iniciar em background
    echo   down      - Parar o agente
    echo   logs      - Ver logs em tempo real
    echo   restart   - Reiniciar o agente
    echo   clean     - Limpar tudo (containers, volumes, imagens)
    echo   status    - Ver status dos containers
    echo   shell     - Abrir shell no container
    echo   help      - Mostrar esta ajuda
) else (
    call :print_error "Comando desconhecido: %command%"
    echo Use '%~nx0 help' para ver os comandos disponíveis.
    exit /b 1
)

goto :eof

REM Executar função principal
call :main %* 