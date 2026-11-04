# Projeto PySpark - Processamento e Relatório de Vendas

Este projeto foi desenvolvido em PySpark para o trabalho final da disciplina **Data Engineering Programming** (FIAP MBA).

## 1. Descrição Geral
O objetivo da aplicação é realizar a leitura, consolidação e filtragem dos datasets de pedidos de vendas (CSV) e pagamentos (JSON), gerando um relatório em formato **Parquet** com os pedidos cujos pagamentos foram recusados.

## 2. Pré-requisitos
- Python 3.10+
- Java OpenJDK (ex: Java 11 ou 17 para suporte ao PySpark)
- PySpark
- Pytest

## 3. Instalação de Dependências
Para instalar as bibliotecas necessárias, execute no terminal:
pip install -r requirements.txt

## 4. Instruções sobre os Datasets
Os dados de entrada devem ser armazenados na seguinte estrutura de diretórios:
- data/pedidos/: Contém os ficheiros de pedidos (formato CSV com separador ;).
- data/pagamentos/: Contém os ficheiros de pagamentos (formato JSON).
- data/output/: Diretório onde o relatório Parquet final será gravado.

## 5. Como Executar a Aplicação
Para rodar o pipeline principal e gerar o relatório em Parquet:
python main.py

## 6. Como Executar os Testes Unitários
Para validar a lógica de negócio com o pytest:
pytest -o pythonpath=. tests/

## 7. Estrutura do Projeto
projeto-pyspark/
├── config/
│   └── settings.py
├── spark/
│   └── session_manager.py
├── data/
│   ├── io_handler.py
│   ├── pedidos/
│   ├── pagamentos/
│   └── output/
├── business/
│   └── sales_processor.py
├── pipeline/
│   └── orchestrator.py
├── tests/
│   └── test_sales_processor.py
├── main.py
├── pyproject.toml
├── requirements.txt
├── README.md
└── .gitignore
