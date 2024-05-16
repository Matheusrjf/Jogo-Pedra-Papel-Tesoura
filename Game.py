import random

def jogar():
    escolhas = ['pedra', 'papel', 'tesoura']

    # Escolha do usuário
    escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()
    while escolha_usuario not in escolhas:
        escolha_usuario = input("Escolha inválida. Escolha pedra, papel ou tesoura: ").lower()

    # Escolha aleatória do computador
    escolha_computador = random.choice(escolhas)

    # Determinar o vencedor
    print(f"Você escolheu {escolha_usuario}. O computador escolheu {escolha_computador}.")
    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        print("Você venceu!")
    else:
        print("O computador venceu!")

# Loop principal do jogo
while True:
    jogar()
    continuar = input("Deseja jogar novamente? (s/n): ").lower()
    if continuar != 's':
        print("Obrigado por jogar!")
        break



