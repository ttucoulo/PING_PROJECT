

import os
import sys
import collections as c


while True:
	obj_names, objects = liste_des_objets()
	liste_inter = list(set(obj_names).intersection(objects_list))

	fifo = open("/tmp/detection", "r")
	phrase = "je ne vois rien"
	for line in fifo:
		if line=="description":
			phrase = description(liste_inter, obj_list)


	
	path2 = "/tmp/vocal_fifo"
	fifo = open(path2, "w")
	

	fifo.write(phrase)
	fifo.close()

