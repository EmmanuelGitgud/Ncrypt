from secrets import token_hex
from cryptography.fernet import Fernet

token = Fernet.generate_key()

with open('Ncrypt.key','wb') as key:
    key.write(token)
