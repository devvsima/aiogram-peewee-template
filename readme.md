
# 🚀 Getting Started

## 🛠️ Technologies Stack
- `aiogram 2`
- `peewee`
- `PostgreSQL \ Sqlite`

---

## 📥 How to Install?

### 1. Clone the Repository
First, clone the repository and navigate to its directory:

```bash
git clone https://github.com/devvsima/aiogram-peewee-template.git
cd tgbot
```

### 2. Setting up a virtual environment ".venv"

#### Linux
Install dependencies and activate the virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

#### Windows
Similar steps for Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

> 💡 Note: The name `.venv` can be changed to anything else you wish.

### 3. Setting environment variable

First, copy the `.env.dist` file and rename it to `.env`:

```bash
cp .env.dist .env
```

Then edit the environment variables file:

```bash
vim .env
# or
nano .env
```

### 4. Bot settings

#### `ADMINS` - Admin IDs
Add admin IDs, separating them with commas

```bash
# example
ADMINS=12345678,12345677,12345676
```

#### `TOKEN` - Bot token from [@BotFather](https://t.me/BotFather)
Add your bot token:

```bash
# example
BOT_TOKEN=123452345243:Asdfasdfasf
```

### 5. Configuring the PostgreSQL database

Set the database connection parameters:

- `DB_NAME` - название базы данных
- `DB_HOST` - хост базы данных (по умолчанию `'localhost'`)
- `DB_PORT` - порт базы данных (по умолчанию `5432`)
- `DB_USER` - пользователь с доступом к базе данных
- `DB_PASS` - пароль от базы данных

---

Now the bot is ready to run! 🎉