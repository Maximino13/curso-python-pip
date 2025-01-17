import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0

rounds = 1
print("""[🤖 Bienvenido al juego Piedra, Papel o tijera 🙋]
              >>> Ingresa una opción <<<""")
while True:
    #Bienvenida
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    #Marcador
    print(
        f"""[_MARCADOR_     Usuario: {user_wins}        Maquina: {computer_wins} ]
      """)
    #Elección del usuario
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()

    rounds += 1
    #Validación de respuesta
    if not user_option in options:
        print('esa opcion no es valida\n')
        continue
    #Elección de la computadora
    computer_option = random.choice(options)
    #Impresión de elecciones
    print('Opción del usuario:', user_option)
    print('Opción de la maquina:', computer_option)
    #Logica del juego
    if user_option == computer_option:
        print('\nEmpate!\n')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('\n piedra gana a tijera')
            print('El usuario gano!\n')
            user_wins += 1
        else:
            print('\nPapel gana a piedra')
            print('La computadora gano!\n')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('\npapel gana a piedra')
            print('El usuario gano!\n')
            user_wins += 1
        else:
            print('\ntijera gana a papel')
            print('La computadora gano!\n')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('\ntijera gana a papel')
            print('El usuario gano!\n')
            user_wins += 1
        else:
            print('\npiedra gana a tijera')
            print('La computadora gano!\n')
            computer_wins += 1
    #Validación de victorias
    if computer_wins == 2:
        print('El ganador es la computadora')
        break
    if user_wins == 2:
        print('El ganador es el usuario')
        break
