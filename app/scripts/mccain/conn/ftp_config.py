import os
from dotenv import load_dotenv

load_dotenv()

FTP_CONFIG = {
    'server_ftp_mccain': os.getenv('SERVER_FTP_MCCAIN'),
    'user_ftp_mccain': os.getenv('USER_FTP_MCCAIN'),
    'password_ftp_mccain': os.getenv('PASSWORD_FTP_MCCAIN'),
    'path_produto_mccain': os.getenv('PATH_PRODUTO_MCCAIN'),
    'path_clientes_mccain': os.getenv('PATH_CLIENTES_MCCAIN'),
    'path_clientes_sp_mccain': os.getenv('PATH_CLIENTES_SP_MCCAIN'),
    'path_clientes_pr_mccain': os.getenv('PATH_CLIENTES_PR_MCCAIN'),
    'path_estoque_mccain': os.getenv('PATH_ESTOQUE_MCCAIN'),
    'path_estoque_sp_mccain': os.getenv('PATH_ESTOQUE_SP_MCCAIN'),
    'path_estoque_pr_mccain': os.getenv('PATH_ESTOQUE_PR_MCCAIN'),
    'path_vendas_mccain': os.getenv('PATH_VENDAS_MCCAIN'),
    'path_vendas_sp_mccain': os.getenv('PATH_VENDAS_SP_MCCAIN'),
    'path_vendas_pr_mccain': os.getenv('PATH_VENDAS_PR_MCCAIN'),
}
