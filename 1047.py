Hinicial, Minicial, Hfinal, Mfinal = map(int, input().split())

if Hinicial == Hfinal:

    if Minicial == Mfinal:
        print(f'O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
    
    elif Minicial > Mfinal:
        print(f'O JOGO DUROU 24 HORA(S) E {(Minicial - Mfinal)} MINUTO(S)')

    elif Minicial < Mfinal:
        print(f'O JOGO DUROU 24 HORA(S) E {(Minicial - Mfinal)} MINUTO(S)')

elif Minicial > Hfinal:

    if Minicial == Mfinal:
        print(f'O JOGO DUROU {24 - Hinicial - Hfinal} HORA(S) E 0 MINUTO(S)')

    elif Minicial > Mfinal:
        print(f'O JOGO DUROU {24 - (Minicial - Mfinal)} HORA(S) E {60 - (Minicial - Mfinal)} MINUTO(S)')

    elif Minicial < Mfinal:
        print(f'O JOGO DUROU {24 - (Minicial - Mfinal)} HORA(S) E {60 - (Minicial - Mfinal)} MINUTO(S)')

elif Minicial < Hfinal:

    if Minicial == Mfinal:
        print(f'O JOGO DUROU {(Hinicial - Hfinal)} HORA(S) E 0 MINUTO(S)')

    elif Minicial > Mfinal:
        print(f'O JOGO DUROU {Hinicial - Hfinal - 1} HORA(S) E {60 - (Minicial - Mfinal)} MINUTO(S)')

    elif Minicial < Mfinal:
        print(f'O JOGO DUROU {Mfinal - Minicial} HORA(S) E {(Minicial - Mfinal)} MINUTO(S)')