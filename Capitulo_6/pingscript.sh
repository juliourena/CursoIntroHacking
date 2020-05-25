# Ejemplo tomado del Libro de Georgia Weidman

#!/bin/bash
if [ "$1" == "" ]
then
echo "Uso: ./pingscript.sh [direccion de red]"
echo "Ejemplo: ./pingscript.sh 192.168.20"
else
for x in `seq 1 254`; do
ping -c 1 $1.$x | grep "64 bytes" | cut -d" " -f4 | sed 's/.$//'
done
fi
