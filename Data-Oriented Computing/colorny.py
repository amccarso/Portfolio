# JR for 463/563

from numpy import *
import pandas
from lxml import etree
use_etree = True

def randomhexcolor( pallor=0.0 ):
	s ='#'
	for i in [1,2,3]:
		r = int( 256*pallor + 256*(1-pallor)*random.rand() )
		s += hex(r)[2:].zfill(2)
	return s

def hexcolor( x, rgb0=[1.,1.,1.], rgb1=[1.,0.,0.] ):
	# create a hexcolor (like #ff00aa) corresponding to scalar x
	# using a linear gradient from rgb0 (for x=0) to rgb1 (for x=1)
	# x a scalar between 0 and 1
	rgb = (1.-x)*array(rgb0) + x*array(rgb1)
	s = '#'
	for element in rgb: s += hex(int(255*element))[2:].zfill(2)
	return s

def colorny( series, rgb0=[1.,1.,1.], rgb1=[1.,0.,0.] ):

	smax = float(series.max())
	indices = set(series.index)
	with open('Map_of_New_York_counties_inkscape.svg','rb') as f:
		bigstring = f.read()
	count = 0

	doc = etree.fromstring( bigstring )
	for p in doc:
		if p.tag == '{http://www.w3.org/2000/svg}polygon' or \
		   p.tag == '{http://www.w3.org/2000/svg}path':
			count += 1
			if p.attrib['id'] != 'New_York_State': 
				if p.attrib['id'] in indices:
					if isnan(series[p.attrib['id']]): 
						#print("NaN seen")
						color = '#ffffff'
					else:
						x = series[p.attrib['id']]/smax
						color = hexcolor(x,rgb0, rgb1)
				else:
					color = '#999999'
			#print p.attrib['id'],x
				p.attrib['style'] ="fill:" + color + \
				 ";stroke:#d0c0a0;stroke-width:1;stroke-opacity:1;fill-opacity:1;stroke-miterlimit:4;stroke-dasharray:none"

	#print 'lxml.etree version',etree.__version__

	with open('myny.svg','w') as f:
		f.write( etree.tostring(doc, pretty_print=True ).decode('utf-8') ) 
	try:
		from IPython.display import SVG
		return SVG('myny.svg')
	except:
		return 'Wrote myny.svg'
	

if __name__ == "__main__":
	print ('hello')
	import pandas
	s = pandas.Series({'Erie':5,'Niagara':1})
	print (s)
	color_new_york_from_series( s )

