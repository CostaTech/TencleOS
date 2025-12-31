int << func >> ("=== INDOVINA IL NUMERO ===")
int numero_segreto = 42
int tentativi = 0
int indovinato = 0

<<While>>! <on> indovinato == 0
    int tentativo = << func >> input("Indovina il numero (1-100): ")
    tentativi = tentativi + 1
    
    if tentativo == numero_segreto
        int << func >> ("BRAVO! Hai indovinato in " + tentativi + " tentativi!")
        indovinato = 1
    elif tentativo < numero_segreto
        int << func >> ("Troppo basso! Riprova.")
    else
        int << func >> ("Troppo alto! Riprova.")
