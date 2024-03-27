"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df.set_index(df.columns[0], inplace= True)

    df_prueba= df.copy()

    df_prueba["sexo"] = df_prueba["sexo"].str.lower()

    df_prueba["tipo_de_emprendimiento"] = df_prueba["tipo_de_emprendimiento"].str.lower()

    df_prueba["idea_negocio"] = df_prueba["idea_negocio"].str.lower()
    df_prueba["idea_negocio"] = df_prueba["idea_negocio"].str.replace("_"," ")
    df_prueba["idea_negocio"] = df_prueba["idea_negocio"].str.replace("-"," ")
    df_prueba["idea_negocio"] = df_prueba["idea_negocio"].str.strip()

    df_prueba["barrio"] = df_prueba["barrio"].str.lower()
    df_prueba["barrio"] = df_prueba["barrio"].str.replace("_"," ")
    df_prueba["barrio"] = df_prueba["barrio"].str.replace("-"," ")

    df_prueba["comuna_ciudadano"] = df_prueba["comuna_ciudadano"].replace(".",",")

    df_prueba ["fecha_de_beneficio_1"] = pd.to_datetime(df_prueba.fecha_de_beneficio, format = "%Y/%m/%d", errors ="coerce")
    df_prueba ["fecha_de_beneficio_2"] = pd.to_datetime(df_prueba.fecha_de_beneficio, format = "%d/%m/%Y", errors ="coerce")
    df_prueba ["fecha_de_beneficio"] = df_prueba.apply(lambda x: f"{x["fecha_de_beneficio_1"]} {x["fecha_de_beneficio_2"]}", axis = 1)
    df_prueba ["fecha_de_beneficio"] = df_prueba["fecha_de_beneficio"].str.replace("NaT ","")
    df_prueba ["fecha_de_beneficio"] = df_prueba["fecha_de_beneficio"].str.replace(" NaT","")


    df_prueba["monto_del_credito"] = df_prueba["monto_del_credito"].str.replace("$ ","")
    df_prueba["monto_del_credito"] = df_prueba["monto_del_credito"].str.replace(",","")
    df_prueba["monto_del_credito"] = df_prueba["monto_del_credito"].str.replace(".00","")
    df_prueba["monto_del_credito"] = df_prueba["monto_del_credito"].str.strip()

    df_prueba["línea_credito"] = df_prueba["línea_credito"].str.lower()
    df_prueba["línea_credito"] = df_prueba["línea_credito"].str.replace("_"," ")
    df_prueba["línea_credito"] = df_prueba["línea_credito"].str.replace("-"," ")
    df_prueba["línea_credito"] = df_prueba["línea_credito"].str.strip()


    df_prueba= df_prueba.drop(["fecha_de_beneficio_1", "fecha_de_beneficio_2"], axis = 1)

    df_def = df_prueba.dropna(subset=["tipo_de_emprendimiento", "barrio"], how = "any")
    df_def = df_def.drop_duplicates()

    df_def = df_def.sort_values(by = ["sexo", "tipo_de_emprendimiento", "idea_negocio", "barrio", "estrato", "comuna_ciudadano", "fecha_de_beneficio", "monto_del_credito", "línea_credito"], ascending=[False, False, False, False, False, False, False, False, False])

    return df_def
