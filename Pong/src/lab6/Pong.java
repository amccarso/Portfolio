package lab6;

import java.awt.Color;

import javax.swing.Timer;

import lab6.gameobjects.Ball;
import lab6.gameobjects.Paddle;
import lab6.gameobjects.Wall;
import lab6.handlers.AnnounceWinnerListener;
import lab6.handlers.HorizontalBounceListener;
import lab6.handlers.PaddleKeyHandler;
import lab6.handlers.TimerHandler;
import lab6.handlers.VerticalBounceListener;
import engine.Game;

//Austin McCarson, Fall 2014

//Class to simulate game
public class Pong {
	private static final int WALL_PADDLE_WIDTH = 10;
	public static final int GAME_WIDTH = 800;
	public static final int GAME_HEIGHT = 400;
	
	public Pong() {
        
        //Instantiate game
		Game g = new Game(GAME_WIDTH, GAME_HEIGHT);
		g.setBackgroundColor(Color.BLACK);
	
        //Create walls(boundaries for the game)
		Wall north = new Wall(0, 0, GAME_WIDTH, WALL_PADDLE_WIDTH, Color.BLACK);
		Wall south = new Wall(0, GAME_HEIGHT-WALL_PADDLE_WIDTH, GAME_WIDTH, WALL_PADDLE_WIDTH, Color.BLACK);
		Wall west = new Wall(0, WALL_PADDLE_WIDTH, WALL_PADDLE_WIDTH, GAME_HEIGHT-2*WALL_PADDLE_WIDTH, Color.BLUE);
        Wall east = new Wall(GAME_WIDTH-WALL_PADDLE_WIDTH, WALL_PADDLE_WIDTH, WALL_PADDLE_WIDTH, GAME_HEIGHT-2*WALL_PADDLE_WIDTH, Color.GREEN);
        
        //Create two paddles
		Paddle p1 = new Paddle(4*WALL_PADDLE_WIDTH, GAME_HEIGHT/2-2*WALL_PADDLE_WIDTH, WALL_PADDLE_WIDTH, 4*WALL_PADDLE_WIDTH, Color.BLUE);
		Paddle p2 = new Paddle(GAME_WIDTH - 5*WALL_PADDLE_WIDTH, GAME_HEIGHT/2-2*WALL_PADDLE_WIDTH, WALL_PADDLE_WIDTH, 4*WALL_PADDLE_WIDTH, Color.GREEN);
        
        //Create ball
		Ball b = new Ball(GAME_WIDTH/2, GAME_HEIGHT/2, 2, 2, 6, Color.YELLOW);

        //Create collision listeners for walls
		north.addCollisionListener(new VerticalBounceListener());
		south.addCollisionListener(new VerticalBounceListener());
		west.addCollisionListener(new AnnounceWinnerListener(2));
		east.addCollisionListener(new AnnounceWinnerListener(1));
        
        //collision listener for paddle 1
		p1.addCollisionListener(new HorizontalBounceListener());
        
        //key listener for player 1(paddle 1), a moves paddle up, z down
		g.addKeyListener(new PaddleKeyHandler(p1,'a',-4));
		g.addKeyListener(new PaddleKeyHandler(p1,'z',+4));
        
        //collision listener for paddle 2
		p2.addCollisionListener(new HorizontalBounceListener());
        
        //key listener for player 2(paddle 2), k moves paddle up, m down
		g.addKeyListener(new PaddleKeyHandler(p2,'k',-4));
		g.addKeyListener(new PaddleKeyHandler(p2,'m',+4));

        //add walls to game
		g.addEntity(north);
		g.addEntity(west);
		g.addEntity(east);
		g.addEntity(south);
        
        //add paddles and ball to game
		g.addEntity(p1);
		g.addEntity(p2);
		g.addEntity(b);
		
        //game updates every 20 seconds
		Timer t = new Timer(20, new TimerHandler(g));
		t.start();	
	}
}
