import dash
from dash import dcc, html, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import datetime
import modelo

departamentos_y_municipios = {
     'AMAZONAS':['LETICIA', 'PUERTO NARINO'],
     'ANTIOQUIA':['ABRIAQUI', 'AMALFI', 'ANGOSTURA', 'ANORI', 'ARMENIA', 'BELLO', 'CALDAS', 'CAREPA', 'COCORNA', 'CONCORDIA', 'DABEIBA', 'EL BAGRE', 'FREDONIA', 'FRONTINO', 'GIRALDO', 'JARDIN', 'LA UNION', 'MEDELLIN', 'NECHI', 'REMEDIOS', 'RETIRO', 'RIONEGRO', 'SAN CARLOS', 'SAN ROQUE', 'SAN VICENTE', 'SANTA BARBARA', 'SANTA FE DE ANTIOQUIA', 'SANTA ROSA DE OSOS', 'SANTO DOMINGO', 'SEGOVIA', 'SONSON', 'TAMESIS', 'TITIRIBI', 'VALDIVIA', 'VEGACHI', 'VENECIA', 'YOLOMBO'],
     'ARAUCA':['ARAUCA', 'SARAVENA'],
     'ARCHIPIELAGO DE SAN ANDRES, PROVIDENCIA Y SANTA CATALINA':['SAN ANDRES', 'SAN ANDRES Y  PROVIDENCIA', 'SAN ANDRES Y  PROVIDENCIA (SANTA ISABEL)'],
     'ATLANTICO':['BARRANQUILLA', 'JUAN DE ACOSTA', 'MANATI', 'REPELON', 'SABANALARGA', 'SOLEDAD'],
     'BOGOTA D.C.':['BOGOTA D.C.'],
     'BOLIVAR':['ACHI', 'ARJONA', 'CARTAGENA DE INDIAS', 'EL CARMEN DE BOLIVAR', 'EL GUAMO', 'MAGANGUE', 'SAN PABLO', 'SANTA CATALINA'],
     'BOYACA':['AQUITANIA', 'BOYACA', 'BUENAVISTA', 'CHINAVITA', 'CHITA', 'CORRALES', 'CUITIVA', 'EL ESPINO', 'GUACAMAYAS', 'GUAYATA', 'GUICAN', 'LA CAPILLA', 'MACANAL', 'MONGUA', 'MONIQUIRA', 'MOTAVITA', 'OTANCHE', 'PAEZ', 'PAIPA', 'PAJARITO', 'PAUNA', 'PESCA', 'PISVA', 'PUERTO BOYACA', 'QUIPAMA', 'RAMIRIQUI', 'SAMACA', 'SAN PABLO DE BORBUR', 'SANTA MARIA', 'SIACHOQUE', 'SOCHA', 'SOCOTA', 'SOGAMOSO', 'TUNJA', 'VENTAQUEMADA', 'VILLA DE LEIVA', 'ZETAQUIRA'],
     'CALDAS':['ANSERMA', 'BELALCAZAR', 'CHINCHINA', 'MANIZALES', 'MANZANARES', 'MARULANDA', 'PENSILVANIA', 'RIOSUCIO', 'SALAMINA', 'SUPIA', 'VILLAMARIA'],
     'CAQUETA':['BELEN DE LOS ANDAQUIES', 'EL PAUJIL', 'FLORENCIA', 'SOLANO'],
     'CASANARE':['MONTERREY', 'OROCUE', 'PAZ DE ARIPORO', 'TAMARA', 'TAURAMENA', 'TRINIDAD', 'YOPAL'],
     'CAUCA':['BALBOA', 'CORINTO', 'EL TAMBO', 'GUAPI', 'INZA', 'LA SIERRA', 'PATIA', 'PIENDAMO', 'POPAYAN', 'PURACE', 'SAN SEBASTIAN', 'TORIBIO'],
     'CESAR':['AGUACHICA', 'AGUSTIN CODAZZI', 'CURUMANI', 'PAILITAS', 'PUEBLO BELLO', 'VALLEDUPAR'],
     'CHOCO':['ACANDI', 'ALTO BAUDO', 'ATRATO', 'BAHIA SOLANO', 'BOJAYA', 'CERTEGUI', 'CONDOTO', 'EL ATRATO', 'EL CARMEN', 'ISTMINA', 'LLORO', 'NOVITA', 'QUIBDO', 'SAN JOSE DEL PALMAR', 'TADO', 'UNGUIA', 'UNION PANAMERICANA'],
     'CORDOBA':['AYAPEL', 'CHIMA', 'MONTERIA', 'PLANETA RICA', 'PUERTO ESCONDIDO', 'PUERTO LIBERTADOR', 'SAHAGUN', 'TIERRALTA'],     
     'CUNDINAMARCA':['ANAPOIMA', 'ANOLAIMA', 'BOGOTA D.C', 'BOJACA', 'CABRERA', 'CARMEN DE CARUPA', 'CHIA', 'CHOACHI', 'CHOCONTA', 'COGUA', 'CUCUNUBA', 'EL COLEGIO', 'FACATATIVA', 'FUNZA', 'GIRARDOT', 'GUADUAS', 'GUASCA', 'GUAYABETAL', 'GUTIERREZ', 'JUNIN', 'LA CALERA', 'LA VEGA', 'MACHETA', 'MEDINA', 'MOSQUERA', 'NEMOCON', 'PACHO', 'PASCA', 'PUERTO SALGAR', 'PULI', 'QUEBRADANEGRA', 'SAN CAYETANO', 'SAN FRANCISCO', 'SIBATE', 'SILVANIA', 'SIMIJACA', 'SOACHA', 'SOPO', 'TABIO', 'TAUSA', 'TENA', 'UBATE', 'VILLAGOMEZ', 'VILLAPINZON', 'VILLETA', 'YACOPI', 'ZIPAQUIRA'],
     'GUAINIA':['INIRIDA'],
     'GUAVIARE':['SAN JOSE DEL GUAVIARE'],
     'HUILA':['AGRADO', 'AIPE', 'ALGECIRAS', 'ALTAMIRA', 'BARAYA', 'CAMPOALEGRE', 'COLOMBIA', 'GARZON', 'GIGANTE', 'LA ARGENTINA', 'LA PLATA', 'NATAGA', 'NEIVA', 'OPORAPA', 'PALERMO', 'PALESTINA', 'PITALITO', 'SALADOBLANCO', 'SAN AGUSTIN', 'SANTA MARIA', 'SUAZA', 'TELLO', 'TERUEL'],
     'LA GUAJIRA':['ALBANIA', 'DIBULLA', 'FONSECA', 'MAICAO', 'RIOHACHA', 'SAN JUAN DEL CESAR', 'URIBIA', 'URUMITA'],
     'MAGDALENA':['CIENAGA', 'EL BANCO', 'FUNDACION', 'SAN SEBASTIAN DE BUENAVISTA', 'SANTA MARTA', 'ZONA BANANERA'],
     'META':['BARRANCA DE UPIA', 'EL CALVARIO', 'GRANADA', 'LEJANIAS', 'PUERTO GAITAN', 'PUERTO LLERAS', 'PUERTO LOPEZ', 'RESTREPO', 'VILLAVICENCIO', 'VISTAHERMOSA'],
     'NARINO':['ALDANA', 'BARBACOAS', 'CONSACA', 'CONTADERO', 'IMUES', 'PASTO', 'PUERRES', 'RICAURTE', 'SANDONA', 'TAMINANGO', 'TANGUA', 'TUMACO'],
     'NORTE DE SANTANDER':['ABREGO', 'ARBOLEDAS', 'CACHIRA', 'CHINACOTA', 'CONVENCION', 'CUCUTA', 'CUCUTILLA', 'GRAMALOTE', 'HERRAN', 'MUTISCUA', 'OCANA', 'PAMPLONA', 'SARDINATA', 'SILOS', 'TIBU', 'TOLEDO'],
     'PUTUMAYO':['MOCOA'],
     'QUINDIO':['ARMENIA', 'BUENAVISTA', 'CALARCA', 'CIRCASIA', 'MONTENEGRO', 'PIJAO', 'SALENTO'],
     'RISARALDA':['APIA', 'BELEN DE UMBRIA', 'GUATICA', 'LA CELIA', 'PEREIRA', 'SANTA ROSA DE CABAL'],
     'SANTANDER':['BARRANCABERMEJA', 'BUCARAMANGA', 'CARCASI', 'CERRITO', 'CHARALA', 'CIMITARRA', 'CONFINES', 'FLORIDABLANCA', 'GIRON', 'LEBRIJA', 'MALAGA', 'MOGOTES', 'ONZAGA', 'PIEDECUESTA', 'PUENTE NACIONAL', 'PUERTO WILCHES', 'SABANA DE TORRES', 'SAN VICENTE DE CHUCURI', 'SOCORRO', 'SURATA', 'TONA', 'VETAS', 'ZAPATOCA'],
     'SUCRE':['MAJAGUAL', 'MORROA', 'SAMPUES', 'SAN BENITO ABAD', 'SAN MARCOS'],
     'TOLIMA':['ALPUJARRA', 'AMBALEMA', 'ANZOATEGUI', 'ARMERO', 'ARMERO (GUAYABAL)', 'ATACO', 'CAJAMARCA', 'CHAPARRAL', 'DOLORES', 'ESPINAL', 'GUAMO', 'IBAGUE', 'LIBANO', 'MARIQUITA', 'MELGAR', 'MURILLO', 'PLANADAS', 'RONCESVALLES', 'ROVIRA', 'SALDANA', 'SAN ANTONIO', 'SANTA ISABEL', 'VALLE DE SAN JUAN'],
     'VALLE DEL CAUCA':['ANSERMANUEVO', 'ARGELIA', 'BUENAVENTURA', 'BUGA', 'CAICEDONIA', 'CALI', 'CARTAGO', 'DAGUA', 'FLORIDA', 'JAMUNDI', 'LA CUMBRE', 'PALMIRA', 'RESTREPO', 'SEVILLA', 'TRUJILLO'],
     'VICHADA':['CUMARIBO', 'LA PRIMAVERA']
}
# Inicializar la aplicación Dash
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout con Bootstrap
app.layout = dbc.Container([
    html.Br(),
    dbc.Row([
        dbc.Col(html.H2("Predicción de Humedad por Municipio"), width={"size": 8, "offset": 2}, className="text-center")
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Label("Departamento"),
            dcc.Dropdown(
                id='departamento-dropdown',
                options=[{'label': k, 'value': k} for k in departamentos_y_municipios.keys()],
                placeholder='Selecciona un departamento'
            ),
        ], md=6),
        dbc.Col([
            dbc.Label("Municipio"),
            dcc.Dropdown(
                id='municipio-dropdown',
                placeholder='Selecciona un municipio'
            ),
        ], md=6),
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Label("Selecciona una fecha"),
            dcc.DatePickerSingle(
                id='calendario-fechas',
                min_date_allowed=datetime.date(2025, 6, 1),
                max_date_allowed=datetime.date(2025, 6, 14),
                initial_visible_month=datetime.date(2025, 6, 1),
                placeholder='Selecciona una fecha',
                display_format='YYYY-MM-DD',
                date=datetime.date(2025, 6, 1)
            )
        ], md=6),
        dbc.Col([
            html.Br(),
            dbc.Button("Generar predicción", id="boton-predecir", color="primary", className="mt-2")
        ], md=6)
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='grafica-lineas')
        ])
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id='tabla-resultados',
                columns=[
                    {'name': 'Hora', 'id': 'Hora'},
                    {'name': 'valorobservado', 'id': 'valorobservado'},
                    {'name': 'humedad_predicha', 'id': 'humedad_predicha'},
                    {'name': 'Intervalo inferior', 'id': 'Intervalo inferior'},
                    {'name': 'Intervalo superior', 'id': 'Intervalo superior'}
                ],
                style_table={'overflowX': 'auto'},
                style_cell={'textAlign': 'center'}
            )
        ])
    ])
], fluid=True)

# Callback para actualizar el municipio según el departamento
@app.callback(
    Output('municipio-dropdown', 'options'),
    Input('departamento-dropdown', 'value')
)
def actualizar_municipios(departamento):
    if departamento:
        return [{'label': m, 'value': m} for m in departamentos_y_municipios[departamento]]
    return []

# Callback para pasar parámetros al otro archivo al hacer clic en botón
@app.callback(
    Output('tabla-resultados', 'data'),
    Output('grafica-lineas', 'figure'),
    Input('boton-predecir', 'n_clicks'),
    State('departamento-dropdown', 'value'),
    State('municipio-dropdown', 'value'),
    State('calendario-fechas', 'date')
)
    
def ejecutar_modelo(n_clicks, departamento, municipio, fecha):
    if n_clicks > 0 and departamento and municipio and fecha:
        df = modelo.obtener_prediccion(departamento, municipio, fecha)

        figura = go.Figure()
        figura.add_trace(go.Scatter(
            x=df['Hora'], y=df['valorobservado'],
            mode='lines+markers', name='Valor Observado'
        ))
        figura.add_trace(go.Scatter(
            x=df['Hora'], y=df['humedad_predicha'],
            mode='lines+markers', name='Humedad Predicha'
        ))
        figura.add_trace(go.Scatter(
            x=df['Hora'],
            y=df['Intervalo inferior'],
            mode='lines',
            line=dict(color='orange', width=1), # Color para la línea del intervalo
            name='Intervalo de Confianza', # Un solo nombre para el par de líneas
            fill='tonexty', # Rellena el área hasta el siguiente trace
            fillcolor='rgba(255, 255, 0, 0.1)', # Color con transparencia (rojo, alpha=0.2)
            showlegend=True # Muestra esta entrada en la leyenda
        ))
        
        # 4. Graficar 'Intervalo superior' (el 'nexty' del trace anterior)
        figura.add_trace(go.Scatter(
            x=df['Hora'],
            y=df['Intervalo superior'],
            mode='lines',
            line=dict(color='orange', width=1), # Mismo color que la línea inferior
            name='_hide_this_trace', # Nombre que no se mostrará en la leyenda
            fill='tonexty', # Rellena el área hasta el siguiente trace
            fillcolor='rgba(255, 255, 0, 0.2)', # Color con transparencia (rojo, alpha=0.2)
            showlegend=False # NO mostrar esta entrada en la leyenda
        ))
        figura.update_layout(
            title={
                'text': 'Comparación de Valor Observado y Humedad Predicha con Intervalo de Confianza',
                'font': {'size': 25}
            },
            xaxis_title={'text': 'Fecha y Hora', 'font': {'size': 20}},
            yaxis_title={'text': 'Valores', 'font': {'size': 20}},
            legend=dict(font=dict(size=12)),
            margin=dict(l=50, r=50, t=80, b=50),
            hovermode='x unified',
            template='plotly_white'
        )

        return df.to_dict('records'), figura

    # Valores por defecto (sin predicción)
    return [], go.Figure()

# Ejecutar la aplicación
if __name__ == '__main__':
    #app.run_server(debug=True)
    app.run(debug=True)