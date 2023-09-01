# flake8: noqa
# pylint: disable=all
from sqlalchemy import create_engine, exc
from dotenv import load_dotenv
from loguru import logger
import os


class DatabaseConnection:
    def __init__(self):
        load_dotenv()
        self.DUSNEI_LOG_DIRECTORY = os.getenv('DUSNEI_LOG_DIRECTORY')
        self.LOG_FILE = os.path.join(self.DUSNEI_LOG_DIRECTORY, 'data.log')
        self.db_url = os.getenv('DUSNEI_URL')

    def initialize_logging(self):
        logger.add(
            sink='Z:/repositório/Dusnei-Automation/log/log_{time:YYYY-MM-DD}.log', 
            level='INFO', 
            rotation='1 day',
            format='{time:YYYY-MM-DD} | {function}: {message}'
        )

    def log_data(self):        
        for arquivo in os.listdir(self.DUSNEI_LOG_DIRECTORY):
            if arquivo.endswith('.log'):
                logger.info('Arquivo iniciado')

        
    def get_db_engine(self):
        try:
            self.db_url = os.getenv('DUSNEI_URL')
            engine = create_engine(self.db_url)
            # Test connection
            with engine.connect() as connection:
                logger.info('Conexão estabelecida!')
                pass
            logger.info('Banco de dados conectado!')
            return engine
        except exc.SQLAlchemyError as e:
            logger.info(f"Error: {e}")
            return None


if __name__ == "__main__":
    db_connection = DatabaseConnection()
    db_connection.initialize_logging()
    db_connection.log_data()
    db_connection.get_db_engine()