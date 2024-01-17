# Project Name

Matific Assignment

## Node.js Requirement

This project requires Node.js to be installed. and it specifically requires a version greater than v20.11.0 Download and install it from [nodejs.org](https://nodejs.org/).

## Python Requirement

This project requires Python to be installed, and it specifically requires a version greater than 3.10. Download and install Python from [python.org](https://www.python.org/).

## Frontend installation and start

```bash
    cd react-basketball-league
    npm install
    npm run dev
```

## Backend installation and start

```bash
    python3.10 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    cd basketball-league
    python manage.py runserver
```

## Backend Setup Before Running

Before starting the backend, it would require run script to import fake data.
Below command will import games, coaches, players and league admin.

```bash
    python create_fake_data.py
```
Here is the league admin information which can be used to login app in frontend.

league admin: 
    username: league_admin
    password: 12345

