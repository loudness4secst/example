import pandas as pd
from itertools import product

def trova_combinazione_meno_frequente():
    # Leggi solo le colonne specifiche dal file Excel
    colonne = ["O", "P", "Q", "R", "S", "T", "U"]
    dati_excel = pd.read_excel("/Users/ivan/Desktop/riepilogoprovvisorio.xlsx", usecols=colonne)
    # Genera tutte le possibili combinazioni di data e ora
    giorni_settimana = ["lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"]
    mesi = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]
    ore = list(range(1, 13))
    minuti = list(range(0, 60))
    am_pm = ["am", "pm"]

    combinazioni = product(giorni_settimana, range(1, 32), mesi, [2024], ore, minuti, am_pm)
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

    combinazione_meno_frequente = min(conteggio_combinazioni, key=conteggio_combinazioni.get)
    return combinazione_meno_frequente, conteggio_combinazioni[combinazione_meno_frequente]

risultato, frequenza = trova_combinazione_meno_frequente()
if frequenza == 0:
    print("La combinazione meno frequente non esiste affatto.")
else:
    print("La combinazione meno frequente è:", risultato, "con", frequenza, "occorrenze.")
