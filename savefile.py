"""
Armazenamento com SQLite para registro dos scores dos usuários.
"""
import sqlite3

# Nome do arquivo do banco
DB_NAME = "doomsday_scores.db"

def inicializar_banco():
    """Cria a tabela se ela não existir"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Cria a tabela 'scores' com id, nome e pontos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            pontos INTEGER NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()

def salvar_score(nome, pontos):
    """Salva a pontuação de um jogador"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO scores (nome, pontos) VALUES (?, ?)", (nome, pontos))
    
    conn.commit()
    conn.close()
    print("💾 Pontuação salva com sucesso!")

def buscar_top_scores(limite=5):
    """Retorna os top X jogadores"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Busca ordenando por pontos (Do maior para o menor - DESC)
    cursor.execute("SELECT nome, pontos FROM scores ORDER BY pontos DESC LIMIT ?", (limite,))
    dados = cursor.fetchall()
    
    conn.close()
    return dados