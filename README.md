<h1>ROUTERPASSS</h1>

Script para poder tomar los datos de un AP especificamente de un operador de fibra optica, con usuarios y pass por defecto

Yo lo he ejecutado con un

Hice un escaneo con nmap:

<h3>nmap -sP 192.168.1.0/24</h3>

Luego tomar las ips

<h3>cat ips.txt | grep -w "[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}" --color | cut -d" " -f 5 > ipsnuevas.txt</h3>

Luego pasarlo a xargs

<h3>cat ips.txt | xargs -n 1 -I IP python routerpass.py IP</h3>
