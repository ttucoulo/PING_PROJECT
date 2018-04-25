import math


###Camera techs specs
FOCAL = 3.04
SENSOR_HEIGHT = 2.76 
HORIZONTAL_FIELD_VIEW = 62.2 # degrees
VERTICAL_FIELD_VIEW = 48.8

###Image Size
FRAME_HEIGHT = 720
FRAME_WIDTH = 1280

HALF_HORIZONTAL_FIELD_VIEW = HORIZONTAL_FIELD_VIEW/2
ANGLE_BY_PIXEL = HORIZONTAL_FIELD_VIEW/FRAME_WIDTH



#We calculate the distance from the center
def normalize_X(x):
	return x-FRAME_WIDTH/2

def calculate_distance(real_object_height, image_object_height):
	return (FOCAL * real_object_height * FRAME_HEIGHT)/(image_object_height * SENSOR_HEIGHT)


def calculate_angle(x):
	return normalize_X(x) * ANGLE_BY_PIXEL

def orthogonal_projection(angle, distance):
	return math.cos(math.radians(angle)) * distance 

def distance_from_center(angle, distance):
	return math.sin(math.radians(angle)) * distance 


if __name__ == '__main__':
	print(calculate_angle(1280))
