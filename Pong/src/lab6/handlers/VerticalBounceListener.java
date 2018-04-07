package lab6.handlers;

import engine.Entity;
import engine.collision.CollisionListener;

//Austin McCarson, Fall 2014

//Class to detect if ball hits bottom wall
public class VerticalBounceListener implements CollisionListener {

    //reverses y direction of ball
	@Override public void collisionOccurred(Entity e) {
		e.setYVelocity(-e.getYVelocity());
	}

}
