from django.core.management.utils import get_random_secret_key

secret = get_random_secret_key()

#get db database info into variables from input
db_name = input("Nombre Base de datos: ")
db_user = input("Usuario de base de datos: ")
db_password = input("Contrasena base de datos: ")


# Write the secret key to a file .env
with open('.env', 'w') as f:
    f.write(f"DJANGO_SECRET={secret}")
    f.write(f"\nDJANGO_DB={db_name}")
    f.write(f"\nDJANGO_USER={db_user}")
    f.write(f"\nDJANGO_PASS={db_password}")