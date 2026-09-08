
"""
Script de Seed - Dados Iniciais para o Kairos
Arquivo: database/seeds.py
"""
import sqlite3
from datetime import date

DB_PATH = "kairos.db"


def run_seeds():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("Inserindo dados iniciais (seeds)...")

    # 1. Usuário de teste inicial
    cursor.execute("""
        INSERT OR IGNORE INTO users (id, name, email, password_hash)
        VALUES (1, 'Usuário Teste', 'demo@kairos.app', 'hash_senha_teste_123')
    """)

    # 2. Hábitos de exemplo
    habits = [
        (1, 1, 'Leitura Espiritual', 'Ler 15 minutos por dia', 'Espiritualidade', 'daily'),
        (2, 1, 'Beber 2L de água', 'Manter garrafa cheia durante o dia', 'Saúde', 'daily'),
        (3, 1, 'Exercício Físico', '30 minutos de caminhada ou treino', 'Saúde', 'daily')
    ]
    
    cursor.executemany("""
        INSERT OR IGNORE INTO habits (id, user_id, title, description, category, frequency)
        VALUES (?, ?, ?, ?, ?, ?)
    """, habits)

    # 3. Registro de check-in de exemplo para o dia de hoje
    cursor.execute("""
        INSERT OR IGNORE INTO habit_logs (habit_id, completed_at, status)
        VALUES (1, ?, 1)
    """, (date.today().isoformat(),))

    conn.commit()
    conn.close()
    print("Seeds inseridas com sucesso!")


if __name__ == "__main__":
    run_seeds()
