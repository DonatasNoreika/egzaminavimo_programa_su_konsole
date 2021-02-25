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




# while True:
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


# sprendimas1.testas = testas1
#
# session.add(sprendimas1)
# session.commit()


klausimai = session.query(Klausimas).filter_by(testas=pasirinktas_testas).all()
for klausimas in klausimai:
    print()
    print(klausimas.tekstas)
    for atsakymas in klausimas.atsakymai:
        print(klausimas.id, atsakymas.tekstas)
    input()
