import pandas as pd


def lectura_y_unificacion_de_ficheros(anios):
    df = []
    columnas = None

    for anio in anios:
        dataset = pd.read_excel(f"./Data/{anio}_Accidentalidad.xlsx")
        if columnas is None:
            columnas = set(dataset.columns)
        else:
            if set(dataset.columns) != columnas:
                print(f"Las columnas del anio {anio} no coinciden")
                continue

        df.append(dataset)

    if df:
        df = pd.concat(df, ignore_index=True)
        print("Archivos unificados correctamente")
        return df
    else:
        print("No se han podido unificar los archivos")
        return None


def limpieza_de_dataset(df):
    return df.drop(['coordenada_x_utm', 'coordenada_y_utm'], axis=1, inplace=True)


if __name__ == "__main__":
    anios = [2019, 2020, 2021, 2022, 2023, 2024]

    df_unificado = lectura_y_unificacion_de_ficheros(anios)
    df_limpiado = limpieza_de_dataset(df_unificado)
