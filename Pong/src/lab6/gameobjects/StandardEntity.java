package lab6.gameobjects;

import java.awt.Color;
import java.awt.Rectangle;
import java.util.ArrayList;

import engine.Entity;
import engine.collision.CollisionListener;
import engine.drawing.ICanvas;

//Austin McCarson, Fall 2014

//Parent class for ball and paddles
public abstract class StandardEntity implements Entity {

    //Instantiate variables
	private ArrayList<CollisionListener> _listeners;
	protected int _x;
	protected int _y;
	protected int _vy;
	protected int _vx;
	protected int _width;
	protected int _height;
	protected Color _color;

    //Constructor
	public StandardEntity(int x, int y, int w, int h, int vx, int vy, Color c) {
		super();
		_x = x;
		_y = y;
		_width = w;
		_height = h;
		_vx = vx;
		_vy = vy;
		_color = c;
		_listeners = new ArrayList<CollisionListener>();
	}

    //gets rectangle for paddles
	@Override
	public Rectangle getRect() {
		return new Rectangle(_x, _y, _width, _height);
	}

    //get and set attributes
	@Override public int getXCoordinate() { return _x; }
	@Override public int getYCoordinate() { return _y; }
	@Override public void setXCoordinate(int c) { _x = c; }
	@Override public void setYCoordinate(int c) { _y = c; }
	@Override public int getXVelocity() { return _vx; }
	@Override public int getYVelocity() { return _vy; }
	@Override public void setXVelocity(int xVelocity) { _vx = xVelocity; }
	@Override public void setYVelocity(int yVelocity) { _vy = yVelocity; }
	@Override public Color getColor() { return _color; }
	@Override public void setColor(Color c) { _color = c; }
	@Override public int getWidth() { return _width; }
	@Override public int getHeight() { return _height; }
	@Override public void setWidth(int x) { _width = x; }
	@Override public void setHeight(int x) { _height = x; }



    //Tells when collision occurs between objects(ball and paddle)
	@Override
	public void fireCollisionOccurred(Entity e) {
		for (CollisionListener cl : _listeners) {
			cl.collisionOccurred(e);
		}
	}

    //creates a collision listener
	@Override
	public void addCollisionListener(CollisionListener cl) {
		_listeners.add(cl);
	}

    //Removes collision listener
	@Override
	public void removeCollisionListener(CollisionListener cl) {
		_listeners.remove(cl);
	}

    //draws object
	@Override public abstract void draw(ICanvas dc);

    //updates coordinates of object
	@Override
	public void update() {
		// Basic implementation - subclasses may wish to partially override
		_x = _x + _vx;
		_y = _y + _vy;
	}

}
