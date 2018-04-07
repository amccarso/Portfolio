package lab6.gameobjects;

import java.awt.Color;

import engine.drawing.ICanvas;

//Austin McCarson, Fall 2014

//Wall class, not visible to player
public class Wall extends StandardEntity {
		
    //Constructor
	public Wall(int x, int y, int w, int h, Color c) {
		super(x,y,w,h,0,0,c);
	}
	
    //creates wall in window
	@Override public void draw(ICanvas dc) {
		dc.drawFilledRectangle(_x, _y, _width, _height, _color);
	}
	
    //does not move, does not need to be updated
	@Override
	public void update() {
	}

}
