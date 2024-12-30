from cryptography.fernet import Fernet
import hashlib
import base64

# Tu contraseña sencilla
password = "1234"

# Convertir la contraseña en una clave válida (32 bytes) usando SHA-256
key = hashlib.sha256(password.encode()).digest()
key = base64.urlsafe_b64encode(key[:32])  # Fernet necesita base64 y exactamente 32 bytes

print(key)

# Crear un objeto Fernet con la clave
cipher = Fernet(key)

# Leer el archivo de texto
with open("archivo.txt", "rb") as file:
    data = file.read()

# Encriptar el contenido del archivo
encrypted_data = cipher.encrypt(data)
with open("archivo_encriptado.txt", "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)
print("Archivo encriptado guardado como 'archivo_encriptado.txt'.")
