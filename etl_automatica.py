#!/usr/bin/env python
# coding: utf-8

from datetime import datetime, timedelta
import time
import pandas as pd
from sodapy import Socrata
from pymongo import MongoClient
from unidecode import unidecode

client = Socrata("www.datos.gov.co", None)

def tratamiento_datos_carga(df_results):
     #Tratamiento de datos
     df_results['fechamedida'] = pd.to_datetime(df_results['fechaobservacion'])
     df_results['valorobservado'] = df_results['valorobservado'].fillna(0).astype(int)
     df_results['valorobservado'] = df_results['valorobservado'].astype(int)
     df_results['nombreestacion'] = df_results['nombreestacion'].apply(lambda x: unidecode(x))
     df_results['departamento'] = df_results['departamento'].apply(lambda x: unidecode(x))
     df_results['municipio'] = df_results['municipio'].apply(lambda x: unidecode(x))
     df_results['zonahidrografica'] = df_results['zonahidrografica'].apply(lambda x: unidecode(x))
     df_results['ubicacion'] = df_results.apply(
     lambda row: {
          'latitud': float(row['latitud']),
          'longitud': float(row['longitud'])
     },
     axis=1
     )
     #Inicia conexión a bd
     client = MongoClient("mongodb://localhost:27017/")
     db = client["TFM"]
     collection = db["datalake_humedad"]
     # Insertar los datos como diccionarios
     collection.insert_many(df_results.to_dict('records'))
     
     print("Se cargaron con exito: ", len(df_results))

def ideam(fecha_inicial, fecha_final):
     results = client.get(
     "uext-mhny",
     limit=7000, 
     order="fechaobservacion ASC",
     where=f"fechaobservacion >= '{fecha_inicial}' AND fechaobservacion < '{fecha_final}'")
     df_results = pd.DataFrame.from_records(results)
     tratamiento_datos_carga(df_results)

if __name__ == "__main__":
     dias = 2
     lista_dfs = []
     
     for dia in range(0, 60, dias):
          fecha_inicial = '2007-06-29T00:00:00'
          fecha_inicial = datetime.strptime(fecha_inicial, "%Y-%m-%dT%H:%M:%S") + timedelta(dia)
          fecha_final = fecha_inicial + timedelta(days=dias)
          fecha_inicial = fecha_inicial.strftime('%Y-%m-%dT%H:%M:%S')
          fecha_final = fecha_final.strftime('%Y-%m-%dT%H:%M:%S')
          print("Fecha inicial: ", fecha_inicial)
          print("Fecha final: ", fecha_final)
          ideam(fecha_inicial, fecha_final)
          time.sleep(1)