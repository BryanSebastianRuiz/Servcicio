import base64  # ¡Importación necesaria!

# Texto original
flag_utf16 = "flag{welcome_to_ctf}"

# Codificar en UTF-16
encoded_flag_utf16 = flag_utf16.encode('utf-16')

# Codificar en base64
encoded_base64_utf16 = base64.b64encode(encoded_flag_utf16).decode()

# Guardarlo en un archivo
with open("ciber.txt", "w") as f:
    f.write(encoded_base64_utf16)

print("Archivo generado: ciber.txt")
