import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PATH_PEDIDOS = os.path.join(BASE_DIR, "data", "pedidos")
PATH_PAGAMENTOS = os.path.join(BASE_DIR, "data", "pagamentos")
PATH_OUTPUT = os.path.join(BASE_DIR, "data", "output", "relatorio_pedidos_recusados_2025")
