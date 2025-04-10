📄 RETO 3: Análisis de Tráfico de Red

🎯 Objetivo:
Analiza el archivo 'trafico_misterioso.pcap' con Wireshark y encuentra la comunicación sospechosa.
La flag está escondida dentro de una petición HTTP GET realizada a un servidor.

🛠 Herramienta recomendada:
- Wireshark
- pip install scapy (CMD)

📌 Pista:
Filtra por protocolo HTTP en Wireshark y revisa los métodos GET.

📝 Instrucciones:
1. Abre el archivo 'trafico_misterioso.pcap' con Wireshark.
2. Usa el filtro: http.request
3. Inspecciona las URLs en las líneas GET.
4. Encuentra la que contiene la flag y cópiala en 'flag_template.txt'
