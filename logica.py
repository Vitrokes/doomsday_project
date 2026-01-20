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
    # Pega só o século (Ex: 1997 -> 19)
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
    # TODO: Implementar a lógica aqui
    pass

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
    # TODO: Implementar a lógica aqui
    pass