from geometric_situation import *


if __name__ == "__main__":
	#print(orthogonal_projection1(calculate_angle(1280), 6))
	#print(detection_simple(1100,1.5))
	liste=list()
	table=objet("table",500,500,200,200)
	chaise=objet("chaise",560,50,200,200)
	#ordinateur=objet("ordinateur",1000,500,50,100)
	liste.append(table)
	liste.append(chaise)
	#liste.append(ordinateur)
	print(detection_obstacle(liste,0,30))
