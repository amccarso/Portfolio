package lab6.gameobjects;

import java.awt.Color;

import engine.drawing.ICanvas;

//Austin McCarson, Fall 2014

//Ball Class
public class Ball extends StandardEntity {

    //Constructor for Ball
	public Ball(int x, int y, int vx, int vy, int diameter, Color c) {
		super(x,y,vx,vy,diameter,diameter,c);
	}

    //Draws ball
	@Override
	public void draw(ICanvas dc) {
		dc.drawFilledCircle(_x, _y, _width, _color);
	}
}
