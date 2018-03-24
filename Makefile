Guide : main.o objet.o
	gcc main.o objet.o -o Guide

main.o : main.c objet.c
	gcc -c main.c -o main.o

objet.o : objet.c
	gcc -c objet.c -o objet.o
