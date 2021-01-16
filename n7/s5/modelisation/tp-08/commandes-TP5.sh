#!/bin/sh
echo "Affichage des lignes contenant des nombres entiers naturels :"
egrep -e "\s\+?(0|[1-9][0-9]*)$" exemple.txt
echo "Affichage des lignes contenant des nombres entiers relatifs :"
egrep -e "\s(0|(\+|-)[1-9][[:digit:]]*)$" exemple.txt
echo "Affichage des lignes contenant des nombres décimaux :"
egrep -e "\s-?(0\.[0-9]*((e|E)-?10)?)$" exemple.txt
echo "Affichage des lignes contenant des nombres rationnels :"
egrep -e "\s-?[1-9][0-9]*\/[1-9][0-9]*$" exemple.txt
echo "Affichage des lignes contenant des nombres complexes rationnels :"
egrep -e "\s-?[0-9\/+-]*i$" exemple.txt
