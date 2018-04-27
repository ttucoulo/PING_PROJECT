from geometric_situation import *

objects_list = {'personne' : [1800, 'une'], 'telephone' : [100, 'un'], 'ordinateur' : [250, 'un'], 'sac' : [400, 'un'], 'chaise' : [800, 'une'], 'table' : [800, 'une'], 'livre' : [100, 'un'], 'fauteuil' : [800, 'un'], 'bouteille': [100, 'une'], 'ecran' : [400, 'un']}

class Objet:
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
	objet = fifo.readline().rstrip('\x00').split(";")
	for obj in objet:
		tab = obj.split(",")
		if tab[0].strip() in objects_list.keys():
			try:
				new_objet=Objet(tab[0].strip(),int(tab[1].strip()),int(tab[2].strip()),int(tab[3].strip()),int(tab[4].strip()))
			liste.append(new_objet)
			except ValueError:
	obj_names_list = [o.nom for o in liste if o]
	fifo.close()
	return obj_names_list, liste



