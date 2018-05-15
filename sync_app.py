import requests
from yaml import load

def login(login_url):
    with open('credentials.yaml', 'r') as f:
        text = f.read()
        data = load(text)
    s = requests.Session()
    response = s.get(login_url)

    return s

base_url = 'http://localhost:8000'
# log into account
session = login(base_url)
# get transaction resume
# delete transactions
# set new transaction
# logout
