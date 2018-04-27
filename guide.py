
from object_situation import *

import os
import sys
import collections as c


def write_fifo(path, message):
	fifo = open(path, "w")

        fifo.write(message)
        fifo.close()

def read_fifo(path):
	fifo = open(path, "r")
	message = fifo.readline()
	fifo.close()
	return message

while True:
        path2 = "/tmp/vocal_fifo"
	obj_names, objects = liste_des_objets()
        word = read_fifo("/tmp/detection")

	if not (obj_names and objects):	
		write_fifo(path2, "je ne reconnais rien de ce que j'ai appris")
		continue

	phrase = ""
	if word =="description":
		phrase = description(obj_names)
	elif word in  objects_list.keys():
		phrase = detection_simple(objects[0], 15, 2)
	else:
		phrase = "je ne comprends pas la requete"

	print(phrase)
	write_fifo(path2, phrase)
