from sqlalchemy import create_engine, exc
from dotenv import load_dotenv
import os
import logging

load_dotenv()


def log_data():
    for arquivo in os.listdir("Z:/repositório/Dusnei-Automation/log"): # noqa
        if arquivo.endswith('.log'):
            logging.info('Arquivo iniciado')
    logging.basicConfig(
        filename='log/data_mccain.log',
        level=logging.INFO,
        format='%(asctime)s %(message)s',
        datefmt='%d/%m/%Y %I:%M:%S %p -',
)# noqa


def get_db_engine():
    log_data()
    try:
        db_url = os.getenv('DUSNEI_URL')
        engine = create_engine(db_url)
        # Test connection
        with engine.connect() as connection:  # noqa: F841
            logging.info('Conexão estabelecida!')
            pass
        logging.info('Banco de dados conectado!')
        return engine
    except exc.SQLAlchemyError as e:
        logging.info(f"Error: {e}")
        return None
