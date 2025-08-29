# password_checker.py
def is_valid_password(password: str):
    """
    Gültiges Passwort erfüllt:
    - mind. 8 Zeichen
    - enthält Zahl
    - enthält Groß- und Kleinbuchstaben
    """
    if len(password) < 8:
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    return True
