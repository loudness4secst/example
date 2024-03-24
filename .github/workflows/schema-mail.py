class Dipendente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
ceo = Dipendente("CEO", "ceo@azienda.com")
amministrazione = Dipendente("Amministrazione", "amministrazione@azienda.com")
marketing = Dipendente("Marketing", "marketing@azienda.com")
vendite = Dipendente("Vendite", "vendite@azienda.com")
tecnico = Dipendente("Tecnico", "tecnico@azienda.com")
risorse_umane = Dipendente("Risorse Umane", "risorseumane@azienda.com")
dipendenti = [
    Dipendente("Dipendente 1", "dipendente1@azienda.com"),
    Dipendente("Dipendente 2", "dipendente2@azienda.com"),
    Dipendente("Dipendente 3", "dipendente3@azienda.com"),
    Dipendente("Dipendente 4", "dipendente4@azienda.com"),
    Dipendente("Dipendente 5", "dipendente5@azienda.com"),
    Dipendente("Dipendente 6", "dipendente6@azienda.com"),
    Dipendente("Dipendente 7", "dipendente7@azienda.com"),
    Dipendente("Dipendente 8", "dipendente8@azienda.com"),
    Dipendente("Dipendente 9", "dipendente9@azienda.com"),
    Dipendente("Dipendente 10", "dipendente10@azienda.com"),
    Dipendente("Dipendente 11", "dipendente11@azienda.com"),
    Dipendente("Dipendente 12", "dipendente12@azienda.com"),
    Dipendente("Dipendente 13", "dipendente13@azienda.com"),
    Dipendente("Dipendente 14", "dipendente14@azienda.com"),
    Dipendente("Dipendente 15", "dipendente15@azienda.com"),
    Dipendente("Dipendente 16", "dipendente16@azienda.com"),
    Dipendente("Dipendente 17", "dipendente17@azienda.com"),
    Dipendente("Dipendente 18", "dipendente18@azienda.com"),
    Dipendente("Dipendente 19", "dipendente19@azienda.com"),
    Dipendente("Dipendente 20", "dipendente20@azienda.com")
]
organigramma = {
    ceo: [amministrazione, marketing, vendite, tecnico, risorse_umane],
    amministrazione: dipendenti[:5],
    marketing: dipendenti[5:10],
    vendite: dipendenti[10:15],
    tecnico: dipendenti[15:],
    risorse_umane: []
}
def stampa_organigramma(manager, indentazione=""):
    print(f"{indentazione}{manager.nome} - {manager.email}")
    for dipendente in organigramma[manager]:
        stampa_organigramma(dipendente, indentazione + "\t")

stampa_organigramma(ceo)