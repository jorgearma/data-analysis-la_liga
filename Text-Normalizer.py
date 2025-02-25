import os
import re
import shutil
import unicodedata

def eliminar_tildes(texto):
    """Elimina tildes y diacríticos de un texto."""
    return ''.join(c for c in unicodedata.normalize('NFKD', texto) if unicodedata.category(c) != 'Mn')

def eliminar_puntuacion(texto):
    """Elimina los signos de puntuación, excepto ';'."""
    return re.sub(r'[^\w\s;-]', '', texto)

# Ruta del directorio de entrada
directorio_entrada = '/home/siemprearmando/Desktop/data-analysis-la_liga/jornadas/jornada27'
# Ruta del directorio de respaldo
backup_dir = os.path.join(directorio_entrada, 'backup')

# Crear el directorio de respaldo si no existe
os.makedirs(backup_dir, exist_ok=True)

# Recorrer todos los archivos en el directorio de entrada
for archivo in os.listdir(directorio_entrada):
    ruta_entrada = os.path.join(directorio_entrada, archivo)
    
    # Verificar que el archivo es un archivo y no una carpeta
    if os.path.isfile(ruta_entrada):
        nombre_sin_extension, extension = os.path.splitext(archivo)
        ruta_backup = os.path.join(backup_dir, archivo)
        ruta_salida = os.path.join(directorio_entrada, f"{nombre_sin_extension}_normalizado{extension}")
        
        # Copiar archivo original al directorio de backup
        shutil.copy(ruta_entrada, ruta_backup)
        
        # Normalizar y guardar en el directorio original
        with open(ruta_entrada, 'r', encoding='utf-8') as f_in, open(ruta_salida, 'w', encoding='utf-8') as f_out:
            for linea in f_in:
                linea_normalizada = eliminar_tildes(linea)
                linea_normalizada = eliminar_puntuacion(linea_normalizada)
                f_out.write(linea_normalizada)

    # Eliminar el archivo original del directorio de entrada
        os.remove(ruta_entrada)            
        
        print(f"Archivo '{archivo}'normalizado => respaldado del {archivo}  en backup' '")
