# John Ringland
# May 5, 2010
# My first python class: for drawing to SVG

# To do: See http://www.w3.org/TR/SVG/coords.html for coordinate transformations
#        See http://www.xml.com/pub/a/2004/04/07/svgtype.html for text alignment

from math import sin, cos, pi

class Sketch:

	def __init__( self, filename, width=800.0, height=800.0 ):
		# open SVG file
		self.f = open( filename, 'w' )
		self.width  =  width  #800.0 #600.0
		self.height =  height #800.0 #600.0
		self.xmin = 0
		self.xmax = self.width
		self.ymin = 0
		self.ymax = self.height
		# write SVG header
		self.f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
		self.f.write('<!-- Created by John Ringland -->\n')
		self.f.write('<svg\n')
		self.f.write('   xmlns:svg="http://www.w3.org/2000/svg"\n')
		self.f.write('   xmlns="http://www.w3.org/2000/svg"\n')
		self.f.write('   version="1.1"\n')
		self.f.write('   width="'  + str(self.width ) + '"\n')
		self.f.write('   height="' + str(self.height) + '"\n')
		self.f.write('   id=\"svg2\">\n')
		# start main group
		self.startGroup( "main_group" )
		self.pad = ''  # What was this for? (Originally 3 spaces.)
		self.textstringno = 0
		self.textanchor = 'left'
		self.textsize = '72px'
		self.textcolor   = '#000000'
		self.textweight  = 'normal'
		self.fontfamily  = 'dejavu,sans'
		self.strokecolor = '#000000'
		self.strokewidth = 2.0
		self.fillcolor   = '#ffff88'
		self.strokeopacity = 1.0
		self.fillopacity   = 1.0
		self.d2r = pi/180.0
		self.fformat = '%.'+str(8)+'f'
		self.nclippedgroups = 0
		self.nclippedpolygons = 0	# maintained to generate unique ids

	def setFrame( self, width, height, xmin, xmax, ymin, ymax ): # superseded
		self.width  = width
		self.height = height
		self.xmin = xmin
		self.xmax = xmax
		self.ymin = ymin
		self.ymax = ymax

	def setFrame( self, xmin, xmax, ymin, ymax ):
		self.xmin = xmin
		self.xmax = xmax
		self.ymin = ymin
		self.ymax = ymax

	def clipPath( self, pathid, path ):
		self.f.write('<defs\nid="defs'+str(pathid)+'">\n')
		self.f.write('<clipPath\nid="clipPath'+str(pathid)+'">\n')
		self.f.write('<path	d="M ')
		for point in path: self.f.write( self.fformat%( self.userToActualX(point[0]) )+','+self.fformat%( self.userToActualY(point[1]) )+' ')
		self.f.write('z"\n')
		self.f.write('id="path'+str(pathid)+'" style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />\n</clipPath>\n</defs>\n')


	def beginClippedGroup( self, clippedgroupid, clippathid ):
		self.nclippedgroups += 1 
		self.f.write('<g\nid="clipped_group'+str(clippedgroupid)+'" ')
		self.f.write('clip-path="url(#clipPath'+str(clippathid)+')">\n')

	def endClippedGroup( self ):
		self.f.write('\n</g>\n')

	def userToActualX( self, x ):
		return ( x - self.xmin )*self.width/( self.xmax - self.xmin )

	def userToActualY( self, y ):
		return ( self.ymax - y )*self.height/( self.ymax - self.ymin )

	def userToActual( self, xy ):
		return ( ( xy[0] - self.xmin )*self.width /( self.xmax - self.xmin ),
                         ( self.ymax - xy[1] )*self.height/( self.ymax - self.ymin ) )

	def userDX( self, actualdx ):
		return actualdx*(self.xmax-self.xmin)/self.width

	def userDY( self, actualdy ):
		return actualdy*(self.ymax-self.ymin)/self.height

	def startGroup( self, groupname ):
		self.f.write( '  <g\n    id="' + groupname + '">\n' )

	def endGroup( self, groupname ):
		self.f.write( "  </g>\n" )

	def close( self ):
		self.endGroup( "main_group" ) 
		self.f.write( "</svg>\n" )
		self.f.close()

	def dot( self, center, radius ):  
		self.f.write(self.pad + '<circle cx="' + self.fformat%( self.userToActualX(center[0]) ) + '" '
                                              + 'cy="' + self.fformat%( self.userToActualY(center[1]) ) + '" '
                                              + 'r="'  + self.fformat%(radius)    + '" '
                                              + 'stroke="' + self.strokecolor    + '" '
                                              + 'stroke-width="' + self.fformat%(self.strokewidth)  + '" '
                                              + 'stroke-opacity="' + self.fformat%(self.strokeopacity)  + '" '
                                              + 'fill="' + self.fillcolor  + '" '
                                              + 'fill-opacity="' + self.fformat%(self.fillopacity)   + '"/>\n')

	def text( self, xy, string ):  
		self.f.write( self.pad + "<text  \n")
		temp = self.pad
		self.pad += "   "
		self.f.write( self.pad + 'x="' + self.fformat%(xy[0]) + '"\n')
		self.f.write( self.pad + 'y="' + self.fformat%(xy[1]) + '"\n')
		self.f.write( self.pad + 'id="text' + self.fformat%(self.textstringno) + '"\n')
		self.textstringno += 1
		self.f.write( self.pad + 'xml:space="preserve" \n')
		self.f.write( self.pad + 'style="text-anchor:'+self.textanchor+';font-size:' + self.textsize + ';' )
		self.f.write(   'font-style:normal;font-weight:'+self.textweight+';')
		self.f.write(   'fill:' + self.textcolor + ';fill-opacity:' + self.fformat%( self.fillopacity ) + ';')
		self.f.write(   'stroke:none;font-family:'+self.fontfamily+'"><tspan\n')
		self.f.write( self.pad + 'x="' + self.fformat%( self.userToActualX(xy[0])) + '"\n')
		self.f.write( self.pad + 'y="' + self.fformat%( self.userToActualY(xy[1])) + '"\n')
		self.f.write( self.pad + 'id="tspan' + self.fformat%(self.textstringno) + '">')
		self.f.write( string )
		self.f.write( '</tspan>\n' )
		self.pad = temp
		self.f.write( self.pad + '</text>\n')

	def setTextColor( self, color ):
		self.textcolor = color

	def setTextBold( self ):
		self.textweight = 'bold'

	def setTextNormal( self ):
		self.textweight = 'normal'

	def setTextJustifyLeft( self ):
		self.textanchor = 'start'

	def setTextJustifyMiddle( self ):
		self.textanchor = 'middle'

	def setTextJustifyRight( self ):
		self.textanchor = 'end'

	def setTextSize( self, sizestring ):
		self.textsize = sizestring

	def setStrokeColor( self, color ):
		self.strokecolor = color

	def setFillColor( self, color ):
		self.fillcolor = color

	def setStrokeWidth( self, width ):
		self.strokewidth = width

	def getStrokeWidth( self ):
		return self.strokewidth

	def setStrokeOpacity( self, opacity ):
		self.strokeopacity = opacity

	def getStrokeOpacity( self ):
		return self.strokeopacity

	def setFillOpacity( self, opacity ):
		self.fillopacity = opacity

	def getFillOpacity( self ):
		return self.fillopacity

	def line( self, p1, p2 ):
		self.f.write( self.pad + '<line '
                             + 'x1="' + self.fformat%( self.userToActualX( p1[0] ) ) + '" ' 
                             + 'y1="' + self.fformat%( self.userToActualY( p1[1] ) ) + '" ' 
                             + 'x2="' + self.fformat%( self.userToActualX( p2[0] ) ) + '" ' 
                             + 'y2="' + self.fformat%( self.userToActualY( p2[1] ) ) + '" ' 
                             + 'stroke="' + self.strokecolor    + '" '
                             + 'stroke-width="' + self.fformat%(self.strokewidth)  + '" '
                             + 'stroke-opacity="' + self.fformat%(self.strokeopacity)  + '" '
                             + '/>\n')

	def circularArc( self, center, r, theta0, theta1): # added October 9, 2011  # Was this ever tested? 3/7/14
		p0 = [center[0]+r*cos(theta0*self.d2r),center[1]+r*sin(theta0*self.d2r)]
		p1 = [center[0]+r*cos(theta1*self.d2r),center[1]+r*sin(theta1*self.d2r)]
		rx = self.userToActualX( r ) - self.userToActualX( 0 )
		ry = self.userToActualY( 0 ) - self.userToActualY( r )
		largeArcFlag = 0
		if abs(theta0-theta1)*self.d2r > pi:
			largeArcFlag = 1
		self.f.write( self.pad + '<path d=" '
                             + 'M ' 
                             + self.fformat%( self.userToActualX( p0[0] ) ) + ',' 
                             + self.fformat%( self.userToActualY( p0[1] ) ) 
                             + ' A ' + self.fformat%(rx) + ',' + self.fformat%(ry) + ' 0 '
                             + self.fformat%(largeArcFlag)
                             + ',0 ' 
                             + self.fformat%( self.userToActualX( p1[0] ) ) + ',' 
                             + self.fformat%( self.userToActualY( p1[1] ) ) + '" '
                             + 'fill="none" '
#                             + 'fill="' + self.fillcolor    + '" '
#                             + 'fill-opacity="' + self.fformat%(self.strokeopacity)  + '" '
                             + 'stroke="' + self.strokecolor    + '" '
                             + 'stroke-width="' + self.fformat%(self.strokewidth)  + '" '
                             + 'stroke-opacity="' + self.fformat%(self.strokeopacity)  + '" '
                             + '/>\n')

	def polyline( self, pointarray ):
		mystr = self.pad + '<polyline points="'
		for i in range(0,len(pointarray)):
			mystr += (  self.fformat%( self.userToActualX( pointarray[i][0] ) )
                                  + ','  
                                  + self.fformat%( self.userToActualY( pointarray[i][1] ) )
                                  + ' '
                                 )
		mystr += '" \n'
		self.f.write( mystr )
		self.f.write( self.pad 
                             + 'fill="none" ' 
                             + 'stroke="' + self.strokecolor    + '" '
                             + 'stroke-width="' + self.fformat%(self.strokewidth)  + '" '
                             + 'stroke-opacity="' + self.fformat%(self.strokeopacity)  + '" '
                             + '/>\n')

	def polygon( self, pointarray ):
		mystr = self.pad + '<polygon points="'
		for i in range(0,len(pointarray)):
			mystr += (  self.fformat%( self.userToActualX( pointarray[i][0] ) )
                                  + ','  
                                  + self.fformat%( self.userToActualY( pointarray[i][1] ) )
                                  + ' '
                                 )
		mystr += '" \n'
		self.f.write( mystr )
		self.f.write( self.pad 
                             + 'fill="' + self.fillcolor  + '" '
                             + 'fill-opacity="' + self.fformat%(self.fillopacity)   + '" '
							 + 'stroke="' + self.strokecolor    + '" '
                             + 'stroke-width="' + self.fformat%(self.strokewidth)  + '" '
                             + 'stroke-opacity="' + self.fformat%(self.strokeopacity)  + '" '
                             + '/>\n')

	def clippedPolygon( self, pointarray, groupprefix='' ):	# use polygon itself as clipping path to mask exterior part of stroke
		self.nclippedpolygons += 1 
		self.f.write('<defs\nid="defsPoly'+groupprefix+str(self.nclippedpolygons)+'">\n')
		self.f.write('<clipPath\nid="clipPathPoly'+groupprefix+str(self.nclippedpolygons)+'">\n')
		self.f.write('<path	d="M ')
		for point in pointarray: self.f.write( self.fformat%( self.userToActualX(point[0]) )+','+self.fformat%( self.userToActualY(point[1]) )+' ')
		self.f.write('z"\n')
		self.f.write('id="cppath'+groupprefix+str(self.nclippedpolygons)+'" style="fill:none;stroke:#000000;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" />\n</clipPath>\n</defs>\n')
		self.f.write('<g\nid="clippedPolygon'+groupprefix+str(self.nclippedpolygons)+'" ')
		self.f.write('clip-path="url(#clipPathPoly'+groupprefix+str(self.nclippedpolygons)+')">\n')

		mystr = self.pad + '<polyline points="'
		for i in range(0,len(pointarray)):
			mystr += (  self.fformat%( self.userToActualX( pointarray[i][0] ) )
                                  + ','  
                                  + self.fformat%( self.userToActualY( pointarray[i][1] ) )
                                  + ' '
                                 )
		mystr += (  self.fformat%( self.userToActualX( pointarray[0][0] ) ) # append first point to close
                                  + ','  
                                  + self.fformat%( self.userToActualY( pointarray[0][1] ) )
                                  + ' '
                                 )
		mystr += '" \n'
		self.f.write( mystr )
		self.f.write( self.pad 
                             + 'fill="' + self.fillcolor  + '" '
                             + 'fill-opacity="' + self.fformat%(self.fillopacity)   + '" '
							 + 'stroke="' + self.strokecolor    + '" '
                             + 'stroke-width="' + self.fformat%(self.strokewidth)  + '" '
                             + 'stroke-opacity="' + self.fformat%(self.strokeopacity)  + '" '
                             + '/>\n')
		self.f.write('\n</g>\n')

	def setPrecision( self, ndigits ):
		self.fformat = '%.'+str(ndigits)+'f'

	def getPrecision( self ):
		return int(self.fformat[2:][:-1])
	
	def comment( self, textstring ):
		self.f.write('\n<!-- '+textstring+' -->\n')

