import unicodedata
import re

# Función para eliminar tildes, caracteres especiales y normalizar "ü"
def eliminar_tildes(texto):
    texto = unicodedata.normalize('NFD', texto)  # Normaliza caracteres (separar tildes y diéresis)
    texto = texto.encode('ascii', 'ignore')      # Elimina tildes, diéresis y caracteres no ASCII
    texto = texto.decode('utf-8')               # Convierte de bytes a string
    return texto

# Función para eliminar puntuación, excepto el ";"
def eliminar_puntuacion(texto):
    # Elimina todo lo que no sea letras, números, espacios o ";"
    return re.sub(r'[^\w\s;]', '', texto)

# Ruta del archivo de entrada y salida
archivo_entrada = '/home/siemprearmando/Desktop/data-analysis-la_liga/jornadas/jornada25/index_equipo_posicion.txt'
archivo_salida = '/home/siemprearmando/Desktop/data-analysis-la_liga/jornadas/jornada25/index_equipo_posicion_normalizado.txt'

# Procesar el archivo
with open(archivo_entrada, 'r', encoding='utf-8') as f_in, open(archivo_salida, 'w', encoding='utf-8') as f_out:
    for linea in f_in:
        # Eliminar tildes, diéresis y caracteres especiales
        linea_normalizada = eliminar_tildes(linea)
        # Eliminar puntuación, excepto el ";"
        linea_normalizada = eliminar_puntuacion(linea_normalizada)
        # Escribir la línea normalizada en el archivo de salida
        f_out.write(linea_normalizada)

print(f"Archivo normalizado guardado en: {archivo_salida}")