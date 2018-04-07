package lab6.handlers;

import engine.Entity;
import engine.collision.CollisionListener;

//Class to announce winner when ball hits wall
public class AnnounceWinnerListener implements CollisionListener {
	
	private int _winner;
	
    //set winner
	public AnnounceWinnerListener(int w) {
		_winner = w;
	}

    //Announce winner
	@Override public void collisionOccurred(Entity e) {
		System.out.println("Player #"+_winner+" wins!");
		System.exit(0);
	}

}
