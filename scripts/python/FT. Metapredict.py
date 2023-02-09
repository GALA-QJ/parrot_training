#Modulos requeridos----

import os
import metapredict as meta

# Comparación de desorden: PONDR vs. METAEDICT----

# Obtener el nivel de desorden del proteoma o del fasta
# de interés con metapredict

meta.predict_disorder_fasta(filepath="TAIR_bien.fasta", 
output_file="METAPREDICT_RESULTS/Proteome_disor_META.csv")

# Análisis de biosensores (21) valores de pLDDT----

# Emplear el archivo fasta IDRs_99p. 
os.chdir("DATA/DATA FOR PYTHON/FASTA_META/") #nuevo directorio

# Obtener los valores de pLDDT de AlphaFold con el archivo
meta.predict_pLDDT_fasta(filepath="IDRs_99p_FASTA.fasta", 
output_file="METAPREDICT_RESULTS/IDRs_99p_pLDDT.txt")


