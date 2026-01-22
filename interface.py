"""
Interface inicial do Programa, onde o usuário escolhe o que deseja fazer.
"""

import os
import random
import logica   
import savefile

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def ler_data_usuario():
    while True:
        try:
            entrada = input("Digite uma data (dd/mm/aaaa): ")
            partes = entrada.split('/')
            if len(partes) != 3: raise ValueError
            return int(partes[0]), int(partes[1]), int(partes[2])
        except:
            print("⚠️ Formato inválido! Use dd/mm/aaaa")

def exibir_ranking():
    limpar_tela()
    print("=== 🏆 HALL DA FAMA ===")
    ranking = savefile.buscar_top_scores()
    
    if not ranking:
        print("Nenhum recorde salvo ainda.")
    else:
        for i, (nome, pontos) in enumerate(ranking, 1):
            print(f"{i}º. {nome} - {pontos} pontos")
            
    input("\nEnter para voltar...")

def modo_calculadora():
    limpar_tela()
    print("=== 🧮 CALCULADORA ===")
    d, m, a = ler_data_usuario()
    
    res = logica.descobrir_dia_semana(d, m, a)
    nome = logica.NOMES_DIAS[res]
    
    print(f"\n📅 {d}/{m}/{a} é: {nome.upper()}")
    input("\nEnter para voltar...")

def modo_jogo():
    limpar_tela()
    print("=== 🎮 SOBREVIVÊNCIA ===")
    pontos = 0
    
    while True:
        # Gera data aleatória
        ano = random.randint(1900, 2100)
        mes = random.randint(1, 12)
        # Define dias máximos do mês (lógica simplificada para interface)
        max_d = 31
        if mes == 2: max_d = 29 if logica.eh_bissexto(ano) else 28
        elif mes in [4,6,9,11]: max_d = 30
        
        dia = random.randint(1, max_d)
        
        # Pergunta
        print(f"\nData: {dia}/{mes}/{ano}")
        print("0-Dom 1-Seg 2-Ter 3-Qua 4-Qui 5-Sex 6-Sab")
        
        try:
            resp = int(input("Qual o dia (0-6)? "))
            gabarito = logica.descobrir_dia_semana(dia, mes, ano)
            
            if resp == gabarito:
                pontos += 1
                print(f"✅ Boa! (+1) Total: {pontos}")
            else:
                certa = logica.NOMES_DIAS[gabarito]
                print(f"\n❌ ERROU! Era {certa}.")
                break # Sai do loop
        except ValueError:
            print("Digite número!")

    # Game Over - Salvar Score
    print(f"\nFIM DE JOGO! Pontuação final: {pontos}")
    if pontos > 0:
        nome = input("Digite seu nome para o ranking: ")
        savefile.salvar_score(nome, pontos)
    
    input("Enter para sair...")

def iniciar():
    """Função principal que inicia o menu"""
    # Garante que o banco existe antes de começar
    savefile.inicializar_banco()
    
    while True:
        limpar_tela()
        print("=== DOOMSDAY TRAINER ===")
        print("1. Jogar")
        print("2. Calculadora")
        print("3. Ranking")
        print("0. Sair")
        
        op = input("\nOpção: ")
        
        if op == "1": modo_jogo()
        elif op == "2": modo_calculadora()
        elif op == "3": exibir_ranking()
        elif op == "0": break