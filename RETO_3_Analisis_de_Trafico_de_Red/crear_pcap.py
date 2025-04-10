from scapy.all import *

# Crear los paquetes Ethernet, IP y TCP
ether = Ether()
ip = IP(dst="192.168.1.1", src="192.168.1.100")
tcp = TCP(dport=80, sport=12345, flags="PA", seq=1, ack=1)

# Dividir la flag en fragmentos pequeños
http_payload_part1 = b"GET /flag?data=flag{tr4f1c_"  # Fragmento 1 de la bandera real
http_payload_part2 = b"det3ct} HTTP/1.1\r\n"  # Fragmento 2 de la bandera real (oculta más)
http_payload_part3 = b"Host: example.com\r\n"  # Cabecera HTTP que no tiene información de la flag
http_payload_part4 = b"Connection: keep-alive\r\n"  # Otra cabecera HTTP para hacer más completa la conversación
http_payload_part5 = b"User-Agent: Mozilla/5.0\r\n\r\n"  # Otra cabecera HTTP, fragmentación

# Fragmentos para la bandera
http_payload_f1_part1 = b"GET /flag?data=flag{incorrect_"  # Fragmento 1 de la falsa flag 1
http_payload_f1_part2 = b"flag_1234} HTTP/1.1\r\n"  # Fragmento 2 de la falsa flag 1

http_payload_f3_part1 = b"GET /flag?data=flag{fake_"  # Fragmento 1 de la falsa flag 3
http_payload_f3_part2 = b"flag_9876} HTTP/1.1\r\n"  # Fragmento 2 de la falsa flag 3

http_payload_f5_part1 = b"GET /flag?data=flag{no_"  # Fragmento 1 de la falsa flag 5
http_payload_f5_part2 = b"flag_here_4321} HTTP/1.1\r\n"  # Fragmento 2 de la falsa flag 5

http_payload_f2_part1 = b"GET /flag?data=flag{wrong_"  # Fragmento 1 de la falsa flag 2
http_payload_f2_part2 = b"flag_5678} HTTP/1.1\r\n"  # Fragmento 2 de la falsa flag 2

http_payload_f4_part1 = b"GET /flag?data=flag{not_"  # Fragmento 1 de la falsa flag 4
http_payload_f4_part2 = b"the_flag_0000} HTTP/1.1\r\n"  # Fragmento 2 de la falsa flag 4


# Crear paquetes fragmentados para la bandera real y las falsas
packet_part1 = ether / ip / tcp / Raw(load=http_payload_part1)
packet_part2 = ether / ip / tcp / Raw(load=http_payload_part2)
packet_part3 = ether / ip / tcp / Raw(load=http_payload_part3)
packet_part4 = ether / ip / tcp / Raw(load=http_payload_part4)
packet_part5 = ether / ip / tcp / Raw(load=http_payload_part5)

# Crear paquetes con fragmentos de banderas falsas
packet_f1_part1 = ether / ip / tcp / Raw(load=http_payload_f1_part1)
packet_f1_part2 = ether / ip / tcp / Raw(load=http_payload_f1_part2)

packet_f3_part1 = ether / ip / tcp / Raw(load=http_payload_f3_part1)
packet_f3_part2 = ether / ip / tcp / Raw(load=http_payload_f3_part2)

packet_f5_part1 = ether / ip / tcp / Raw(load=http_payload_f5_part1)
packet_f5_part2 = ether / ip / tcp / Raw(load=http_payload_f5_part2)

packet_f2_part1 = ether / ip / tcp / Raw(load=http_payload_f2_part1)
packet_f2_part2 = ether / ip / tcp / Raw(load=http_payload_f2_part2)

packet_f4_part1 = ether / ip / tcp / Raw(load=http_payload_f4_part1)
packet_f4_part2 = ether / ip / tcp / Raw(load=http_payload_f4_part2)



# Escribir todos los paquetes en un solo archivo .pcap
wrpcap("trafico_misterioso_incompleto.pcap", [
    packet_part1, packet_part2, packet_part3, packet_part4, packet_part5,  # Flag real fragmentada
    packet_f1_part1, packet_f1_part2,  # Flag falsa 1
    packet_f3_part1, packet_f3_part2,  # Flag falsa 3
    packet_f5_part1, packet_f5_part2,  # Flag falsa 5
    packet_f2_part1, packet_f2_part2,  # Flag falsa 2
    packet_f4_part1, packet_f4_part2,  # Flag falsa 4
    
])

print("Archivo 'trafico_misterioso.pcap' creado correctamente.")
