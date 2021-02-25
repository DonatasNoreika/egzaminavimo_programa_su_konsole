from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.testas import *

engine = create_engine('sqlite:///egzaminavimo_programa.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

# while True:
testai = session.query(Testas).all()
for testas in testai:
    print(testas.id, testas.pavadinimas)
pasirinkto_testo_id = int(input("Pasirinkite testą"))
pasirinktas_testas = session.query(Testas).get(pasirinkto_testo_id)
print("Testas", pasirinktas_testas.pavadinimas)

klausimai = session.query(Klausimas).filter_by(testas=pasirinktas_testas).all()
for klausimas in klausimai:
    print()
    print(klausimas.tekstas)
    for atsakymas in klausimas.atsakymai:
        print(klausimas.id, atsakymas.tekstas)
    input()
