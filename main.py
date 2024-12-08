import pandas as pd


def lectura_xlsx(file_path):
    return pd.read_excel(file_path)


def validacion_similitud(df_2019, df_2020, df_2021, df_2022, df_2023, df_2024):
    return True if (list(df_2019.columns) == list(df_2020.columns) == list(df_2021.columns) == list(df_2022.columns) ==
                    list(df_2023.columns) == list(df_2024.columns)) else False


if __name__ == "__main__":
    accidentalidad_2019 = './Data/2019_Accidentalidad.xlsx'
    accidentalidad_2020 = './Data/2020_Accidentalidad.xlsx'
    accidentalidad_2021 = './Data/2021_Accidentalidad.xlsx'
    accidentalidad_2022 = './Data/2022_Accidentalidad.xlsx'
    accidentalidad_2023 = './Data/2023_Accidentalidad.xlsx'
    accidentalidad_2024 = './Data/2024_Accidentalidad.xlsx'

    df_2019 = lectura_xlsx(accidentalidad_2019)
    df_2020 = lectura_xlsx(accidentalidad_2020)
    df_2021 = lectura_xlsx(accidentalidad_2021)
    df_2022 = lectura_xlsx(accidentalidad_2022)
    df_2023 = lectura_xlsx(accidentalidad_2023)
    df_2024 = lectura_xlsx(accidentalidad_2024)

    check = validacion_similitud(df_2019, df_2020, df_2021, df_2022, df_2023, df_2024)

    print("Las columnas son iguales") if check else print("Las columnas son distintas")
