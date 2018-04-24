import math


###Camera techs specs
FOCAL = 3.04
SENSOR_HEIGHT = 2.76 
HORIZONTAL_FIELD_VIEW = 62.2 # degrees
VERTICAL_FIELD_VIEW = 48.8

###Image Size
FRAME_HEIGHT = 720
FRAME_WIDTH = 1280

HALF_HORIZONTAL_FIELD_VIEW = HORIZONTAL_FIELD_VIEW/2
ANGLE_BY_PIXEL = HORIZONTAL_FIELD_VIEW/FRAME_WIDTH

class objet:
	def __init__(self,Nom,X,Y,Largeur,Hauteur):
		self.nom=Nom
		self.x=X
		self.y=Y
		if(Nom=="table"):
			real_object_height=80
		elif(Nom=="chaise"):
			real_object_height=80
		else:
			real_object_height=20
		self.largeur=Largeur
		self.hauteur=Hauteur
		self.distance=calculate_distance(real_object_height,Hauteur)
		self.angle=calculate_angle(X)

#We calculate the distance from the center
def normalize_X(x):
	return x-FRAME_WIDTH/2

def calculate_distance(real_object_height, image_object_height):
	return (FOCAL * real_object_height * FRAME_HEIGHT)/(image_object_height * SENSOR_HEIGHT)


def calculate_angle(x):
	return normalize_X(x) * ANGLE_BY_PIXEL

def orthogonal_projection(angle, distance):
	return math.cos(math.radians(angle)) * distance 

def orthogonal_projection1(angle, distance):
	return math.sin(math.radians(angle)) * distance 

def detection_simple(x,distance):
	oppose=orthogonal_projection1(calculate_angle(x),distance)
	if(oppose>-0.5 and oppose<0.5 and distance <2):
		return "l'objet se trouve au centre devant vous"
	elif(oppose<=-0.5 and distance <2):
		return "l'objet se trouve juste sur votre gauche"
	elif(oppose>=0.5 and distance<2):
		return "l'objet se trouve juste sur votre droite"
	elif(oppose>-0.5 and oppose<0.5 and distance >2):
		return "l'objet se trouve devant vous"
	elif(oppose<=0.5 and distance >2):
		return "l'objet se trouve un peu plus loin sur votre gauche"
	else:
		return "l'objet se trouve un peu plus loin sur votre droite"


def liste_des_objets (string):
	liste=[]
	if (string):
		tokens=string.split(';')[:-1]
		if(tokens):
			for case in tokens:
				tab=case.split(',')
				new_objet=objet(tab[0],int(tab[1]),int(tab[2]),int(tab[3]),int(tab[4]))
				liste.append(new_objet)
	return liste


def detection_obstacle(liste,index_in_liste,seuil_angle):   #index_in_liste est l'index dans la liste de l'objet que je souhaite atteindre
    if (liste):
        if(len(liste)==1):
            return "Il n'y a aucun obstacle devant l'objet"
        else:
	    angle_objet=calculate_angle(liste[index_in_liste].x)
            projete_mediane_objet=orthogonal_projection(liste[index_in_liste].angle,liste[index_in_liste].distance)
            for element in liste:
		angle_element=calculate_angle(element.x)
		projete_mediane_obstacle=orthogonal_projection(element.angle,element.distance)
		if(projete_mediane_obstacle<projete_mediane_objet):
			if(angle_element+seuil_angle>angle_objet and angle_element<angle_objet):
                    		return "Obstacle detecte "+element.nom
                	elif(angle_element-seuil_angle<angle_objet and angle_element> angle_objet):
                    		return "Obstacle detecte "+element.nom
            return "Il n'y a aucun obstacle devant l'objet"
    else:
        return "Il n'y a aucun objet dans votre champ de vision"



if __name__ == '__main__':
	print(calculate_angle(1280))
