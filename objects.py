from geometric_situation import *
from helper import read_fifo


objects_list = {'personne' : [1800, 'une', True], 'telephone' : [100, 'un', False], 'ordinateur' : [250, 'un', False], 'sac' : [400, 'un', False], 'chaise' : [800, 'une', True], 'table' : [800, 'une', True], 'livre' : [100, 'un', False], 'fauteuil' : [800, 'un', True], 'bouteille': [100, 'une', False], 'ecran' : [400, 'un', False]}

class Objet:
	def __init__(self,Nom,X,Y,Largeur,Hauteur):
		self.nom=Nom
		self.x=X
		self.y=Y
		self.largeur=Largeur
		self.hauteur=Hauteur
		self.distance=calculate_distance(objects_list[Nom][0],Hauteur)
		self.angle=calculate_angle(X+Largeur/2)

	def __eq__(self, other):
		return self.__dict__ == other.__dict__


def liste_des_objets():
	path = "/tmp/fifo_file"
	objet = read_fifo(path).rstrip('\x00').split(";")
	liste = []

	for obj in objet:
		tab = obj.split(",")
		if tab[0].strip() in objects_list.keys():
			try:
				new_objet=Objet(tab[0].strip(),int(tab[1].strip()),int(tab[2].strip()),int(tab[3].strip()),int(tab[4].strip()))
				liste.append(new_objet)
			except Exception as ex:
				print("object not parsable")
				print(ex)
	obj_names_list = [o.nom for o in liste if o]
	return obj_names_list, liste



