"""
Módulo de Processamento de Dados de Vendas
Contém a lógica principal do agente para análise e relatórios de vendas.
"""

import os
import json
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List, Any
from faker import Faker
from tabulate import tabulate
from colorama import Fore, Style

class SalesDataProcessor:
    """Classe responsável pelo processamento de dados de vendas."""
    
    def __init__(self):
        """Inicializa o processador de dados."""
        self.fake = Faker('pt_BR')
        self.data_dir = 'data'
        self.reports_dir = 'reports'
        
        # Criar diretórios se não existirem
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.reports_dir, exist_ok=True)
    
    def generate_sample_data(self, num_records: int = 100) -> List[Dict[str, Any]]:
        """Gera dados de vendas fictícios para demonstração."""
        print(f"{Fore.BLUE}📊 Gerando {num_records} registros de vendas fictícios...{Style.RESET_ALL}")
        
        sales_data = []
        products = [
            "Smartphone Galaxy S23", "Notebook Dell Inspiron", "Tablet iPad Pro",
            "Smart TV Samsung 55\"", "Fone de Ouvido Sony WH-1000XM4", "Câmera Canon EOS R",
            "Console PlayStation 5", "Smartwatch Apple Watch", "Drone DJI Mini 3",
            "Monitor LG 27\" 4K"
        ]
        
        categories = ["Eletrônicos", "Informática", "Gaming", "Fotografia", "Áudio"]
        
        for i in range(num_records):
            product = self.fake.random_element(products)
            category = self.fake.random_element(categories)
            price = round(self.fake.random.uniform(100, 5000), 2)
            quantity = self.fake.random_int(min=1, max=10)
            sale_date = self.fake.date_between(start_date='-30d', end_date='today')
            
            sale = {
                'id': i + 1,
                'product_name': product,
                'category': category,
                'price': price,
                'quantity': quantity,
                'total_amount': round(price * quantity, 2),
                'customer_name': self.fake.name(),
                'customer_email': self.fake.email(),
                'sale_date': sale_date.strftime('%Y-%m-%d'),
                'payment_method': self.fake.random_element(['Cartão de Crédito', 'PIX', 'Boleto', 'Dinheiro']),
                'region': self.fake.random_element(['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Bahia', 'Paraná'])
            }
            sales_data.append(sale)
        
        return sales_data
    
    def save_data_to_file(self, data: List[Dict[str, Any]], filename: str = 'sales_data.json'):
        """Salva os dados em arquivo JSON."""
        filepath = os.path.join(self.data_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"{Fore.GREEN}💾 Dados salvos em: {filepath}{Style.RESET_ALL}")
    
    def load_data_from_file(self, filename: str = 'sales_data.json') -> List[Dict[str, Any]]:
        """Carrega dados do arquivo JSON."""
        filepath = os.path.join(self.data_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"{Fore.YELLOW}⚠️  Arquivo não encontrado, gerando novos dados...{Style.RESET_ALL}")
            return []
    
    def process_sales_data(self) -> Dict[str, Any]:
        """Processa os dados de vendas e retorna análises."""
        print(f"{Fore.CYAN}🔄 Iniciando processamento de dados de vendas...{Style.RESET_ALL}")
        
        # Gerar ou carregar dados
        sales_data = self.load_data_from_file()
        if not sales_data:
            sales_data = self.generate_sample_data()
            self.save_data_to_file(sales_data)
        
        # Converter para DataFrame
        df = pd.DataFrame(sales_data)
        
        # Análises
        results = {
            'total_sales': len(df),
            'total_revenue': df['total_amount'].sum(),
            'average_order_value': df['total_amount'].mean(),
            'top_products': df.groupby('product_name')['total_amount'].sum().nlargest(5).to_dict(),
            'category_performance': df.groupby('category')['total_amount'].sum().to_dict(),
            'payment_methods': df['payment_method'].value_counts().to_dict(),
            'regional_sales': df.groupby('region')['total_amount'].sum().to_dict(),
            'daily_sales': df.groupby('sale_date')['total_amount'].sum().to_dict(),
            'dataframe': df
        }
        
        print(f"{Fore.GREEN}✅ Processamento concluído!{Style.RESET_ALL}")
        return results
    
    def display_results(self, results: Dict[str, Any]):
        """Exibe os resultados do processamento de forma organizada."""
        print(f"\n{Fore.CYAN}📊 RESUMO EXECUTIVO{Style.RESET_ALL}")
        print("=" * 50)
        
        # Métricas principais
        print(f"{Fore.YELLOW}💰 Receita Total: R$ {results['total_revenue']:,.2f}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}📦 Total de Vendas: {results['total_sales']:,}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}📈 Ticket Médio: R$ {results['average_order_value']:,.2f}{Style.RESET_ALL}")
        
        # Top produtos
        print(f"\n{Fore.CYAN}🏆 TOP 5 PRODUTOS{Style.RESET_ALL}")
        top_products_data = [[k, f"R$ {v:,.2f}"] for k, v in results['top_products'].items()]
        print(tabulate(top_products_data, headers=['Produto', 'Receita'], tablefmt='grid'))
        
        # Performance por categoria
        print(f"\n{Fore.CYAN}📂 PERFORMANCE POR CATEGORIA{Style.RESET_ALL}")
        category_data = [[k, f"R$ {v:,.2f}"] for k, v in results['category_performance'].items()]
        print(tabulate(category_data, headers=['Categoria', 'Receita'], tablefmt='grid'))
        
        # Métodos de pagamento
        print(f"\n{Fore.CYAN}💳 MÉTODOS DE PAGAMENTO{Style.RESET_ALL}")
        payment_data = [[k, v] for k, v in results['payment_methods'].items()]
        print(tabulate(payment_data, headers=['Método', 'Quantidade'], tablefmt='grid'))
        
        # Vendas por região
        print(f"\n{Fore.CYAN}🗺️  VENDAS POR REGIÃO{Style.RESET_ALL}")
        region_data = [[k, f"R$ {v:,.2f}"] for k, v in results['regional_sales'].items()]
        print(tabulate(region_data, headers=['Região', 'Receita'], tablefmt='grid'))
    
    def generate_report(self, results: Dict[str, Any]):
        """Gera um relatório detalhado em arquivo."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_filename = f'sales_report_{timestamp}.json'
        report_path = os.path.join(self.reports_dir, report_filename)
        
        # Preparar dados do relatório
        report_data = {
            'report_info': {
                'generated_at': datetime.now().isoformat(),
                'version': '1.0.0',
                'data_source': os.getenv('DATA_SOURCE', 'sales_data')
            },
            'summary': {
                'total_sales': results['total_sales'],
                'total_revenue': results['total_revenue'],
                'average_order_value': results['average_order_value']
            },
            'detailed_analysis': {
                'top_products': results['top_products'],
                'category_performance': results['category_performance'],
                'payment_methods': results['payment_methods'],
                'regional_sales': results['regional_sales']
            }
        }
        
        # Salvar relatório
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, ensure_ascii=False, indent=2)
        
        print(f"{Fore.GREEN}📄 Relatório salvo em: {report_path}{Style.RESET_ALL}")
        
        # Gerar também um relatório CSV
        csv_filename = f'sales_data_{timestamp}.csv'
        csv_path = os.path.join(self.reports_dir, csv_filename)
        results['dataframe'].to_csv(csv_path, index=False, encoding='utf-8')
        print(f"{Fore.GREEN}📊 Dados CSV salvos em: {csv_path}{Style.RESET_ALL}") 