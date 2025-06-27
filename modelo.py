#importación de librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from statsmodels.tsa.statespace.sarimax import SARIMAX

def obtener_prediccion(departamento, municipio, dia_prediccion):
     # Crea las marcas de tiempo para el inicio y el final del día
     inicio_dia = pd.to_datetime(dia_prediccion + ' 00:00:00+00:00')
     fin_dia = pd.to_datetime(dia_prediccion + ' 23:59:59+00:00')
     #Carga de los archivos csv por año ubicados en: https://drive.google.com/drive/folders/10BtFS1WbWR7ZQ19MlgSB74CF0we8ztUB?usp=drive_link 
     df_2023 = pd.read_csv('D:/DevHitss/unir/Maestria/TFM/humedad_5a/TFM.humedad_2023.csv')
     df_2024 = pd.read_csv('D:/DevHitss/unir/Maestria/TFM/humedad_5a/TFM.humedad_2024.csv')
     df_2025 = pd.read_csv('D:/DevHitss/unir/Maestria/TFM/humedad_5a/TFM.humedad_2025.csv')
     df_2025_2 = pd.read_csv('D:/DevHitss/unir/Maestria/TFM/humedad_5a/TFM.humedad_2025_may_jun.csv')
     #Concatenación de los 6 archivos en un solo dataframe llamado df_concat
     df_concat = pd.concat([df_2023, df_2024, df_2025, df_2025_2], axis=0, ignore_index=True)
     df_concat = df_concat.drop('_id', axis=1)
     #Asegurarnos que la fechamedida sea un tipo de dato datetime
     df_concat['fechamedida'] = pd.to_datetime(df_concat['fechamedida'])
     #Creación de columnas para posterior análisis
     df_concat['anio'] = df_concat['fechamedida'].dt.year
     df_concat['mes'] = df_concat['fechamedida'].dt.month
     df_concat['dia'] = df_concat['fechamedida'].dt.day
     df_concat['hora'] = df_concat['fechamedida'].dt.hour
     df_concat['nombre_mes'] = df_concat['mes'].map({
          1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio'
          , 7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
     })
     df_filtrado = df_concat[df_concat['valorobservado'] != 0]
     df_municipio = df_filtrado[(df_filtrado['departamento'] == departamento) & (df_filtrado['municipio'] == municipio)]
     df_real = df_municipio[(df_municipio['fechamedida'] >= inicio_dia) & (df_municipio['fechamedida'] <= fin_dia)]
     df_municipio = df_municipio[df_municipio['fechamedida'] < inicio_dia]
     df_municipio.set_index('fechamedida', inplace=True)
     serie_municipio = df_municipio['valorobservado'].astype(float).resample('h').mean()
     serie_train = serie_municipio[serie_municipio.index < inicio_dia]
     forecast_index = pd.date_range(start=inicio_dia, end=fin_dia, freq="h")
     modelo = SARIMAX(serie_train, order=(1,1,1), seasonal_order=(1,1,1,24), enforce_stationarity=False, enforce_invertibility=False)
     modelo_entrenado = modelo.fit()
     predicciones = modelo_entrenado.get_forecast(steps=24)
     predicciones_df = predicciones.predicted_mean
     predicciones_df.index = forecast_index
     predicciones_df = predicciones_df.reset_index()
     predicciones_df.columns = ['Hora', 'humedad_predicha']
     predicciones_df['Hora'] = pd.to_datetime(predicciones_df['Hora'])
     predicciones_df['Hora'] = predicciones_df['Hora'].dt.tz_localize(None)
     df_real_agrupado = df_real.groupby('fechamedida')['valorobservado'].mean().reset_index()
     df_real_agrupado['fechamedida'] = pd.to_datetime(df_real_agrupado['fechamedida'])
     df_real_agrupado['fechamedida'] = df_real_agrupado['fechamedida'].dt.tz_localize(None)
     df_real_agrupado.rename(columns={'fechamedida': 'Hora'}, inplace=True)
     df_final = pd.merge(predicciones_df, df_real_agrupado, on='Hora', how='outer')
     # Ordenar por tiempo para asegurar que la gráfica se vea bien
     df_final.sort_values('Hora', inplace=True)
     
     return df_final