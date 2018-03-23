#include <stdio.h>
#include "objet.h"
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <assert.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>




position * centre_boxing (obj * objet)//calcule le centre du boxing et les stock dans une position
{
	double X = objet->x + (objet->largeur)/2;
//	printf("%lf",objet->x);
//	printf("%lg",X);
	double Y = objet->y + (objet->longueur)/2;
	position *centre = malloc(sizeof(position));
	centre->x = X;
	centre->y = Y;
	centre-> longueur = 1;
	centre-> largeur = 1;
	return centre;
}
 typedef enum  _pos {HAUT_GAUCHE, HAUT_DROITE, BAS_GAUCHE, BAS_DROITE, CENTRE, HAUT, BAS, DROITE, GAUCHE} pos;
 typedef enum _posfin{GAUCHE_PROCHE, DROITE_PROCHE, EN_FACE, GAUCHE_LOIN, DROITE_LOIN, LOIN_DEVANT}posfin;

pos position_dans_image(double longueur_image, double largeur_image, obj *objet)//retourne la zone ou se situe le centre du boxing
{
	 //printf("%lf",objet->x);
	 position *centre = centre_boxing (objet);
	 if(centre->x < largeur_image/2 && centre->y < longueur_image/2 )
	 {
		 //printf("haut a gauche");
		 return HAUT_GAUCHE;
		 
	 }
	 else if(centre->x > largeur_image/2 && centre->y < longueur_image/2 )
	 {
		 //printf("haut a droite");
		 return HAUT_DROITE;
	 }
	else if(centre->x > largeur_image/2 && centre->y > longueur_image/2 )
	 {
//		 printf("bas a droite");
		 return BAS_DROITE;
	 } 
	else if(centre->x < largeur_image/2 && centre->y > longueur_image/2 )
	 {
		 //printf("bas a gauche");
		 return BAS_GAUCHE;
	 }
	 else if(centre->x == largeur_image/2 && centre->y == longueur_image/2 )
	 {
		 //printf("au centre");
		 return CENTRE;
	 }
	 else if(centre->x == largeur_image/2 && centre->y < longueur_image/2 )
	 {
		 //printf("en haut ");
		 return HAUT;
	 }
	 else if(centre->x == largeur_image/2 && centre->y > longueur_image/2 )
	 {
		 //printf("en bas");
		 return BAS;
	 }
	 else if(centre->x > largeur_image/2 && centre->y == longueur_image/2 )
	 {
		 //printf("a droite");
		 return DROITE;
	 }
	 else 
	 {
		 //printf("a gauche");
		 return GAUCHE;
	 }
}
char** str_split(char* a_str, const char a_delim)
{
    char** result    = 0;
    size_t count     = 0;
    char* tmp        = a_str;
    char* last_comma = 0;
    char delim[2];
    delim[0] = a_delim;
    delim[1] = 0;

    /* Count how many elements will be extracted. */
    while (*tmp)
    {
        if (a_delim == *tmp)
        {
            count++;
            last_comma = tmp;
        }
        tmp++;
    }

    /* Add space for trailing token. */
    count += last_comma < (a_str + strlen(a_str) - 1);

    /* Add space for terminating null string so caller
       knows where the list of returned strings ends. */
    count++;

    result = malloc(sizeof(char*) * count);

    if (result)
    {
        size_t idx  = 0;
        char* token = strtok(a_str, delim);

        while (token)
        {
            assert(idx < count);
            *(result + idx++) = strdup(token);
            token = strtok(0, delim);
        }
        assert(idx == count - 1);
        *(result + idx) = 0;
    }

    return result;
}


liste *inserer_en_tete (liste *liste_des_objets,obj objet_liste)
{
	liste *el = (liste*)malloc(sizeof(liste));
	el->objet = objet_liste;
	el->suivant = liste_des_objets;
	return el;
}

liste * liste_des_objets (char * string)
{
	char **tokens;
	double x, y, largeur, longueur, taille; char nom[20] ="";
	liste *list =NULL;
	if(string)
	{	tokens = str_split(string, ';');
		if(tokens)
		{
			int i;
			for (i=0;*(tokens+i);i++)
			{
				sscanf(*(tokens+i), "%s , %lg , %lg , %lg , %lg", nom, &x,&y,&largeur, &longueur);
				obj objj ;
				strcat(objj.nom, nom); objj.x=x; objj.y=y; objj.largeur=largeur; objj.longueur = longueur; objj.hauteur_reelle=taille;
				list = inserer_en_tete(list, objj);
				
				 memset(objj.nom, '\0', 20);
				free(*(tokens+i));
				
			}
			free(tokens);
		}
	}
	return list;
}

char * Detection_simple (char *string)
{
	
	liste *liste1=liste_des_objets(string);
	obj *objet1 = &(liste1->objet);
	objet1->hauteur_reelle=100;

	char phrase[100] = "";

	//printf("%d",position_dans_image(700,700,objet1));
	if(position_dans_image(700,700,objet1)==2 && est_proche(objet1) == true)//bas gauche proche
	{
		strcat(phrase, objet1->nom+ " se trouve immédiatement sur votre gauche.");
	}
	else if(position_dans_image(700,700,objet1)==3 && est_proche(objet1) == true)//bas droite proche
	{
		strcat(phrase,objet1->nom+ " se trouve immédiatement sur votre droite.");
	}
	else if(position_dans_image(700,700,objet1)==6 && est_proche(objet1) == true)//bas proche
	{
		strcat(phrase,objet1->nom+ " se trouve en face de vous .");
	}
	//au fond
	else if(position_dans_image(700,700,objet1)==0 && est_proche(objet1) == false)//haut gauche proche
	{
		strcat(phrase,objet1->nom+ " se trouve plus loin sur votre gauche.");
	}
	else if(position_dans_image(700,700,objet1)==1 && est_proche(objet1) == false)//haut droite proche
	{
		strcat(phrase,objet1->nom+ " se trouve plus loin sur votre droite.");
	}
	else if(position_dans_image(700,700,objet1)==5 && est_proche(objet1) == false)//bas gauche proche
	{
		strcat(phrase,objet1->nom+ " se trouve plus loin devant vous.");
	}
	else{
		strcat(phrase,"ouvrez la fenetre et sautez.");
	}

return phrase;
	
}
void Detection_complexe()
{
	//creation ligne
	
//on declare le nombre d'objets correspondants avec des if
//	if(nombre_lignes == 1)
//	{
//		obj*objet1 =malloc(sizeof(obj));
//		int i=0;
//		while(ligne[i]!=',')
//		{
//			objet1->nom +=chaine[i];
//			i++;
//		}
//		i++;
//		while(ligne[i]!=',')
//		{
//			objet1->x += ligne[i];
//			i++;
//		}
//		
//		i++;
//		while(ligne[i]!=',')
//		{
//			objet1->y += ligne[i];
//			i++;
//		}
//		i++;
//		while(ligne[i]!=',')
//		{
//			objet1->longueur += ligne[i];
//			i++;
//		}
//		i++;
//		while(ligne[i]!=',')
//		{
//			objet1->largeur += ligne[i];
//			i++;
//		}
//		i++;
//		while(ligne[i]!=',')
//		{
//			objet1->hauteur_reelle += ligne[i];
//			i++;
//		}
//		Detection_simple(objet1);
//	}
//	//2 objets detectés
//	else if(nombre_lignes == 2)
//	{
		obj*objet1=malloc(sizeof(obj));
		obj*objet2=malloc(sizeof(obj));

//	objet1-> nom = "a";
//	objet1->hauteur_reelle = 100.0;
//	objet1->x = 6.0;//call stack
//	objet1->y = 666.0;
//	objet1->largeur = 80.0;
//	objet1->longueur = 20.0;
//	
//	objet2-> nom = "b";
//	objet2->hauteur_reelle = 100.0;
//	objet2->x = 6.0;//call stack
//	objet2->y = 6.0;
//	objet2->largeur = 20.0;
//	objet2->longueur = 20.0;
//		int i=0;
//		while(ligne[i]!=',')
//		{
//			objet1->nom +=chaine[i];
//			i++;
//		}
//		i++;
//		while(ligne[i]!=',')
//		{
//			objet1->x += ligne[i];
//			i++;
//		}
//		
//		i++;
//		while(ligne[i]!=',')
//		{
//			objet1->y += ligne[i];
//			i++;
//		}
//		i++;
//		while(ligne[i]!=',')
//		{
//			objet1->longueur += ligne[i];
//			i++;
//		}
//		i++;
//		while(ligne[i]!=',')
//		{
//			objet1->largeur += ligne[i];
//			i++;
//		}
//		i++;
//		while(ligne[i]!=',')
//		{
//			objet1->hauteur_reelle += ligne[i];
//			i++;
//		}
		//...
		//comparaisons obstacles
		//obj1 devant obj2
		if(Detection_simple(objet1)==0 && Detection_simple(objet2)==3)
		{
			printf("attention %c se trouve entre vous et %c", objet1->nom, objet2->nom);
		}
		else if(Detection_simple(objet1)==1 && Detection_simple(objet2)==4)
		{
			printf("attention %c se trouve entre vous et %c", objet1->nom, objet2->nom);
		}
		else if(Detection_simple(objet1)==2 && Detection_simple(objet2)==5)
		{
			printf("attention %c se trouve entre vous et %c", objet1->nom, objet2->nom);
		}
		//obj2 devant obj1
		else if(Detection_simple(objet2)==0 && Detection_simple(objet1)==3)
		{
			printf("attention %c se trouve entre vous et %c", objet2->nom, objet1->nom);
		}
		else if(Detection_simple(objet2)==1 && Detection_simple(objet1)==4)
		{
			printf("attention %c se trouve entre vous et %c", objet2->nom, objet1->nom);
		}
		else if(Detection_simple(objet2)==2 && Detection_simple(objet1)==5)
		{
			printf("attention %c se trouve entre vous et %c", objet2->nom, objet1->nom);
		}
		else
		{
			printf("buuuuuuug");
		}
//	}
//	else if (nombre_objets ==3)
//	{
//		
//	}
//	
//on fait les conditions
	free(objet1);
	free(objet2);

}


void write_to_pipe (char *fifo, char *message)
{
    int fd; 
    // Open FIFO for write only
    fd = open(fifo, O_WRONLY);

    // Write the input arr2ing on FIFO
    // and close it
    write(fd, message, strlen(message)+1);
    close(fd);
    return 0;
}



void read_from_pipe (char *fifo, char *message)
{
    int fd; 
    // Open FIFO for write only
    fd = open(fifo, O_RDONLY);
    // Read from FIFO 
    read(fd, message, 250);

    // Print the read message
    close(fd);

    return 0;
}




int main(int argc, char **argv)
{
//	position * p = malloc(sizeof(position));
//	p->x = 5;
//	p->y = 6;
//	p->largeur = 50;
//	p->longueur = 50;
	
	//determination des boxings en dur
	
//	obj * chaise = malloc(sizeof(obj));
//	chaise-> nom = 'c';
//	chaise->hauteur_reelle = 100.0;
//	chaise->x = 6.0;//call stack
//	chaise->y = 666.0;
//	chaise->largeur = 80.0;
//	chaise->longueur = 20.0;
	//il faudrait créer un héritage des que l on créé des chaises, on ajoute juste la position.
	
//position_dans_image(700,700,chaise);

//Detection_complexe();//param file
//est_proche(chaise);


char test[250] = "";
read_from_pipe("/tmp/fifo_file", test);

//liste *list = liste_des_objets(test);
 write_to_pipe("/tmp/vocal_fifo", Detection_simple(test));
//printf("%s", list->objet.nom);

	return 0;
}
