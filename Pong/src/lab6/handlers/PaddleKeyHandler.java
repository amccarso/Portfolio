package lab6.handlers;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import lab6.gameobjects.Paddle;

//Austin McCarson, Fall 2014

//Class to detect key press and release, for movement
public class PaddleKeyHandler implements KeyListener {

    //Instantiate variables
	private Paddle _p;
	private char _c;
	private int _v;
	
    //Constructor, c is used to move paddle
	public PaddleKeyHandler(Paddle p, char c, int v) {
		_p = p;
		_c = c;
		_v = v;
	}
	
    //detects what key was pressed
	@Override public void keyTyped(KeyEvent e) {}
    
    //detects key release so paddle stops moving
	@Override public void keyReleased(KeyEvent e) {
		if (e.getKeyChar() == _c) {
			_p.setYVelocity(0);
		}
	}
    
    //Detects what key is pressed
	@Override public void keyPressed(KeyEvent e) {
		if (e.getKeyChar() == _c) {
			_p.setYVelocity(_v);
		}
	}

}
