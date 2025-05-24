import csv
from typing import List, Dict


def ucitaj_csv(putanja_datoteke: str) -> List[Dict]:
    """
    Učitava CSV datoteku i vraća listu rječnika gdje svaki rječnik predstavlja jedan red

    Args:
        putanja_datoteke (str): Put do CSV datoteke

    Returns:
        List[Dict]: Lista rječnika s podacima iz CSV-a
    """
    try:
        with open(putanja_datoteke, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            return list(csv_reader)
    except FileNotFoundError:
        print(f"Greška: Datoteka '{putanja_datoteke}' nije pronađena.")
        return []
    except Exception as e:
        print(f"Greška pri učitavanju CSV datoteke: {str(e)}")
        return []


def spremi_u_csv(podaci: List[Dict], putanja_datoteke: str, stupci: List[str] = None) -> bool:
    """
    Sprema listu rječnika u CSV datoteku

    Args:
        podaci (List[Dict]): Lista rječnika za spremanje
        putanja_datoteke (str): Put gdje će se spremiti CSV datoteka
        stupci (List[str], optional): Lista imena stupaca. Ako nije zadano, koriste se ključevi prvog rječnika

    Returns:
        bool: True ako je spremanje uspješno, False ako nije
    """
    try:
        if not podaci:
            print("Nema podataka za spremanje.")
            return False

        # Ako stupci nisu specificirani, uzmi ključeve iz prvog rječnika
        if stupci is None:
            stupci = list(podaci[0].keys())

        with open(putanja_datoteke, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=stupci)
            writer.writeheader()  # Zapiši zaglavlje
            writer.writerows(podaci)  # Zapiši sve redove
        return True

    except Exception as e:
        print(f"Greška pri spremanju u CSV: {str(e)}")
        return False


def filtriraj_podatke(podaci: List[Dict], uvjet: callable) -> List[Dict]:
    """
    Filtrira podatke prema zadanom uvjetu

    Args:
        podaci (List[Dict]): Lista rječnika za filtriranje
        uvjet (callable): Funkcija koja prima rječnik i vraća True/False

    Returns:
        List[Dict]: Filtrirana lista rječnika
    """
    return list(filter(uvjet, podaci))