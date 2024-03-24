import pandas as pd

# Leggi il file Excel
dati_excel = pd.read_excel(percorso_file_excel, sheet_name=nome_foglio, usecols="O:U", header=None)

# Rinomina le colonne con le lettere
dati_excel.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Rimuovi le righe vuote
dati_excel = dati_excel.dropna()

# Stampa i dati aggiornati
print(dati_excel)
