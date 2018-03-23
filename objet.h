#ifndef OBJET_H
#define OBJET_H
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
typedef struct _position 
{
	double x;
	double y;
	double longueur;
	double largeur;
}position;

typedef struct _objet
{
	char nom[20];
//	position *pos;
	double x;
	double y;
	double longueur;
	double largeur;
	double hauteur_reelle;
}obj;

typedef struct list_objets
{
	obj objet;
	struct list_objets *suivant;
}liste;

bool est_proche (obj *objet);
#endif