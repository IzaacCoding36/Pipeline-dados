import json
import csv
import os

from processamento_dados import Dados

# Determine the correct paths based on current working directory
if os.path.basename(os.getcwd()) == 'scripts':
    # Running from scripts directory
    path_json = '../data_raw/dados_empresaA.json'
    path_csv = '../data_raw/dados_empresaB.csv'
    path_dados_combinados = '../data_processed/dados_combinados.csv'
else:
    # Running from root directory
    path_json = 'data_raw/dados_empresaA.json'
    path_csv = 'data_raw/dados_empresaB.csv'
    path_dados_combinados = 'data_processed/dados_combinados.csv'

#Extract

dados_empresaA = Dados.leitura_dados(path_json, 'json')
print(dados_empresaA.nome_colunas)
print(dados_empresaA.qtd_linhas)

dados_empresaB = Dados.leitura_dados(path_csv, 'csv')
print(dados_empresaB.nome_colunas)
print(dados_empresaB.qtd_linhas)

#Transform

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.nome_colunas)

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(dados_fusao.nome_colunas)
print(dados_fusao.qtd_linhas)

#Load

dados_fusao.salvando_dados(path_dados_combinados)
print(f"Dados salvos em: {path_dados_combinados}")

# # Iniciando a leitura
# dados_json = leitura_dados(path_json,'json')
# nome_colunas_json = get_columns(dados_json)
# tamanho_dados_json = size_data(dados_json)

# print(f"Nome colunas dados json: {nome_colunas_json}")
# print(f"Tamanho dos dados json: {tamanho_dados_json}")

# dados_csv = leitura_dados(path_csv, 'csv')
# nome_colunas_csv = get_columns(dados_csv)
# tamanho_dados_csv = size_data(dados_csv)
# print(nome_colunas_csv)
# print(tamanho_dados_csv)

# #Transformacao dos dados

# key_mapping = {'Nome do Item': 'Nome do Produto',
#                 'Classificação do Produto': 'Categoria do Produto',
#                 'Valor em Reais (R$)': 'Preço do Produto (R$)',
#                 'Quantidade em Estoque': 'Quantidade em Estoque',
#                 'Nome da Loja': 'Filial',
#                 'Data da Venda': 'Data da Venda'}
# dados_csv = rename_columns(dados_csv, key_mapping)
# nome_colunas_csv = get_columns(dados_csv)
# print(nome_colunas_csv)

# dados_fusao = join(dados_json, dados_csv)
# nome_colunas_fusao = get_columns(dados_fusao)
# tamanho_dados_fusao = size_data(dados_fusao)
# print(nome_colunas_fusao)
# print(tamanho_dados_fusao)


# #Salvando dados

# dados_fusao_tabela = transformando_dados_tabela(dados_fusao, nome_colunas_fusao)

# path_dados_combinados = 'data_processed/dados_combinados.csv'

# salvando_dados(dados_fusao_tabela, path_dados_combinados)

# print(path_dados_combinados)