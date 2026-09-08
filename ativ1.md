# Atividade 1 - Arquitetura de Banco de Dados e Endpoints Iniciais (Kairos)

### 1. Quais tabelas você definiu inicialmente?
Defini três tabelas principais para suportar a regra de negócio essencial:
* **`users`**: Armazena as informações dos usuários cadastrados (id, nome, e-mail, senha criptografada e data de criação).
* **`habits`**: Contém os hábitos criados (id, chave estrangeira do usuário, título, descrição, categoria, frequência e data de criação).
* **`habit_logs`**: Registra o histórico diário de realização de cada hábito (id, chave estrangeira do hábito, data do check-in e status de conclusão).

---

### 2. Você utilizou migrations? Se sim, quantas migrations? Descreva em uma frase o que cada uma faz.
Sim, utilizei apenas 1 migration inicial (`database/migrations/001_initial_tables.py`):
* **Migration 1 (`001_initial_tables.py`)**: Cria toda a estrutura relacional inicial contendo as tabelas `users`, `habits` e `habit_logs` com suas respectivas chaves estrangeiras e restrições.

---

### 3. Qual o caminho do arquivo que gera a seed do seu banco?
`database/seeds.py`

---

### 4. Quais os endpoints que você irá implementar inicialmente?
* `POST /auth/register` - Criação de conta de usuário.
* `POST /auth/login` - Autenticação e emissão de token de acesso (JWT).
* `GET /habits` - Listagem dos hábitos pertencentes ao usuário autenticado.
* `POST /habits` - Cadastro de um novo hábito.
* `POST /habits/{id}/check` - Marcação ou desmarcação do hábito para a data informada.

---

### 5. Você está usando algum framework para escrever os endpoints da sua API? Se sim, qual?
Sim. Utilizei o **FastAPI** sobre a linguagem **Python**. O framework foi escolhido pela alta produtividade, validação automática de dados via Pydantic e geração nativa de documentação interativa (Swagger/OpenAPI), o que acelera o teste e a integração com as aplicações cliente.
