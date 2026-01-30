import pandas as pd
import os

print("--- INICIANDO TESTE DE LEITURA ---")

# 1. Verifica se o Python está enxergando os arquivos na pasta
print("Arquivos encontrados nesta pasta:")
print(os.listdir())
print("-" * 30)

# 2. Tenta ler o arquivo de Clientes
try:
    print("Tentando ler o arquivo de clientes...")
    df = pd.read_csv('olist_customers_dataset.csv')
    
    print("\n✅ SUCESSO! Consegui ler a tabela.")
    print(f"Total de linhas carregadas: {df.shape[0]}")
    print("\nAqui estão os primeiros clientes:")
    print(df.head())

except FileNotFoundError:
    print("\n❌ ERRO: Não encontrei o arquivo CSV. Verifique se o nome está correto.")
except Exception as e:
    print(f"\n❌ Ocorreu um erro inesperado: {e}")