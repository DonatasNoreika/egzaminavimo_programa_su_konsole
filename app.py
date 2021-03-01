from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.testas import *

engine = create_engine('sqlite:///egzaminavimo_programa.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

while True:
    vartotojai = session.query(Vartotojas).all()
    for vartotojas in vartotojai:
        print(vartotojas.id, vartotojas.vardas, vartotojas.pavarde)
    pasirinkto_vartotojo_id = int(input("Pasirinkite vartotoją arba sukurkite (0)"))
    if pasirinkto_vartotojo_id == 0:
        vardas = input("Įveskite vardą")
        pavarde = input("Įveskite pavardę")
        vartotojas = Vartotojas(vardas, pavarde)
        session.add(vartotojas)
        session.commit()
    else:
        aktyvus_vartotojas = session.query(Vartotojas).get(pasirinkto_vartotojo_id)
        break

testai = session.query(Testas).all()
for testas in testai:
    print(testas.id, testas.pavadinimas)
pasirinkto_testo_id = int(input("Pasirinkite testą"))
pasirinktas_testas = session.query(Testas).get(pasirinkto_testo_id)


sprendimas1 = Sprendimas()
sprendimas1.vartotojas = aktyvus_vartotojas
sprendimas1.testas = pasirinktas_testas
session.add(sprendimas1)
session.commit()

klausimai = session.query(Klausimas).filter_by(testas=pasirinktas_testas).all()

klausimu_kiekis = 0
taskai = 0
for klausimas in klausimai:
    print()
    print(klausimas.tekstas)
    for atsakymas in klausimas.atsakymai:
        print(atsakymas.id, atsakymas.tekstas)
    pasirinkto_atsakymo_id = int(input("Pasirinkite atsakymą"))
    pasirinktas_atsakymas = session.query(Atsakymas).get(pasirinkto_atsakymo_id)
    vartotojo_ats1 = VartotojoAtsakymas()
    vartotojo_ats1.sprendimas = sprendimas1
    vartotojo_ats1.klausimas = klausimas
    vartotojo_ats1.atsakymas = pasirinktas_atsakymas
    klausimu_kiekis += 1
    if pasirinktas_atsakymas.ar_teisingas:
        taskai += 1
    session.add(vartotojo_ats1)
    session.commit()
rezultatas = f"{taskai}/{klausimu_kiekis}"
sprendimas1.rezultatas = taskai
print("Rezultatas:", rezultatas)
