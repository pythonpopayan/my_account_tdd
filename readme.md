# tdd

## setup environment

1. clone this repository, dependencies are on `requirements.txt`
2. create a `secrets.yaml` file located on `dj_myaccount/` folder as shown on [docs/secrets.example](docs/secrets.example)
3. create an `initial_data.yaml` file located on `setup/` folder as shown on [docs/initial_data.example](docs/initial_data.example)
4. once you run migrations, run in manage.py shell script `setup/initial_superuser.py` to create admin account and initial settings
5. once you're finished, make a pull request on github repository


## goal

- create an django app for notifications, this app must notify in an sticky bar or by email, this django app should be portable to other projects (dependency inversion)
- create a settings window where user can:
    - change its own name
    - change its own password
    - set email for notifications
    - configure if want to activate email or app notifications


## nice-to-have

- the modal with id `die_glucke` in `templates/detail.html` is shown properly only for phone screens, would be nice to fix it for desktop screens
- deploy the app on heroku

## criteria

- redability counts, pip8 on python code and consistent JavaScript styling, docstrings counts
- the most ready-to-plug, the best
- the most safety-design oriented, the best (safety for user and for server app excecution)
