import sys

def main():
    if len(sys.argv) < 2:
        #scriviamo su stderr per indicare un errore
        sys.stderr.write("Errore CRITICO: Devi fornire un nome utente\n")
        sys.exit(1) # il programma muore comunicando Errore 1 al sistema operativo

    nome_utente = sys.argv[1]

    if nome_utente. lower() == "admin" or nome_utente. lower() == "root":
        sys.stderr.write("VIOLAZIONE: Non puoi usare 'admin'/'root' come nome utente\n")
        sys.exit(2)# il programma muore comunicando Errore 2 al sistema operativo

# stiamo codificando gli errori assegnandolgi un  umero es. sys.exit(1) per errore 1, sys.exit(2) per errore 2, ecc. 
# Questo è utile per identificare rapidamente il tipo di errore quando si esegue il programma da riga di comando o in uno script.

    print(f"[{nome_utente.upper()}] - Token di accesso generato: 987654321")
    sys.exit(0) 
    
    # il programma muore comunicando Errore 0 al sistema operativo, cioè tutto è andato bene

if __name__ == "__main__":
    main()
