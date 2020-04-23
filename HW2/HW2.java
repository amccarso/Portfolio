
import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class HW2 {

	public class Player {

		private int Id;
		private double MarioTime, DoomTime;


		public Player() {}

	    public Player ( int id, double marioTime, double doomTime) {
	        Id = id;
	        MarioTime = marioTime;
	        DoomTime = doomTime;
	    }

	    public double getDoomTime () {
	        return DoomTime;
	    }

	    public void setDoomTime ( double doomtime ) {
	        DoomTime = doomtime;
	    }

	    public int getId () {
	        return Id;
	    }

	    public void setId ( int id ) {
	        Id = id;
	    }

	    public double getMarioTime () {
	        return MarioTime;
	    }

	    public void setMarioTime ( double mariotime ) {
	        MarioTime = mariotime;
	    }
	}
	
	static void merge ( ArrayList<Player> left, ArrayList<Player> right, ArrayList<Player> players) {

		int leftIndex = 0;
	    int rightIndex = 0;
	    int wholeIndex = 0;
	 
	    while (leftIndex < left.size() && rightIndex < right.size()) {
	        if ( left.get(leftIndex).getDoomTime() >= right.get(rightIndex).getDoomTime() ) {
	            players.set(wholeIndex, left.get(leftIndex));
	            leftIndex++;
	        } else {
	            players.set(wholeIndex, right.get(rightIndex));
	            rightIndex++;
	        }
	        wholeIndex++;
	    }
	 
	    ArrayList<Player> rest;
	    int restIndex;
	    if (leftIndex >= left.size()) {
	        rest = right;
	        restIndex = rightIndex;
	    } else {
	        rest = left;
	        restIndex = leftIndex;
	    }
	 
	    for (int i=restIndex; i<rest.size(); i++) {
	        players.set(wholeIndex, rest.get(i));
	        wholeIndex++;
	    }

    }


	public static ArrayList<Player> mergeSort ( ArrayList<Player> players ) {

		ArrayList<Player> left = new ArrayList<Player>();
	    ArrayList<Player> right = new ArrayList<Player>();
	    int center;
	 
	    if (players.size() == 1) {    
	        return players;
	    } else {
	        center = players.size()/2;
	        for (int i=0; i<center; i++) {
	                left.add(players.get(i));
	        }
	 
	        for (int i=center; i<players.size(); i++) {
	                right.add(players.get(i));
	        }
	 
	        left  = mergeSort(left);
	        right = mergeSort(right);
	 
	        merge(left, right, players);
	    }
	    return players;

    }
	
	public static void main(String[] args){
        String inputFilename = args[0];
        String outputFilename = args[1];

        
        String id, mariotime, doomtime;
        HW2 hw2 = new HW2();
        ArrayList<Player> players = new ArrayList<Player>();
        try {
        	Scanner scanner = new Scanner(new File(inputFilename));
            scanner.useDelimiter(",|\\n");
            while ( scanner.hasNext() ) {
                Player player = hw2.new Player(scanner.nextInt(), scanner.nextDouble(), scanner.nextDouble());
                players.add(player);
            }
            scanner.close();
		} catch (IOException e) {
			e.printStackTrace();
		}

        
        
        //mergesort vector
        mergeSort(players);
        
        
        try {
        		PrintWriter writer = new PrintWriter(outputFilename, "UTF-8");
        		int i = 0;
        		while ( i < players.size() ) {
        		writer.println(players.get(i).getId());
        		i++;
        		}
        		writer.close();
        }
        catch (IOException e) {
        		e.printStackTrace();
        }
	}
}
