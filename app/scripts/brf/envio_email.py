# flake8: noqa W293
# pylint: disable=all
import os
import glob
import smtplib
from loguru import logger
from email import encoders
from os.path import basename
from datetime import datetime
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

load_dotenv()

class Envio_Email:
    def __init__(self):
        load_dotenv()
        self.path_dados = os.getenv('DUSNEI_DATA_DIRECTORY_BRF')
        self.password_email = os.getenv('EMAIL_PASSWORD')
        self.email_from = os.getenv('EMAIL_FROM')
        self.email_to = os.getenv('EMAIL_TO')
        self.email_cc = os.getenv('EMAIL_CC')
        
      
    def envio_email(self):
        data_atual = datetime.now().strftime("%Y-%m-%d-%H:%M")
        data_atual_email = datetime.now().strftime("%Y-%m-%d")
        
        try:
            msg = MIMEMultipart()
            allTo = self.email_cc.split(",") + [self.email_to] 

            msg['From'] = self.email_from 
            msg['To'] = self.email_to
            msg['Cc'] = self.email_cc
            msg['Subject'] = "Relatórios Dusnei"

            body = (f'''
            Boa Tarde.
            
            Dusnei Alimentos,
            Segue relatórios em anexo, da data {data_atual}.
            
            Att.
            Galli, Marcelo L.
            Dusnei Alimentos LTDA
            Cel: +55 44 98862-0946
            ''')

            msg.attach(MIMEText(body, 'plain'))

            arquivos = glob.glob(f'{self.path_dados}/{data_atual_email}/*.txt')
            
            # files = [
            #     f"C:/Users/Windows/Documents/Python/GerarDocumentos/arquivosBRF/CLIENTESDUSNEI001{data_atual}.txt",
            #     ...arquivos
            # ]

            for arquivo in arquivos:
                with open(arquivo,'rb') as attachment:
                    part = MIMEApplication(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename=%s" % basename(arquivo))
                    msg.attach(part)
            
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.email_from, self.password_email)
                text = msg.as_string()
                server.sendmail(self.email_from, allTo, text)
                
            logger.info('Email enviado com sucesso!')
        except Exception as e:
            if e.smtp_code == 552:
                logger.error("Email excedeu limite de tamanho!")
            else:
                logger.error(f"SMTP Erro: {e.smtp_error}")
                logger.info(f'Erro ao enviar email: {e}')
        
if __name__ == "__main__":
  envio_email_instance = Envio_Email()
  envio_email_instance.envio_email()