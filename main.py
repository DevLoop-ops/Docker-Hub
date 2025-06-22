#!/usr/bin/env python3
"""
Agente de Processamento de Dados - Sistema de Relatórios de Vendas
Autor: Engenheiro de Software Sênior
Empresa: DevLoop - Soluções em Tecnologia
Versão: 1.0.0
"""

import os
import sys
import logging
from datetime import datetime
from dotenv import load_dotenv
from colorama import init, Fore, Style

from job_example import SalesDataProcessor

# Inicializar colorama para output colorido
init(autoreset=True)

# Configurar logging
def setup_logging():
    """Configura o sistema de logging da aplicação."""
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    logging.basicConfig(
        level=getattr(logging, log_level),
        format=log_format,
        handlers=[
            logging.FileHandler('logs/agent.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger(__name__)

def print_banner():
    """Exibe o banner de inicialização do agente."""
    banner = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
║                    AGENTE DE PROCESSAMENTO DE DADOS                    ║
║                         Sistema de Relatórios                         ║
║                              v1.0.0                                   ║
║                    Desenvolvido pela DevLoop                          ║
╚══════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)

def main():
    """Função principal do agente."""
    try:
        # Carregar variáveis de ambiente
        load_dotenv()
        
        # Configurar logging
        logger = setup_logging()
        
        # Exibir banner
        print_banner()
        
        logger.info("🚀 Iniciando Agente de Processamento de Dados")
        logger.info(f"📅 Data/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info(f"🌍 Ambiente: {os.getenv('ENVIRONMENT', 'development')}")
        logger.info(f"📊 Fonte de Dados: {os.getenv('DATA_SOURCE', 'sales_data')}")
        logger.info("🏢 Desenvolvido pela DevLoop - Soluções em Tecnologia")
        
        print(f"{Fore.GREEN}✅ Configuração inicializada com sucesso!{Style.RESET_ALL}")
        
        # Criar instância do processador
        processor = SalesDataProcessor()
        
        # Executar processamento
        print(f"\n{Fore.YELLOW}🔄 Iniciando processamento de dados...{Style.RESET_ALL}")
        results = processor.process_sales_data()
        
        # Exibir resultados
        print(f"\n{Fore.GREEN}📈 Resultados do Processamento:{Style.RESET_ALL}")
        processor.display_results(results)
        
        # Gerar relatório
        print(f"\n{Fore.YELLOW}📋 Gerando relatório final...{Style.RESET_ALL}")
        processor.generate_report(results)
        
        logger.info("✅ Processamento concluído com sucesso!")
        print(f"\n{Fore.GREEN}🎉 Agente finalizado com sucesso!{Style.RESET_ALL}")
        print(f"{Fore.BLUE}💼 DevLoop - Transformando ideias em soluções digitais{Style.RESET_ALL}")
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}⚠️  Processo interrompido pelo usuário{Style.RESET_ALL}")
        logger.warning("Processo interrompido pelo usuário")
        sys.exit(0)
        
    except Exception as e:
        print(f"\n{Fore.RED}❌ Erro durante a execução: {str(e)}{Style.RESET_ALL}")
        logger.error(f"Erro durante a execução: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 