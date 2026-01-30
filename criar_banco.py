import pandas as pd
from sqlalchemy import create_engine
import os

print("--- INICIANDO A CRIAÇÃO DO BANCO DE DADOS ---")

# 1. Cria a conexão com um banco SQLite novo chamado 'olist.db'
# O banco será criado na mesma pasta onde você está.
engine = create_engine('sqlite:///olist.db')

# 2. Dicionário: Nome do Arquivo CSV -> Nome da Tabela no Banco
arquivos_para_tabelas = {
    'olist_orders_dataset.csv': 'orders',         # Tabela de Pedidos
    'olist_order_items_dataset.csv': 'items',     # Tabela de Itens
    'olist_customers_dataset.csv': 'customers',   # Tabela de Clientes
    'olist_products_dataset.csv': 'products',     # Tabela de Produtos
    'olist_order_payments_dataset.csv': 'payments' # Tabela de Pagamentos
}

# 3. Loop para processar cada arquivo
for arquivo_csv, nome_tabela in arquivos_para_tabelas.items():
    try:
        print(f"Lendo arquivo: {arquivo_csv}...")
        df = pd.read_csv(arquivo_csv)
        
        print(f" --> Salvando como tabela '{nome_tabela}' no banco de dados...")
        df.to_sql(nome_tabela, engine, index=False, if_exists='replace')
        print(" --> OK!")
        
    except Exception as e:
        print(f"Erro ao processar {arquivo_csv}: {e}")

print("\n✅ PROCESSO CONCLUÍDO!")
print("O arquivo 'olist.db' deve ter aparecido na sua pasta.")