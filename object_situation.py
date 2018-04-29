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


def return_reachable_object(liste_objet, seuil_angle):
	objet_distance_mini=Objet(None,None,None,None,None)
	liste_with_obstacle=[]
	liste_sans_obstacle=[]
	for element in liste_objet:
		if(detection_obstacle(liste_objet,liste_objet.index(element),seuil_angle)==True):
			liste_with_obstacle.append(element)
		else:
			liste_sans_obstacle.append(element)
	if(len(liste_sans_obstacle)==0):
		distance_mini=liste_with_obstacle[0].distance
		for objet in liste_with_obstacle:
			if(objet.distance<distance_mini):
				objet_distance_mini=objet
		return objet_distance_mini
	else:
		distance_mini=liste_sans_obstacle[0].distance
		for objet in liste_sans_obstacle:
			if(objet.distance<distance_mini):
				objet_distance_mini=objet
		return objet_distance_mini
			
		
	

def selection_objet(liste_objet, nom_objet,seuil_angle):
	compteur=0
	liste=[]
	for element in liste_objet:
		if(element.nom==nom_objet):
			compteur=compteur+1
	if(compteur==0):
		return "Il n'y a pas de "+nom_objet+" dans votre champ de vision"

	elif(compteur==1):
		for element in liste_objet:
			if(element.nom==nom_objet):
				return element
	else:
		for element in liste_objet:
			if(element.nom==nom_objet):
				liste.append(element)
		return return_reachable_object(liste,seuil_angle)




######### Non integree pour l'instant
def detection_obstacle(liste,index_in_liste,seuil_angle):   #index_in_liste est l'index dans la liste de l'objet que je souhaite atteindre
    if (liste):
        if(len(liste)==1):
            return False
        else:
            angle_objet=calculate_angle(liste[index_in_liste].x)
            projete_mediane_objet=orthogonal_projection(liste[index_in_liste].angle,liste[index_in_liste].distance)
            for element in liste:
                if(element.x!=liste[index_in_liste].x or element.y!=liste[index_in_liste].y):
                        angle_element=calculate_angle(element.x)
                        projete_mediane_obstacle=orthogonal_projection(element.angle,element.distance)
                        if(projete_mediane_obstacle<projete_mediane_objet):
                                if(angle_element+seuil_angle>angle_objet and angle_element<angle_objet):
                                        return True
                                elif(angle_element-seuil_angle<angle_objet and angle_element> angle_objet):
                                        return True
            return False
    else:
        return False
