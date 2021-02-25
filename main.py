from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models.testas import *

engine = create_engine('sqlite:///egzaminavimo_programa.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

# Sukuriame testą

# testas1 = Testas("Python testas")
# session.add(testas1)
# session.commit()

# Sukuriame klausimą

# testas1 = session.query(Testas).get(1)
#
# klausimas1 = Klausimas("Koks kintamasis skirtas sveikajam skaičiui saugoti?", 1)
# klausimas1.testas = testas1
# session.add(klausimas1)
# session.commit()

# Sukuriame klausimo atsakymus

# klausimas1 = session.query(Klausimas).get(1)
#
# atsakymas1 = Atsakymas("Float", False)
# atsakymas1.klausimas = klausimas1
# atsakymas2 = Atsakymas("Integer", True)
# atsakymas2.klausimas = klausimas1
# atsakymas3 = Atsakymas("Boolean", False)
# atsakymas3.klausimas = klausimas1
#
# session.add(atsakymas1)
# session.add(atsakymas2)
# session.add(atsakymas3)
# session.commit()

# # Sukuriame vartotoją
#
# vartotojas1 = Vartotojas("Donatas", "Noreika")
# session.add(vartotojas1)
# session.commit()

# Sukuriame sprendimą

# vartotojas1 = session.query(Vartotojas).get(1)
# testas1 = session.query(Testas).get(1)
#
# sprendimas1 = Sprendimas()
# sprendimas1.vartotojas = vartotojas1
# sprendimas1.testas = testas1
#
# session.add(sprendimas1)
# session.commit()

# Sukuriame vartotojo atsakymus

sprendimas1 = session.query(Sprendimas).get(1)
klausimas1 = session.query(Klausimas).get(1)
atsakymas2 = session.query(Atsakymas).get(2)

vartotojo_atsakymas1 = VartotojoAtsakymas()
vartotojo_atsakymas1.sprendimas = sprendimas1
vartotojo_atsakymas1.klausimas = klausimas1
vartotojo_atsakymas1.atsakymas = atsakymas2

atsakymas3 = session.query(Atsakymas).get(3)

vartotojo_atsakymas2 = VartotojoAtsakymas()
vartotojo_atsakymas2.sprendimas = sprendimas1
vartotojo_atsakymas2.klausimas = klausimas1
vartotojo_atsakymas2.atsakymas = atsakymas3
session.add(vartotojo_atsakymas1)
session.add(vartotojo_atsakymas2)
session.commit()



