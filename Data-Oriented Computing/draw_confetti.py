import SVGSketch
from os.path import join, exists, basename
import numpy as np
from randomhexcolor import randomhexcolor
import os
import sys
from cairosvg import svg2png  # not needed if using Inkscape to render svg to png
USE_INKSCAPE = False

prefix       = sys.argv[1]
minsides = int(sys.argv[2])
maxsides = int(sys.argv[3])
nimages  = int(sys.argv[4])

def drawsvg(npolygons,nv):
	w,h = 150,100
	sk = SVGSketch.Sketch('temp.svg',w,h)
	sk.setFrame(0,w,0,h)
	sk.setStrokeWidth(0)

	# fill whole image with background color
	sk.setFillColor('#e0e0e0')
	sk.polygon( [(0,0),(w,0),(w,h),(0,h)] )
	sk.setFillColor('#ff88ff')

	rfac = np.sqrt( 2/(nv*np.sin(2*np.pi/nv)) )  # this is to make the area of the polygon independent of nv

	R = min(w,h)/3

	for ip in range(npolygons):
			x0,y0 = np.random.rand( 2 )*[w,h]
			r = rfac*np.random.rand(  )*R
			t0 = np.random.rand()*2*np.pi
			polygon = [np.array((x0+r*np.cos(t0+t), y0+r*np.sin(t0+t))) for t in np.linspace(0,2*np.pi,nv,endpoint=False)] 
			sk.setFillColor(randomhexcolor(pallor=0.5))
			sk.polygon(polygon)

	sk.close()


folder = prefix
if not exists(folder):
	os.makedirs(folder)
else: 
	os.system( 'rm ' + join( folder, '*.png' ) )

txt = open( join( folder, prefix + '.txt'), 'w' )
print('npolygons nv',file=txt)
html = open( join( folder, prefix + '.html'), 'w' )

for i in range(nimages):
	#print(i+1,'of',nimages)
	npolygons = np.random.randint(0,51)
	nv = np.random.randint(minsides,maxsides+1)
	drawsvg( npolygons, nv )
	pngname = join(folder,str(i).zfill(4) + '_' + str(npolygons).zfill(3) + '_' + str(nv).zfill(3) + '.png')
	print( npolygons,nv, file=txt )
	print( '<img src=' + basename(pngname) + '>', file=html )

	if USE_INKSCAPE:
		cmd = 'inkscape -d 48 -e ' + pngname + ' temp.svg' 
		print(cmd)
		os.system(cmd)
	else:
		with open('temp.svg') as f:
			svgtext = f.read()
		print('svg2png',pngname)
		svg2png(bytestring=svgtext,write_to=pngname)

#os.system('rm temp.svg')
txt.close()
html.close()
