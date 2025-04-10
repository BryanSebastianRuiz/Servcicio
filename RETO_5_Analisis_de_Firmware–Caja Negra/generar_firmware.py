import random

with open("firmware_dump_simple.bin", "wb") as f:
    # Relleno inicial
    f.write(bytes([random.randint(0, 255) for _ in range(1024)]))

    # Simulación de estructura de archivos
    f.write(b"/boot/init\n")
    f.write(b"/usr/config\n")
    f.write(b"/secret/files/config.sys\n")

    # Falsa flag para despistar
    f.write(b"flag{this_is_a_decoy}\n")

    # Relleno intermedio
    f.write(bytes([random.randint(0, 255) for _ in range(2048)]))

    # Flag real bien ubicada pero sin ofuscar
    f.write(b"### CONFIG FILE START ###\n")
    f.write(b"# Usuario: admin\n")
    f.write(b"# Permisos: root\n")
    f.write(b"Flag encontrada: flag{firmware_easy_but_hidden}\n")
    f.write(b"### CONFIG FILE END ###\n")

    # Padding final
    f.write(bytes([0] * 512))
