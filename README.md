# routerpass
Script para poder tomar los datos de un AP especificamente de un operador de fibra optica, con usuarios y pass por defecto

Yo lo he ejecutado con un

echo "ip1 ip2 ip3" | xargs -n 1 -I IP python router.py IP
