from cryptography.fernet import Fernet
import hashlib
import base64

password = input("Ingrese contraseña: ")

# Convertir la contraseña en una clave válida (32 bytes) usando SHA-256
key = hashlib.sha256(password.encode()).digest()
key = base64.urlsafe_b64encode(key[:32])  # Fernet necesita base64 y exactamente 32 bytes

print(key)

# Crear un objeto Fernet con la clave
cipher = Fernet(key)


# Desencriptar el archivo (necesitas la clave)
with open("archivo_encriptado.txt", "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

decrypted_data = cipher.decrypt(encrypted_data)
with open("archivo_desencriptado.txt", "wb") as decrypted_file:
    decrypted_file.write(decrypted_data)
print("Archivo desencriptado guardado como 'archivo_desencriptado.txt'.")
