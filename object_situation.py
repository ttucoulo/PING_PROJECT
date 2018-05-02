import collections as c
from objects import *
from operator import attrgetter


def detection_obstacle(liste,wanted_object,seuil_angle):
	result = []
	if liste and len(liste)> 1 and wanted_object in liste :
		pot_obstacleS = [item for item in liste if item != wanted_object and objects_list[item.nom][2]]
		for pot_obstacle in pot_obstacleS:
                        if(pot_obstacle.distance < wanted_object.distance):
				if (abs(wanted_object.angle - pot_obstacle.angle) < seuil_angle):
					result.append(pot_obstacle)
	return result




def return_reachable_object(liste_objet, object_name, seuil_angle):
	liste_with_obstacle=[]
	liste_sans_obstacle=[]

	wanted_objects = [item for item in liste_objet if item.nom == object_name]
	
	for element in wanted_objects :
		obstacles = detection_obstacle(liste_objet, element, seuil_angle)
		if obstacles :
			liste_with_obstacle.append(element)
		else:
			liste_sans_obstacle.append(element)
	if liste_sans_obstacle:
		return min(liste_sans_obstacle, key=attrgetter('distance')), None
	elif liste_with_obstacle:
		object = min(liste_with_obstacle, key=attrgetter('distance'))
		return object, detection_obstacle(liste_objet, object, seuil_angle)
	else:
		return None, None




def situate_object(objet,obstacles, angle_seuil, distance_seuil):
	phrase = "{0} {1} se trouve ".format(objects_list[objet.nom][1], objet.nom)
	if abs(objet.angle) <= angle_seuil:
		phrase = "{0} juste devant vous ".format(phrase)
	elif abs(objet.angle) > angle_seuil:
		if objet.angle >0 :
			phrase="{0} sur votre droite".format(phrase)
		else:
			phrase = "{0} sur votre gauche".format(phrase)
	if objet.distance < distance_seuil:
		phrase = "{0} juste a {1} metres. ".format(phrase, objet.distance)
	else:
		phrase = "{0} un peu plus loin a {1} metres. ".format(phrase, objet.distance)
	t=""
	if obstacles:
		for obstacle in obstacles:
			t = t+objects_list[obstacle.name][1]+" "+ obstacle.name +", "
		phrase = "{0} Mais attention, {1} se trouvent avant".format(phrase, t)
	return phrase



