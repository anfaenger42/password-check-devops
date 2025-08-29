# password_checker.py
import string

def is_valid_password(password):
    """
    Gültiges Passwort erfüllt:
    - mind. 8 Zeichen
    - enthält Zahl
    - enthält Groß- und Kleinbuchstaben
    - enthält Sonderzeichen
    """
    if len(password) < 8:
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c in string.punctuation for c in password):
        return False
    return True
