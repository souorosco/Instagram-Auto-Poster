username = input('Enter your username: \n')
password = input('Enter your password: \n')
totp_secret = input('Enter your F2A auth key (base32): \n')

config_file = open('config.py', 'w')
config_file.write(
f'''USERNAME = \'{username}\'
PASSWORD = \'{password}\'
AUTH_KEY = \'{totp_secret}\''''
)