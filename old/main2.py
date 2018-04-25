from enum import Enum

class position:
	def __init__(self,X,Y):
		self.x=X
		self.y=Y

class objet:
	def __init__(self,Nom,X,Y,Largeur,Longueur,Hauteur_reelle):
		self.nom=Nom
		self.x=X
		self.y=Y
		self.longueur=Longueur
		self.largeur=Largeur
		self.hauteur_reelle=Hauteur_reelle


def centre_boxing(objet):
	X= objet.x+(objet.largeur)/2
	Y=objet.y+(objet.longueur)/2
	centre=position(X,Y)
	return centre

class _pos (Enum):
	HAUT_GAUCHE=0
	HAUT_DROIT=1
	BAS_GAUCHE=2
	BAS_DROIT=3
	CENTRE=4
	HAUT=5
	BAS=6
	DROITE=7
	GAUCHE=8

class _posfin(Enum):
	GAUCHE_PROCHE=0
	DROITE_PROCHE=1
	EN_FACE=2
	GAUCHE_LOIN=3
	DROITE_LOIN=4
	LOIN_DEVANT=5


def position_dans_image(longueur_image, largeur_image, objet):
	centre=centre_boxing(objet)
	if(centre.x < largeur_image/2 and centre.y < longueur_image/2):
		return _pos.HAUT_GAUCHE
	elif(centre.x >largeur_image/2 and centre.y < longueur_image/2):
		return _pos.HAUT_DROIT
	elif(centre.x > largeur_image/2 and centre.y > longueur_image/2):
		return _pos.BAS_DROIT
	elif(centre.x < largeur_image/2 and centre.y > longueur_image/2):
		return BAS_GAUCHE
	elif(centre.x == largeur_image/2 and centre.y == longueur_image/2):
		return CENTRE

	elif(centre.x == largeur_image/2 and centre.y < longueur_image/2):
		return HAUT
	elif(centre.x == largeur_image/2 and centre.y > longueur_image/2):
		return BAS
	elif(centre.x > largeur_image/2 and centre.y == longueur_image/2):
		return DROITE
	else:
		return GAUCHE

def est_proche(objet):
	if(objet.largeur>objet.hauteur_reelle*2/3):
		return True
	else:
		return False


def liste_des_objets (string,taille):
	liste=[]
	if (string):
		tokens=string.split(';')[:-1]
		if(tokens):
			for case in tokens:
				tab=case.split(',')
				new_objet=objet(tab[0],int(tab[1]),int(tab[2]),int(tab[3]),int(tab[4]),100)
				liste.append(new_objet)
	return liste


def Detection_simple (string):
	liste1=liste_des_objets(string,100)
	objet1=liste1[0]
	if(position_dans_image(700,700,objet1)==2 and est_proche(objet1) == True):
		return objet1.nom +" se trouve immediatement sur votre gauche."
	elif(position_dans_image(700,700,objet1)==3 and est_proche(objet1) == True):
		return objet1.nom + " se trouve immediatement sur votre droite."
	elif(position_dans_image(700,700,objet1)==6 and est_proche(objet1) == True):
		return objet1.nom+ " se trouve en face de vous ."
	elif(position_dans_image(700,700,objet1)==0 and est_proche(objet1) == False):
		return objet1.nom+ " se trouve plus loin sur votre gauche."
	elif(position_dans_image(700,700,objet1)==1 and est_proche(objet1) == False):
		return objet1.nom+ " se trouve plus loin sur votre droite."
	elif(position_dans_image(700,700,objet1)==5 and est_proche(objet1) == False):
		return objet1.nom+ " se trouve plus loin devant vous."
	else:
		return "ouvrez la fenetre et sautez."


def read_from_pipe (path):
        fifo = open(path, "r")

        message  = ""
        for line in fifo:
                message +=line
        fifo.close()
        return message



def write_to_pipe (fifo,message):
	fichier = open(fifo, 'w')
    	fichier.write(message)
    	fichier.close()




test = read_from_pipe("/tmp/fifo_file")
write_to_pipe("/tmp/vocal_fifo", Detection_simple(test))
