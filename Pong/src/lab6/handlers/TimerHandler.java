package lab6.handlers;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import engine.Game;

//Austin McCarson, Fall 2014

//Class for updates in game
public class TimerHandler implements ActionListener{

    //Instantiate game variable
	private Game _g;

    //Constructor
	public TimerHandler(Game g) {
		_g = g;
	}
	
    //detects when an action is performed(collision, movement)
	@Override public void actionPerformed(ActionEvent e) {
		// ORDER IS IMPORTANT
		_g.updateEntities();
		_g.checkCollision();
		_g.draw();
	}

}
