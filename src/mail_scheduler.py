import pandas as po
import sys
from datetime import datetime



def envio_automatico(): # En esta función buscaremos que nuestro csv tenga listo fechas de envíos y los datos a rellenar para que el script se ejecute de manera automática.
    '''
    FUTURE FEATURE: La mayoría de las veces vamos a usar los csv que se encuentran
    en la carpeta /assets/schedule pero podemos editar este apartado para seleccionar 
    el archivo específico con sys os
    '''
    csv_de_rellenado = "assets/Schedule/Calendario_Mantenimiento_Computadoras_2026.csv"  # Para cambiar el archivo a analizar habrá que cambiar el hardcode
    datos_recolectados_del_dia = []
    try:
        df = po.read_csv(csv_de_rellenado, encoding="utf-8") # Cargamos el archivo a pandas (el encoding es para que los acentos no generen caracteres raros)
        fecha_actual = datetime.now().strftime("%d/%m/%Y") 

        for posicion, fecha in enumerate(df["Fecha"]):
            if fecha == fecha_actual: # Al automatizar la ejecución diaria, buscamos que la fecha de agenda sea la misma del día que se ejecuta
                for datos in df.iloc[posicion]:
                           # El script leerá la columna fecha y cuando coincida con la fecha del día de ejecución tomará los datos de esa fila en específico
                    datos_recolectados = {
                    "Fecha": fecha,
                    "Area": datos["Área"],
                    "Hora_de_Inicio": datos["Inicio"],
                    "Hora_de_Fin": datos["Fin"]
                    }
                    datos_recolectados_del_dia.append(datos_recolectados)
            else:
                pass

    except FileNotFoundError:
        print("[!]ERROR El archivo no existe o no se encuentra en el directorio mencionado.")
    


def envio_semiautomatico(): # En esta función buscaremos que nuestro csv tenga listo solo los datos a rellenar, será necesario ejecutar el script manualmente.
    pass