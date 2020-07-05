# routerpass
Script para poder tomar los datos de un AP especificamente de un operador de fibra optica, con usuarios y pass por defecto

Yo lo he ejecutado con un

Hice un escaneo con nmap:

nmap -sP 192.168.1.0/24

Luego tomar las ips

cat ips.txt | grep -w "[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}" --color | cut -d" " -f 5 > ipsnuevas.txt

Luego pasarlo a xargs

echo "ip1 ip2 ip3" | xargs -n 1 -I IP python router.py IP
