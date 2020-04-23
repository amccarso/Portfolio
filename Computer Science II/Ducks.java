package edu.buffalo.cse116;

/**
 * Class that is used to print out the lyrics to "5 little ducks"
 *
 * @author Matthew Hertz
 */
public class Ducks {
	
	public static void main (String[] args) {
		
	int duckies = 5;
	
	
	while ( duckies > 0 ) {
		
		if ( duckies != 1 ) {
			System.out.println(duckies + " little ducks went swimming one day,");
		} 
		else { System.out.println("1 little duck went swimming one day,"); }
		
		duckies--;
		
		System.out.println("Over the hill and far away");
		System.out.println("Mamma duck said: 'Quack, quack, quack, quack!'");
		
		if ( duckies > 1 ) { 
			System.out.println("And only " + duckies + " little ducks came back.");
		}
		else if ( duckies == 1 ) {
			System.out.println("And only 1 little duck came back.");
		}
		else {
			System.out.println("And all her little ducks came back.");
		}
	}
	}
		
}

