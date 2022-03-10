from models.testas import (engine,
                           sessionmaker,
                           Testas,
                           Klausimas,
                           Atsakymas,
                           Vartotojas,
                           Sprendimas,
                           VartotojoAtsakymas)

Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = int(input("Pasirikite:\n1 - Sukurti testą\n2 - Prisijungti\n"))
    if pasirinkimas == 1:
        testo_pavadinimas = input("Įveskite testo pavadinimą")
        testas = Testas(testo_pavadinimas)
        session.add(testas)
        session.commit()

        while True:
            print("Norėdami nutraukti klausimų įvedimą spauskite ENTER")
            klausimo_tekstas = input("Įveskite klausimo tekstą")
            if klausimo_tekstas == "":
                break
            klausimo_balas = input("Įveskite klausimo balą")
            klausimas = Klausimas(klausimo_tekstas, klausimo_balas, testas)
            session.add(klausimas)
            session.commit()
            while True:
                print("Norėdami nutraukį atsakymų įvedimą spauskite ENTER")
                atsakymo_tekstas = input("Įveskite atsakymo tekstą")
                if atsakymo_tekstas == "":
                    break
                atsakymo_teisingas = input("Ar šis atsakymas teisingas (taip/ne)")
                if atsakymo_teisingas == "taip":
                    ar_teisingas = True
                else:
                    ar_teisingas = False
                atsakymas = Atsakymas(atsakymo_tekstas, ar_teisingas)
                klausimas.atsakymai.append(atsakymas)
                session.commit()

    if pasirinkimas == 2:
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

        pasirinkimas2 = int(input("Pasirikite:\n1 - Spręsti testą\n2 - Peržiūrėti sprendimus\n"))
        if pasirinkimas2 == 1:
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
            session.commit()
            print("Rezultatas:", rezultatas)
        if pasirinkimas2 == 2:
            sprendimai = session.query(Sprendimas).filter_by(vartotojas=aktyvus_vartotojas).all()
            for sprendimas in sprendimai:
                print(sprendimas)
