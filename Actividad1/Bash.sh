#!/bin/bash
echo "Inserte un numero 101,510 o 999"
read n
if [ $n -eq 101 ];
then
echo "Ese es el primer numero"
elif [ $n -eq 510 ];
then
echo "Ese es el segundo numero"
elif [ $n -eq 999 ];
then
echo "Ese es el tercer numero"
else
echo "Numero incorrecto"
fi