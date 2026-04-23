# MAI IMPORTARE MODULI/FUNZIONI CHE SI VOGLIONO TESTARE QUI, MA SOLO NEL FILE DI TEST
import pytest
import subprocess

def generatore(argomenti: list[str]):
    comando_base = ["python", "generatore.py"]
    comando_completo = comando_base + argomenti

    risultato = subprocess.run(comando_completo, capture_output=True, text=True)
    return risultato

def test_nessun_parmetro_ritorna_exit_code_1():
    risultato = generatore([])

    assert risultato.returncode == 1, f"Exit code errato: {risultato.returncode}"

    assert "Devi fornire un nome utente" in risultato.stderr
    assert risultato.stdout==""

def test_utente_admin_ritorna_exit_code_2():
    risultato = generatore(["admin"])

    assert risultato.returncode == 2
    assert "Non puoi" in risultato.stderr
    assert risultato.stdout==""

def test_utente_valido_ritorna_exit_code_0():
    risultato = generatore(["stefano"])

    assert risultato.returncode == 0
    assert "Token di accesso generato" in risultato.stdout
    assert "STEFANO" in risultato.stdout
    assert risultato.stderr==""