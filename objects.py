from geometric_situation import *

objects_list = ['personne' : [1800, 'un'], 'telephone' : [10, 'un'], 'ordinateur' : [25, 'un'], 'sac' : [40, 'un'], 'chaise' : [80, 'une'], 'table' : [80, 'une'], 'livre' : [10, 'un'], 'fauteuil' : [80, 'un'], 'bouteille': [10, 'une'], 'ecran' : [40, 'un']]


class objet:
	def __init__(self,Nom,X,Y,Largeur,Hauteur):
		self.nom=Nom
		self.x=X
		self.y=Y
		self.largeur=Largeur
		self.hauteur=Hauteur
		self.distance=calculate_distance(objects_list[Nom][0],Hauteur)
		self.angle=calculate_angle(X)


def liste_des_objets():
	path = "/tmp/fifo_file"
	fifo = open(path, "r")
	liste = []
	objet = line.readline().rstrip('\x00').split(";")
	for obj in objet:
		tab = obj.split(",")
		if tab[0].strip() in objects_list.keys():
			new_objet=objet(tab[0].strip(),int(tab[1].strip()),int(tab[2].strip()),int(tab[3].strip()),int(tab[4].strip()))
			liste.append(new_objet)
	obj_names_list = [o.nom for x in liste if x]
	fifo.close()
	return obj_names_list, liste



