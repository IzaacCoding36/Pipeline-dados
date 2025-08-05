# Pipeline-dados

**Esse repositório apresenta uma pipeline de dados utilizando Python e Jupyter Notebook, utilizado no curso de data science da [Alura](https://alura.com.br).**

## Descrição

Este projeto implementa um pipeline ETL (Extract, Transform, Load) que processa dados de vendas de duas empresas diferentes:
- **Empresa A**: Dados em formato JSON (`data_raw/dados_empresaA.json`)
- **Empresa B**: Dados em formato CSV (`data_raw/dados_empresaB.csv`)

O pipeline combina e padroniza os dados das duas fontes em um único arquivo CSV de saída.

## Estrutura do Projeto

```
Pipeline-dados/
├── data_raw/              # Dados brutos de entrada
│   ├── dados_empresaA.json
│   └── dados_empresaB.csv
├── data_processed/        # Dados processados de saída
│   └── dados_combinados.csv
├── scripts/              # Scripts Python do pipeline
│   ├── processamento_dados.py
│   └── fusao_mercado_fev.py
├── notebooks/            # Notebooks Jupyter para exploração
│   └── exploracao.ipynb
└── README.md
```

## Como Usar

### Executar o Pipeline

O pipeline pode ser executado a partir do diretório raiz ou do diretório scripts:

```bash
# A partir do diretório raiz
python scripts/fusao_mercado_fev.py

# A partir do diretório scripts
cd scripts
python fusao_mercado_fev.py
```

### Exploração dos Dados

Use o Jupyter Notebook para explorar os dados:

```bash
jupyter notebook notebooks/exploracao.ipynb
```

## Funcionalidades

- **Leitura de dados**: Suporte para arquivos JSON e CSV
- **Transformação**: Padronização de nomes de colunas entre diferentes fontes
- **Combinação**: União de dados de múltiplas fontes
- **Export**: Geração de arquivo CSV combinado
- **Tratamento de dados faltantes**: Valores ausentes são marcados como "Indisponivel"

## Dependências

- Python 3.x
- csv (biblioteca padrão)
- json (biblioteca padrão)
- os (biblioteca padrão)

## Estrutura dos Dados

O pipeline processa produtos com os seguintes campos:
- Nome do Produto
- Categoria do Produto  
- Preço do Produto (R$)
- Quantidade em Estoque
- Filial
- Data da Venda (quando disponível)
