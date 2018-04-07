package lab6.handlers;

import engine.Entity;
import engine.collision.CollisionListener;

//Austin McCarson, Fall 2014

//Class to flip direction of ball when it collides w/ paddle
public class HorizontalBounceListener implements CollisionListener {

    //flips direction of ball
	@Override public void collisionOccurred(Entity e) {
		e.setXVelocity(-e.getXVelocity());
	}

}
