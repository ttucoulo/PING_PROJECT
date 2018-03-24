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
	 
	 position *centre = centre_boxing (objet);
	 if(centre->x < largeur_image/2 && centre->y < longueur_image/2 )
	 {
		 return HAUT_GAUCHE;	 
	 }
	 else if(centre->x > largeur_image/2 && centre->y < longueur_image/2 )
	 {
		 return HAUT_DROITE;
	 }
	else if(centre->x > largeur_image/2 && centre->y > longueur_image/2 )
	 {
		 return BAS_DROITE;
	 } 
	else if(centre->x < largeur_image/2 && centre->y > longueur_image/2 )
	 {
		 return BAS_GAUCHE;
	 }
	 else if(centre->x == largeur_image/2 && centre->y == longueur_image/2 )
	 {
		 return CENTRE;
	 }
	 else if(centre->x == largeur_image/2 && centre->y < longueur_image/2 )
	 {
		 return HAUT;
	 }
	 else if(centre->x == largeur_image/2 && centre->y > longueur_image/2 )
	 {
		 return BAS;
	 }
	 else if(centre->x > largeur_image/2 && centre->y == longueur_image/2 )
	 {
		 return DROITE;
	 }
	 else 
	 {
		 return GAUCHE;
	 }
	 free(centre);
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


liste * free_list(liste *list)
{
	liste *temp= list;
	if(temp != NULL)
	{
		free_list(temp->suivant);
		free(temp);
		temp = NULL;

	}
	return NULL;
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

	char *phrase = (char*)malloc(sizeof(char)*100);
	memset(phrase, '\0', 100);

	//printf("%d",position_dans_image(700,700,objet1));
	if(position_dans_image(700,700,objet1)==2 && est_proche(objet1) == true)//bas gauche proche
	{
		strcat(phrase,"l'objet se trouve immédiatement sur votre gauche.");
	}
	else if(position_dans_image(700,700,objet1)==3 && est_proche(objet1) == true)//bas droite proche
	{
		strcat(phrase,"l'objet se trouve immédiatement sur votre droite.");
	}
	else if(position_dans_image(700,700,objet1)==6 && est_proche(objet1) == true)//bas proche
	{
		strcat(phrase,"l'objet se trouve en face de vous .");
	}
	//au fond
	else if(position_dans_image(700,700,objet1)==0 && est_proche(objet1) == false)//haut gauche proche
	{
		strcat(phrase,"l'objet se trouve plus loin sur votre gauche.");
	}
	else if(position_dans_image(700,700,objet1)==1 && est_proche(objet1) == false)//haut droite proche
	{
		strcat(phrase,"l'objet se trouve plus loin sur votre droite.");
	}
	else if(position_dans_image(700,700,objet1)==5 && est_proche(objet1) == false)//bas gauche proche
	{
		strcat(phrase,"l'objet se trouve plus loin devant vous.");
	}
	else{
		strcat(phrase,"ouvrez la fenetre et sautez.");
	}
	free_list(liste1);

return phrase;
	
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

}




int main(int argc, char **argv)
{

char test[250] = "";

while(1){
read_from_pipe("/tmp/fifo_file", test);
char *phrase = Detection_simple(test);
write_to_pipe("/tmp/vocal_fifo", Detection_simple(test));
free(phrase);
memset(test, '\0',250);
}
	return 0;
}
