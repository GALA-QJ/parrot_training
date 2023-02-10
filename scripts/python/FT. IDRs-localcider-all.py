# Modulos requeridos
import os
import pandas as pd
from Bio import SeqIO # Instalar (pip install Bio)
from localcider.sequenceParameters import SequenceParameters # Instalar (pip install localcider)

# Obtener el archivo fasta y dividirlo en archivos individuales por
# cada secuencia que tenga el archivo (usar Bash de Linux). 

# Crear una lista con cada uno de los archivos individuales de las 
# secuencias
filelist = os.listdir("your/path")

# Crear una lista vacía
list_of_IDRs = []

# Poblar la lista vacía con los parámetros de CIDER para cada uno de los
# archivos individuales que contienen las secuencias

# Para obtener el valor de kappa
temp_kappa = [] #Lista temporal vacía
for file in filelist:
    temp_kappa.append((SequenceParameters(sequenceFile=file)).get_kappa())
  
# Para obtener el valor de hidropatía
temp_hidropatia = [] #Lista temporal vacía
for file in filelist:
   temp_hidropatia.append((SequenceParameters(sequenceFile=file)).get_uversky_hydropathy())
  
# Para obtener el valor de carga neta media
temp_carganeta = [] #Lista temporal vacía
for file in filelist:
   temp_carganeta.append((SequenceParameters(sequenceFile=file)).get_mean_net_charge())
  
# Para obtener el valor de desorden promovido
temp_desorden = [] #Lista temporal vacía
for file in filelist:
   temp_desorden.append((SequenceParameters(sequenceFile=file)).get_fraction_disorder_promoting())
  
# Para obtener el valor de FCR (constante para todas las secuencias)
temp_FCR = [] #Lista temporal vacía
for file in filelist:
   temp_FCR.append((SequenceParameters(sequenceFile=file)).get_FCR())
  
# Para obtener el valor de NCPR (constante para todas las secuencias)
temp_NCPR = [] #Lista temporal vacía
for file in filelist:
   temp_NCPR.append((SequenceParameters(sequenceFile=file)).get_NCPR())

# Juantar todas las listas en un dataframe utilizadno el modulo de
# Pandas

# Crear una lista de listas con las variables generadas
CIDER_lists = temp_FCR, temp_kappa, temp_hidropatia, temp_carganeta, temp_desorden, temp_NCPR


# Crear el dataframe con el modulo de Pandas y transponer las columnas
# usando la función "T"
df_CIDER = pd.DataFrame(CIDER_lists, 
index = ['FCR', 'kappa', 'hydropathy', 'charge', 'disorder', 'NCPR']).T

# Exportar dataframe a un archivo de txt para ser usado en R
os.chdir('../') #Retroceder directorios

# Guardar archivo en el directorio de elección
df_CIDER.to_csv('your/PATH/CIDER_values.txt')



# PARA OBTENER LOS DATOS DE NCPR POR CADA RESIDUOS DE AMINOÁCIDO
# SE DEBE EJECUTAR EL SIGUIENTE SCRIPT
# EL CÓDIGO TOMA EN CUENTA VARIABLES ANTERIORES Y DIRECTORIOS
# QUE SE HAYAN UTILIZADO PREVIAMENTE EN EL ANÁLISIS DE LOCALCIDER

# Obtener valores de NCPR por cada residuo
# Para obtener el valor de NCPR (constante para todas las secuencias)
temp_linear_NCPR = [] #Lista temporal vacía
for file in filelist:
   temp_linear_NCPR.append((SequenceParameters(sequenceFile=file)).get_linear_NCPR())

# Obtener los nombres de los biosensores y guardarlos en una lista vacía
lst_NCPR_names = temp_fasta.keys()

# Convertir los nombres (dictionario) a una lista
lst_NCPR_names = list(lst_NCPR_names)

# Generar lista vacía
temp_NCPR = []

# Obtener los datos de NCPR por residuo de cada biosensor
for i in range(0, len(temp_linear_NCPR)):
    # Iterar los valores de NCPR y guardarlos en temp_NCPR
    temp_NCPR.append(temp_linear_NCPR[i][1])

# Convertir lista temp_NCPR a un data frame con Panda
df = pd.DataFrame(temp_NCPR)

# Guardar archivo como CSV
df.to_csv('G:/ALL/Project_IDP_D2P2/DATA/DATA FOR PYTHON/FASTA_CIDER/LIBRARY/IDRBS_library_200_NCPR.csv')
