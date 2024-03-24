import pandas as pd
from itertools import product
import calendar
import random

def trova_combinazione_meno_frequente(percorso_file_excel, nome_foglio):
    # Leggi solo le colonne specifiche dal file Excel
    colonne = ["O", "P", "Q", "R", "S", "T", "U"]
    dtype = {
        "O": str,  # Giorno della settimana
        "P": int,  # Giorno del mese
        "Q": str,  # Mese
        "R": int,  # Anno
        "S": int,  # Ora
        "T": int,  # Minuto
        "U": str   # AM/PM
    }

    dati_excel = pd.read_excel(percorso_file_excel, sheet_name=nome_foglio, header=None, usecols="O:U", dtype=dtype)

    dati_excel.columns = ['O', 'P', 'Q', 'R', 'S', 'T', 'U']

    dati_excel = dati_excel.dropna()

    combinazioni = genera_combinazioni()
    conteggio_combinazioni = {comb: 0 for comb in combinazioni}

    # Conta le occorrenze di ciascuna combinazione nei dati forniti
    for index, riga in dati_excel.iterrows():
        combinazione = (
            riga["O"],  # Giorno della settimana
            riga["P"],  # Giorno del mese
            riga["Q"],  # Mese
            riga["R"],  # Anno
            riga["S"],  # Ora
            riga["T"],  # Minuto
            riga["U"]   # AM/PM
        )
        if combinazione in conteggio_combinazioni:
            conteggio_combinazioni[combinazione] += 1

    minima_frequenza = min(conteggio_combinazioni.values())

    combinazioni_meno_frequenti = [comb for comb, freq in conteggio_combinazioni.items() if freq == minima_frequenza]

    if minima_frequenza == 0:
        nuova_combinazione = genera_combinazioni()
        return nuova_combinazione, 0

    if len(combinazioni_meno_frequenti) == 1:
        return combinazioni_meno_frequenti[0], minima_frequenza
    else:
        return random.choice(combinazioni_meno_frequenti), minima_frequenza

def genera_combinazioni():
    giorni_settimana = ["lun", "mar", "mer", "gio", "ven", "sab", "dom"]
    mesi = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]
    anni = [2024]  # Escludi gli anni 2023
    ore = list(range(1, 13))
    minuti = list(range(0, 60))
    am_pm = ["am", "pm"]

    giorni_del_mese = []
    for mese in mesi:
        num_giorni = calendar.monthrange(2024, mesi.index(mese) + 1)[1]
        giorni_del_mese.extend(list(range(1, num_giorni + 1)))

    return product(giorni_settimana, giorni_del_mese, mesi, anni, ore, minuti, am_pm)


# Definizione del percorso del file Excel e del nome del foglio
percorso_file_excel = "/Users/ivan/Desktop/riepilogoprovvisorio.xlsx"
nome_foglio = "anydesk id + microsoft"

# Chiamata alla funzione per trovare la combinazione meno frequente
risultato, frequenza = trova_combinazione_meno_frequente(percorso_file_excel, nome_foglio)

# Stampa del risultato
if frequenza == 0:
    print("La combinazione meno frequente non esiste, generata una nuova combinazione casuale:", risultato)
else:
    print("La combinazione meno frequente è:", risultato, "con", frequenza, "occorrenze.")
