"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    import pandas as pd
    import os

    df = pd.read_csv('files/input/solicitudes_de_credito.csv', delimiter=';', encoding='utf-8', index_col=0)

    df = df.dropna()

    df['sexo'] = df['sexo'].str.lower().str.strip()

    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower().str.strip()

    df['idea_negocio'] = df['idea_negocio'].str.replace('_', ' ').str.replace('-', ' ')
    df['idea_negocio'] = df['idea_negocio'].str.lower().str.strip()

    df['barrio'] = df['barrio'].astype(str)
    df['barrio'] = df['barrio'].str.replace('_', ' ').str.replace('-', ' ')
    df['barrio'] = df['barrio'].str.lower()
    df['barrio'] = df['barrio'].str.replace(r'no\.\s*(\d+)', r'no\1', regex=True)

    df['estrato'] = df['estrato'].astype(int)

    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)

    df['monto_del_credito'] = df['monto_del_credito'].replace({'\$': '', ',': '', ' ': ''}, regex=True)
    df['monto_del_credito'] = df['monto_del_credito'].astype(float)

    def organizarFecha(date):
        try:
            return pd.to_datetime(date, format='%Y/%m/%d')
        except ValueError:
            return pd.to_datetime(date, format='%d/%m/%Y')

    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(organizarFecha)

    df['línea_credito'] = df['línea_credito'].str.replace('-', ' ').str.replace('_', ' ')
    df['línea_credito'] = df['línea_credito'].str.lower().str.strip()

    df = df.drop_duplicates()

    os.makedirs('files/output/', exist_ok=True)
    df.to_csv('files/output/solicitudes_de_credito.csv', index=False, sep=';')

if __name__ == '__main__':
    print(pregunta_01())

