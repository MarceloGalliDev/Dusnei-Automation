# flake8: noqa W293
# pylint: disable=all
import os
import shutil
import glob
from loguru import logger
import estoques, produtos, vendas, forca_de_vendas, clientes
from conn import DatabaseConnection
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

              
def _send_estoque():
    _estoques = estoques.Estoques()
    _estoques.estoques()
    logger.info('Estoques enviado!')

def _send_produtos():
    _produtos = produtos.Produtos()
    _produtos.produtos()
    logger.info('Produtos enviado!')

def _send_vendas():
    _vendas = vendas.Vendas()
    _vendas.vendas()
    logger.info('Vendas enviado!')

def _send_forca_de_vendas():
    _forca_de_vendas = forca_de_vendas.Forca_De_Venda()
    _forca_de_vendas.forca_de_vendas()
    logger.info('Forca_de_vendas enviado!')

def _send_clientes():
    _clientes = clientes.Clientes()
    _clientes.clientes()
    logger.info('Clientes enviado!')

def execution_scripts():
    _send_estoque()
    _send_produtos()
    _send_vendas()
    _send_forca_de_vendas()
    _send_clientes()

    path_brf = os.getenv('DUSNEI_DATA_DIRECTORY_BRF')
    path_brf_ENVIO = os.getenv('DUSNEI_DATA_DIRECTORY_BRF_ENVIO')
    data_pasta = datetime.now().strftime("%Y-%m-%d")
    directory_path = f'{path_brf}/{data_pasta}'

    # Verifica se o diretório existe
    if os.path.exists(directory_path):
        # Lista todos os arquivos no diretório
        files = os.listdir(directory_path)

        # Verifica se o diretório está vazio
        if len(files) != 0:
            for txt_file in glob.glob(os.path.join(directory_path, '*.txt')):
                # Determina o caminho do arquivo de destino
                dest_file = os.path.join(path_brf_ENVIO, os.path.basename(txt_file))
                
                # Copia cada arquivo para o diretório de destino
                shutil.copy2(txt_file, dest_file)
            logger.info("Arquivos enviados a pasta emptor/envio.")
        else:
            logger.info(f"Pasta origem sem arquivos!")
    else:
        logger.info("O diretório não existe.")


if __name__ == "__main__":
    execution_scripts()