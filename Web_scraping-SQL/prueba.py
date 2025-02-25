import os

disciplina_stats = 1,2,3,4,5
efiencia_stats = 1,2,3
# Definir el directorio de destino
directory = '/home/siemprearmando/Desktop/data-analysis-la_liga/jornadas/jornada27'

# Crear la carpeta si no existe
os.makedirs(directory, exist_ok=True)

# Definir rutas de archivos

stats1 = os.path.join(directory, 'eficiencia_stats.txt')
stats2 = os.path.join(directory, 'disciplina_stats.txt')


