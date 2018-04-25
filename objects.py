

objects_list = ['personne', 'telephone', 'ordinateur', 'sac', 'chaise', 'table', 'livre', 'fauteuil', 'bouteille', 'ecran']

mascular = {'un' : ['telephone', 'ordinateur', 'sac', 'livre', 'fauteuil','ecran'], 'une' : ['personne', 'chaise', 'table', 'bouteille']}

real_objects_heights = {"chaise" : 80, "table":80, "ordinateur":25}



class objet:
	def __init__(self,Nom,X,Y,Largeur,Hauteur):
		self.nom=Nom
		self.x=X
		self.y=Y
		self.largeur=Largeur
		self.hauteur=Hauteur
		self.distance=calculate_distance(real_objects_heights[Nom],Hauteur)
		self.angle=calculate_angle(X)




def liste_des_objets():
	path = "/tmp/fifo_file"
	fifo = open(path, "r")
	liste = []
	objet = line.readline().rstrip('\x00').split(";")
	for obj in objet:
		tab = obj.split(",")
		new_objet=objet(tab[0].strip(),int(tab[1].strip()),int(tab[2].strip()),int(tab[3].strip()),int(tab[4].strip()))
		liste.append(new_objet)
	obj_names_list = [o.Nom for x in liste if x]
	fifo.close()
	return obj_names_list, liste



