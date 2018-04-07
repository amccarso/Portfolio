package lab6.gameobjects;

import java.awt.Color;

import lab6.Pong;
import engine.drawing.ICanvas;

//Austin McCarson, Fall 2014

//Paddle class, two paddles in game
public class Paddle extends StandardEntity {

    //Constructor
	public Paddle(int x, int y, int w, int h, Color c) {
		super(x,y,w,h,0,0,c);
	}

    //draw and create paddles
	@Override public void draw(ICanvas dc) {
		dc.drawFilledRectangle(_x, _y, _width, _height, _color );
	}
	
    //Does not move left or right, does not need xvelocity
	@Override public void setXVelocity(int xVelocity) {
		
	}
	
    //update position of paddle(moves up and down)
	@Override public void update() {
		super.update();
		if (_y < 1) { _y = 1; }  // '1' is for wall thickness
		if ((_y+ _height) > (Pong.GAME_HEIGHT - 1)) { _y = (Pong.GAME_HEIGHT - 1 - _height); } 
	}
}
