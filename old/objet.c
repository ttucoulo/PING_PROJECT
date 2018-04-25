#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "objet.h"

typedef enum  _objets {T,c,p} objets;

bool est_proche (obj *objet1)
{
	if(objet1->largeur>objet1->hauteur_reelle*2/3)
		{
		//printf(" objet en hauteur");
		return true;
	}
	else 
	{
		//printf(" objet loin");
		return false;
	}
}

//programme qui rempli la structure objet

//obj * Construction_objet ()//file
//{
//	//lire file
//	//char[] lecture = //file.read
//	//obj * objet = malloc(sizeof(obj));
//	int i = 0;
//	while(lecture[i] != ',')
//	{
//		objet->nom += lecture[i];
//		i++;
//	}
//	i++;
//	while(lecture[i]!=',')
//	{
//		objet->x += lecture[i]
//	}
//	


