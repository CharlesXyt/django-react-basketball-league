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
    python manage.py migrate
    python manage.py runserver
```

## Backend Setup

If the database is empty, then before starting the backend, it would require to run script to import fake data.
Below command will recreate games, coaches, players and league admin, and default password for users is 12345

```bash
    python manage.py migrate
    python create_fake_data.py
```
After successfully running the above command, there will be usernames in stdout like below
```
(venv) python create_fake_data.py
League Admin Username:benjamin36
Coach Username:scotthector_team_coach
Player Username:sue18
```
Above is the current valid users in sqlite database file, and all fake users' password is 12345.
