#Modulos requeridos----

import os
import metapredict as meta

#Comparación de desorden: PONDR vs. METAEDICT----

#Antes de iniciar, cambiar el directorio actual de trabajo de
#Python en donde estarán los archivos fasta

os.chdir('DATA/DATA FOR PYTHON/FASTA_META/') #Nuevo dir

#Realizar una limpieza del archivo fasta para eliminar aminoácidos
#inválidos usando el modulo de "protfasta"

import protfasta

#Remover los aminácidos inválidos

temp_fasta = protfasta.read_fasta('DATA/DATA FOR PYTHON/FASTA_META/TAIR_bien.txt', 
invalid_sequence_action='remove')

#Guardar archivo fasta limpiado

protfasta.write_fasta(temp_fasta, 
'DATA/DATA FOR PYTHON/FASTA_META/TAIR_bien_FASTAc.fasta', 
linelength=6000)


#Obtener el nivel de desorden del proteoma o del fasta
#de interés con metapredict

meta.predict_disorder_fasta(filepath="TAIR_bien.fasta", 
output_file="METAPREDICT_RESULTS/Proteome_disor_META.csv")




#Análisis de biosensores (21) valores de pLDDT----

#Emplear el archivo fasta IDRs_99p. 
os.chdir("DATA/DATA FOR PYTHON/FASTA_META/") #nuevo directorio

#Obtener los valores de pLDDT de AlphaFold con el archivo
meta.predict_pLDDT_fasta(filepath="IDRs_99p_FASTA.fasta", 
output_file="METAPREDICT_RESULTS/IDRs_99p_pLDDT.txt")



#Obtención del nivel de desorden por aa----

#Emplear el archivo fasta IDRs_99p. 
os.chdir("DATA/DATA FOR PYTHON/FASTA_META/") #nuevo directorio

#Obtener los valores de pLDDT de AlphaFold con el archivo
meta.predict_disorder_fasta(filepath="IDRs_99p_FASTA.fasta", 
output_file="METAPREDICT_RESULTS/IDRs_99p_disorder.txt")



