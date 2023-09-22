# pylint: disable=all
import time
import ctypes
import threading
import clientes_estados
import clientes_unidades
import estoques_unidades
import estoques_estados
import produtos_totais
import vendas_estados
import vendas_unidades


MB_OK = 0x0
TIMEOUT = 10000


def show_message_box():
    ctypes.windll.user32.MessageBoxW(0, "Envio de arquivos McCain realizado!", "Automação McCain", MB_OK)


def envio_automatico():
    clientes_estados.clientes_estado()
    clientes_unidades.clientes()
    estoques_estados.estoques_estado()
    estoques_unidades.estoques()
    produtos_totais.produtos()
    vendas_estados.vendas_estado()
    vendas_unidades.vendas()

    t = threading.Thread(target=show_message_box)
    t.start

    time.sleep(TIMEOUT / 1000.0)

    hwnd = ctypes.windll.user32.FindWindowW(None, "Automação McCain")
    if hwnd != 0:
        ctypes.windll.user32.SendMessageW(hwnd, 0x0010, 0, 0)


if __name__ == "__main__":
    envio_automatico()
