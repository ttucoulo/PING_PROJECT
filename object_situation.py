import collections as c
from objects import *

def description (liste):
	if not liste:
		phrase = "Je ne reconnais rien de ce que j'ai appris"
	else:
		dic = c.Counter(liste)
		phrase = "il y a "
		plur = ""
		for mot in dic.keys():
			if dic[mot] > 1:
				plur = "des"
			else:
				plur = objects_list[mot][1]
			phrase += plur+" "
			phrase+=mot
			phrase +=", "
	return phrase


def detection_simple(objet, angle_seuil, distance_seuil):
	phrase = "{0} {1} se trouve ".format(objects_list[objet.nom][1], objet.nom)
	if abs(objet.angle) <= angle_seuil:
		phrase = "{0} juste devant vous ".format(phrase)
	elif abs(objet.angle) > angle_seuil:
		if objet.angle >0 :
			phrase="{0} sur votre droite".format(phrase)
		else:
			phrase = "{0} sur votre gauche".format(phrase)
	if objet.distance < distance_seuil:
		phrase = "{0} juste a {1} metres".format(phrase, objet.distance)
	else:
		phrase = "{0} un peu plus loin a {1} metres".format(phrase, objet.distance)
	return phrase




######### Non intégrée pour l'instant
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
