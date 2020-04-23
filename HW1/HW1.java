package JavaTemplate.src;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Iterator;

public class HW1{
	
    public static void main(String[] args){
        String inputFilename = args[0];
        String outputFilename = args[1];

        
        int a=0;
        int b=0;
        try {
			Iterator<String> lines = Files.readAllLines(Paths.get(inputFilename)).iterator();
			a = new Integer(lines.next());
			b = new Integer(lines.next());
		} catch (IOException e) {
			e.printStackTrace();
		}
        
        int ans = 1;
        
        while ( b > 0 ) {
        		if ( b%2 == 1 ) {	//odd powers (odd b)
        			ans *= a;		//multiply (essentially "nullifies" odd to proceed as if even power)
        		}
        	a *= a; //repeating squares
        	b /= 2; //divide by 2
        }
        
        try {
        	String data = ans+"";
        	Files.write(Paths.get(outputFilename), data.getBytes());
		} catch (IOException e) {
			e.printStackTrace();
		}
        
    }

}
