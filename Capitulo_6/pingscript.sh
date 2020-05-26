# Ejemplo tomado del Libro de Georgia Weidman con algunas modificaciones.

#/bin/bash
if [ "$1" == "" ]
then
	echo "Uso: ./ping.sh [direccion de red]"
	echo "Ejemplo: ./ping.sh 192.168.20"
else
	echo "Direccion de red selecionada $1"
	for ip in $(seq 1 254); do
		# echo "Intento de Ping a la Direccion IP $ip"
		ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f4 | tr -d ":" &
	done
fi
