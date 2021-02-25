from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///egzaminavimo_programa.db')
Base = declarative_base()

class Testas(Base):
    __tablename__ = "testas"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("Pavadinimas", String)

    def __init__(self, pavadinimas):
        self.pavadinimas = pavadinimas

class Klausimas(Base):
    __tablename__ = "klausimas"
    id = Column(Integer, primary_key=True)
    tekstas = Column("Tekstas", String)
    balas = Column("Balas", Integer)
    testas_id = Column(Integer, ForeignKey('testas.id'))
    testas = relationship("Testas")

    def __init__(self, tekstas, balas):
        self.tekstas = tekstas
        self.balas = balas

class Atsakymas(Base):
    __tablename__ = "atsakymas"
    id = Column(Integer, primary_key=True)
    tekstas = Column("Tekstas", String)
    ar_teisingas = Column("Ar teisingas", Boolean)
    klausimas_id = Column(Integer, ForeignKey('klausimas.id'))
    klausimas = relationship("Klausimas")

    def __init__(self, tekstas, ar_teisingas):
        self.tekstas = tekstas
        self.ar_teisingas = ar_teisingas

class Vartotojas(Base):
    __tablename__ = "vartotojas"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)

    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde


class Sprendimas(Base):
    __tablename__ = "sprendimas"
    id = Column(Integer, primary_key=True)
    # data = Column("Data", DateTime, default=datetime.today())
    vartotojas_id = Column(Integer, ForeignKey('vartotojas.id'))
    vartotojas = relationship("Vartotojas")
    testas_id = Column(Integer, ForeignKey('testas.id'))
    testas = relationship("Testas")

    # Reikia datos dar

class VartotojoAtsakymas(Base):
    __tablename__ = "vartotojo_atsakymas"
    id = Column(Integer, primary_key=True)
    sprendimas_id = Column(Integer, ForeignKey('sprendimas.id'))
    sprendimas = relationship(Sprendimas)
    klausimas_id = Column(Integer, ForeignKey('klausimas.id'))
    klausimas = relationship("Klausimas")
    atsakymas_id = Column(Integer, ForeignKey('atsakymas.id'))
    atsakymas = relationship("Atsakymas")

Base.metadata.create_all(engine)
