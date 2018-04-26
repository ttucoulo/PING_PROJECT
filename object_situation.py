
from objects import *

def description (liste, obj_list):
	if not liste:
		phrase = "Je ne reconnais rien de ce que j'ai appris"
	else:
		dic = c.Counter(obj_list)
		phrase = "il y a "
		plur = ""
		for mot in liste:
			if dic[mot] > 1:
				plur = "des"
			else:
				plur = objects_list[mot][1]
			phrase += plur+" "
			phrase+=mot
			phrase +=", "
	return phrase


def detection_simple(objet,distance, seuil_oppose, seuil_distance):
        oppose=distance_from_center(calculate_angle(objet.x),distance)
        if(oppose>-seuil_oppose and oppose<seuil_oppose and distance <seuil_distance):
                return "l'objet se trouve au centre devant vous"
        elif(oppose<=-seuil_oppose and distance <seuil_distance):
                return "l'objet se trouve juste sur votre gauche"
        elif(oppose>=seuil_oppose and distance<seuil_distance):
                return "l'objet se trouve juste sur votre droite"
        elif(oppose>-seuil_oppose and oppose<seuil_oppose and distance >seuil_distance):
                return "l'objet se trouve devant vous"
        elif(oppose<=seuil_oppose and distance >seuil_distance):
                return "l'objet se trouve un peu plus loin sur votre gauche"
        else:
                return "l'objet se trouve un peu plus loin sur votre droite"


def detection_obstacle(liste,index_in_liste,seuil_angle):   #index_in_liste est l'index dans la liste de l'objet que je souhaite atteindre
    if (liste):
        if(len(liste)==1):
            return "Il n'y a aucun obstacle devant l'objet"
        else:
            angle_objet=calculate_angle(liste[index_in_liste].x)
            projete_mediane_objet=orthogonal_projection(liste[index_in_liste].angle,liste[index_in_liste].distance)
            for element in liste:
                if(element.x!=liste[index_in_liste].x or element.y!=liste[index_in_liste].y):
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
