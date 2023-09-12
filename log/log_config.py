import os
import logging

# Diretório onde os arquivos de log serão armazenados
log_dir = 'Z:/repositório/Dusnei-Automation/log'

# Certifique-se de que o diretório exista
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

def setup_logger(log_file_name):
    log_file_path = os.path.join(log_dir, log_file_name)

    # Verifica se o arquivo já existe; se não, cria-o
    if not os.path.exists(log_file_path):
        open(log_file_path, 'w', encoding='utf-8').close()

    # Configuração inicial de logging para o arquivo específico
    logger = logging.getLogger(log_file_name)
    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(log_file_path, encoding='utf-8')
    handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p -'))

    logger.addHandler(handler)
    return loggera

def log_data(logger):
    logger.info('Iniciando varredura de diretório para arquivos de log.')

    # Listando todos os arquivos .log no diretório
    for arquivo in os.listdir(log_dir):
        if arquivo.endswith('.log'):
            logger.info(f'Arquivo de log encontrado: {arquivo}')


# if __name__ == "__main__":
#     mccain_logger = setup_logger('mccain_log.log')
#     brf_logger = setup_logger('brf_log.log')

#     log_data(mccain_logger)
#     log_data(brf_logger)
