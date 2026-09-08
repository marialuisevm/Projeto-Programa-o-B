"""
Migration inicial - Criação das tabelas base do Kairos
Arquivo: database/migrations/001_initial_tables.py
"""
from alembic import op
import sqlalchemy as sa

# Identificadores da migration
revision = '001_initial_tables'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # 1. Tabela de Usuários
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('email', sa.String(length=150), nullable=False, unique=True),
        sa.Column('password_hash', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now())
    )

    # 2. Tabela de Hábitos (vinculada ao Usuário)
    op.create_table(
        'habits',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('title', sa.String(length=100), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('category', sa.String(length=50), nullable=True),
        sa.Column('frequency', sa.String(length=50), server_default='daily'),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now())
    )

    # 3. Tabela de Histórico/Check-in diário (vinculada ao Hábito)
    op.create_table(
        'habit_logs',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('habit_id', sa.Integer(), sa.ForeignKey('habits.id', ondelete='CASCADE'), nullable=False),
        sa.Column('completed_at', sa.Date(), nullable=False),
        sa.Column('status', sa.Boolean(), default=True)
    )


def downgrade() -> None:
    # Caso precise reverter a migration, apaga na ordem inversa
    op.drop_table('habit_logs')
    op.drop_table('habits')
    op.drop_table('users')
