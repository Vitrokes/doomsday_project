"""
Módulo responsável pela lógica matemática do Algoritmo do Juízo Final (Doomsday).
Aqui ficam apenas as funções utilizadas para o funcionamento do algoritmo.
"""

#Se você tem o NÚMERO e quer o NOME
NOMES_DIAS = [
    "Domingo",        # Índice 0
    "Segunda-feira",  # Índice 1
    "Terça-feira",    # Índice 2
    "Quarta-feira",   # Índice 3
    "Quinta-feira",   # Índice 4
    "Sexta-feira",    # Índice 5
    "Sábado"          # Índice 6
]

#Se você tem o NOME e quer o NÚMERO
MAPA_DIAS = {
    "domingo": 0,
    "segunda": 1,
    "terça": 2,
    "quarta": 3,
    "quinta": 4,
    "sexta": 5,
    "sábado": 6
}

def eh_bissexto(ano: int) -> bool:
    """
    Verifica se um ano é bissexto.
    Regra: Divisível por 4. Se terminar em 00, deve ser divisível por 400.
    Retorna: True se for bissexto, False caso contrário.
    """
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

def get_ancora_secular(ano):
    # Pega o século de referência (Ex: 1997 -> 19)
    seculo = ano // 100 
    
    # Calcula o resto da divisão por 4
    resto = seculo % 4
    
    # Mapeamento direto (Regra 2-0-5-3)
    # 0 (Ex: 1600, 2000) -> Terça (2)
    # 1 (Ex: 1700, 2100) -> Domingo (0)
    # 2 (Ex: 1800, 2200) -> Sexta (5)
    # 3 (Ex: 1900, 2300) -> Quarta (3)
    tabela_secular = {
        0: 2,
        1: 0,
        2: 5,
        3: 3
    }
    
    return tabela_secular[resto]

def calcular_doomsday_ano(ano):
    """
    Calcula o dia da semana do "Doomsday" para um ano específico.
    Fórmula base: (DiaAncora + Ano + Ano//4) % 7
    
    Retorna: Um número representando o dia da semana.
    """
    # 1. Pega a âncora do século (Ex: 2024 -> ancora de 2000 é Terça/2)
    ancora = get_ancora_secular(ano)
    
    # 2. Pega só os dois últimos dígitos (Ex: 2024 -> 24)
    ultimos_dois = ano % 100
    
    # 3. Aplica a fórmula: (Âncora + Ano + Anos Bissextos)
    # Obs: ultimos_dois // 4 é a divisão inteira (quantos bissextos tiveram)
    soma = ancora + ultimos_dois + (ultimos_dois // 4)
    
    # 4. Retorna o resto da divisão por 7
    return soma % 7

def descobrir_dia_semana(dia, mes, ano):
    """
    Função principal. Recebe uma data completa e retorna o dia da semana.
    
    Passos:
    1. Descobrir o Doomsday do ano.
    2. Identificar a data âncora do mês (cuidado com bissextos em Jan/Fev).
    3. Calcular a distância entre o dia informado e a âncora do mês.
    4. Somar e tirar o módulo 7.
    
    Retorna: Uma string (ex: "Sexta-feira") ou um inteiro.
    """
    # 1. Descobre qual é o dia da semana base daquele ano
    doomsday_ano = calcular_doomsday_ano(ano)
    
    # 2. Define as âncoras de cada mês (Mês 1 a 12)
    # Índices: 0 é dummy (vazio), 1 é Jan, 2 é Fev, etc...
    ancoras_meses = [
        None, 
        3,  # Jan (3 em ano comum)
        28, # Fev (28 em ano comum)
        14, # Mar (Pi Day - 14/03)
        4,  # Abr (04/04)
        9,  # Mai (09/05)
        6,  # Jun (06/06)
        11, # Jul (11/07)
        8,  # Ago (08/08)
        5,  # Set (05/09)
        10, # Out (10/10)
        7,  # Nov (07/11)
        12  # Dez (12/12)
    ]
    
    # 3. Ajuste para Ano Bissexto (Só afeta Jan e Fev)
    if eh_bissexto(ano):
        ancoras_meses[1] = 4  # Janeiro vira dia 4
        ancoras_meses[2] = 29 # Fevereiro vira dia 29
        
    # 4. Pega a âncora do mês solicitado
    dia_ancora = ancoras_meses[mes]
    
    # 5. Calcula a diferença (delta)
    # Ex: Quero dia 20, a âncora é 10. Diferença = 10 dias.
    diferenca = dia - dia_ancora
    
    # 6. Soma ao Doomsday do ano e tira o módulo 7
    # (O Python lida bem com números negativos no módulo, ex: -2 % 7 vira 5)
    dia_final = (doomsday_ano + diferenca) % 7
    
    return dia_final # Retorna 0 a 6

# Bloco de teste rápido (só roda se você executar esse arquivo diretamente)
if __name__ == "__main__":
    print("--- Teste de Lógica ---")
    
    # Teste 1: Data de hoje (assumindo que seja 2026 no seu contexto, ou use atual)
    # Vamos testar o exemplo clássico: 11 de Setembro de 2001 (Terça-feira)
    d = 11
    m = 9
    a = 2001
    resultado = descobrir_dia_semana(d, m, a)
    nome = NOMES_DIAS[resultado]
    
    print(f"Data: {d}/{m}/{a}")
    print(f"Resultado Numérico: {resultado}")
    print(f"Resultado Nome: {nome}")
    
    if nome == "Terça-feira":
        print("✅ SUCESSO! O algoritmo funcionou.")
    else:
        print("❌ ERRO! Algo deu errado.")