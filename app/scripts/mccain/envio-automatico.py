# flake8: noqa
from clientes import clientes
from estoques import estoques
from produtos import produtos
from clientes_estado import clientes_estado 
from estoques_estado import estoques_estado
from vendas_estado_arquivo_concat_pr import vendas_estado as vendas_estado_arquivo_concat_pr
from vendas_estado_arquivo_concat_sp import vendas_estado as vendas_estado_arquivo_concat_sp
from vendas_estado_arquivo_unico_pr import vendas_estado as vendas_estado_arquivo_unico_pr
from vendas_estado_arquivo_unico_sp import vendas_estado as vendas_estado_arquivo_unico_sp
from vendas_arquivo_001 import vendas as vendas001
from vendas_arquivo_002 import vendas as vendas002
from vendas_arquivo_003 import vendas as vendas003


import time

import ctypes
import threading


MB_OK = 0x0
TIMEOUT = 10000


def show_message_box():
    ctypes.windll.user32.MessageBoxW(0, "Envio de arquivos McCain realizado!", "Automação McCain", MB_OK)


def envio_automatico():
    clientes()
    estoques()
    produtos()
    vendas001()
    vendas002()
    vendas003()
    clientes_estado()
    vendas_estado_arquivo_concat_pr()
    vendas_estado_arquivo_concat_sp()
    vendas_estado_arquivo_unico_pr()
    vendas_estado_arquivo_unico_sp()
    estoques_estado()
   
    t = threading.Thread(target=show_message_box)
    t.start

    time.sleep(TIMEOUT / 1000.0)

    hwnd = ctypes.windll.user32.FindWindowW(None, "Automação McCain")
    if hwnd != 0:
        ctypes.windll.user32.SendMessageW(hwnd, 0x0010, 0, 0)
    
    
if __name__ == "__main__":
    envio_automatico()