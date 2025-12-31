<< ! >func> somma(a, b)
    return a + b
</func>

<< ! >func> sottrai(a, b)
    return a - b
</func>

<< ! >func> moltiplica(a, b)
    return a * b
</func>

<< ! >func> dividi(a, b)
    if b == 0
        int << func >> ("Errore: Divisione per zero!")
        return 0
    return a / b
</func>

int << func >> ("=== CALCOLATRICE ===")
int << func >> ("10 + 5 = " + << func >> somma(10, 5))
int << func >> ("10 - 5 = " + << func >> sottrai(10, 5))
int << func >> ("10 * 5 = " + << func >> moltiplica(10, 5))
int << func >> ("10 / 5 = " + << func >> dividi(10, 5))
