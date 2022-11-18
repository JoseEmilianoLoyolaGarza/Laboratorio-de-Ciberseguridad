#!/bin/bash
cd IPS
echo "Envio de correos" | mutt -s "Correo con direcciones enviado" pepeape@outlook.com -a Output.txt
