from random import random

def randomhexcolor( pallor=0.0 ):
	s ='#'
	for i in [1,2,3]:
		if pallor >= 0:
			r = int( 256*pallor + 256*(1-pallor)*random() )  # pallor = whiteness
		else:
			r = int(              256*(1+pallor)*random() )  # pallor = whiteness
		s += hex(r)[2:].zfill(2)
	return s