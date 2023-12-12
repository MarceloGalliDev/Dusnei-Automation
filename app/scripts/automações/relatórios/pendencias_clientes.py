# flake8: noqa W293
# pylint: disable=all
import os
import time
import openpyxl
import pandas as pd
from loguru import logger
from datetime import datetime
from dotenv import load_dotenv
from conn import DatabaseConnection

load_dotenv()


class PendenciasClientes():
    def __init__(self):
        load_dotenv()
        self.path_dados = os.getenv('DUSNEI_DATA_DIRECTORY_RELATORIO_PENDENCIAS')
        self.unid_codigos = ["001","002","003","004"]
        self.conn = DatabaseConnection.get_db_engine(self)
        
    def pendencias_clientes_query(self, conn, unid_codigo):
        if isinstance(unid_codigo, list):
            unid_values = ",".join([f"'{code}'" for code in unid_codigo])
        else:
            unid_values = f"'{unid_codigo}'"
        query = (f"""
            SELECT
                pfin.pfin_transacao AS transacao,
                pfin.pfin_status AS status,
                pfin.pfin_datavcto AS datavcto,
                pfin.pfin_pger_conta AS pger_conta,
                pfin.pfin_unid_codigo AS unid_cod,
                pfin.pfin_fpgt_codigo AS fpgt_cod,
                pfin.pfin_vend_codigo AS vend_cod,
                pfin.pfin_codentidade AS entidade_cod,
                pfin.pfin_cnpjcpf AS cnpj,
                pfin.pfin_numerodcto AS nota,
                pfin.pfin_parcela AS parcelas,
                pfin.pfin_valor AS valor,
                pfin.pfin_nparcelas AS nparcelas,
                pfin.pfin_lpgt_codigo AS lpgt_cod,
                pger.pger_descricao AS descricao,
                pger.pger_tipo AS tipo,
                clie.clie_nome AS clie_nome,
                clie.clie_razaosocial AS razaosocial,
                clie.clie_vend_codigo AS clie_vend_cod,
                clie.clie_foneres AS fone_res,
                clie.clie_fonecel AS fone_cel,
                vend.vend_nome AS vend_nome,
                vend.vend_supe_codigo AS supe_cod,
                CONCAT(vend.vend_extra16, vend.vend_extra15) AS vend_cel,
                unid.unid_reduzido AS unidade,
                supe.supe_nome AS supe_nome
            FROM pendfin AS pfin
            LEFT JOIN planoger AS pger ON pfin.pfin_pger_conta = pger.pger_conta
            LEFT JOIN unidades AS unid ON pfin.pfin_unid_codigo = unid.unid_codigo
            LEFT JOIN clientes AS clie ON pfin.pfin_codentidade = clie.clie_codigo
            LEFT JOIN vendedores AS vend ON clie.clie_vend_codigo = vend.vend_codigo
            LEFT JOIN supervisores AS supe ON vend.vend_supe_codigo = supe.supe_codigo
            WHERE pfin.pfin_status = 'P'
            AND pfin.pfin_datavcto < CURRENT_DATE
            AND pfin.pfin_pger_conta IN ('112131')
            GROUP BY 
                pfin.pfin_transacao,
                pfin.pfin_status,
                pfin.pfin_datavcto,
                pfin.pfin_pger_conta,
                pfin.pfin_unid_codigo,
                pfin.pfin_fpgt_codigo,
                pfin.pfin_vend_codigo,
                pfin.pfin_codentidade,
                pfin.pfin_cnpjcpf,
                pfin.pfin_numerodcto,
                pfin.pfin_parcela,
                pfin.pfin_valor,
                pfin.pfin_nparcelas,
                pfin.pfin_lpgt_codigo,
                pger.pger_descricao,
                pger.pger_tipo,
                clie.clie_nome,
                clie.clie_razaosocial,
                clie.clie_vend_codigo,
                clie.clie_foneres,
                clie.clie_fonecel,
                vend.vend_nome,
                vend.vend_supe_codigo,
                vend.vend_extra16,
                vend.vend_extra15,
                unid.unid_reduzido, 
                supe.supe_nome
            ORDER BY pfin.pfin_datavcto DESC
        """)
        return pd.read_sql_query(query, conn)