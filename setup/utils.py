from yaml import load

def load_secrets(secrets_filename):
    """
    load secrets in a dictionary
    """
    with open(secrets_filename, 'r') as f:
        raw_text = f.read()
        secrets = load(raw_text)
    return secrets
