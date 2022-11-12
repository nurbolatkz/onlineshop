# onlineshop


Clone repository

```bash
https://github.com/nurbolatkz/onlineshop.git
```



Add `.env` file for environment variables

```bash
touch .env
```

Copy `.env.dist` content to `.env` file

```bash
cat .env.dist > .env
```

Write your database credentials to `.env` file

Create virtual environment

```bash
virtualenv venv
```

Activate virtual environment

```bash
source venv/bin/activate/
```

Install dependencies
```
pip3 install -r requirements.txt
```

Migrate database

```bash
python3 manage.py migrate
```

Run server
