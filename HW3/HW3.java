package JavaTemplate.src;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class HW3 {

	public class Figure {
		
		private int Id;
		private double Value;
		
		Figure () {}
		
		Figure (int id, double value) {
			Id = id;
			Value = value;
		}
		
		public double getValue () {
			return Value;
		}
		
		public void setValue (double value) {
			Value = value;
		}
		
		public int getId () {
			return Id;
		}
		
		public void setId (int id) {
			Id = id;
		}
		
	}
	

		
		public static Figure compare(Figure o1, Figure o2) {
		
			return o1.getValue() - o2.getValue() > 0 ? o1 : o2;
		}
	
		 
	
	public static void main (String[] args) {
		
		String inputFilename = args[0];
        String outputFilename = args[1];
        
        String id, value;
        HW3 hw3 = new HW3();
        ArrayList<Figure> figures = new ArrayList<Figure>();
       
        
        
		try {
        	Scanner scanner = new Scanner(new File(inputFilename));
            scanner.useDelimiter(",|\\n");
            while ( scanner.hasNext() ) {
                Figure figure = hw3.new Figure();
                id = "";
                value = "";
                id = scanner.next();
                figure.setId(Integer.parseInt(id));
                value = scanner.next();
                figure.setValue(Double.parseDouble(value));
                figures.add(figure);
            }
            scanner.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
		int n = figures.size();
		double[] maxValue =  new double[n];
		maxValue[0] = 0;
		maxValue[1] = figures.get(1).getValue();
		maxValue[2] = max(figures.get(1).getValue(), figures.get(2).getValue());
		for ( int i = n-1; i > 2; i-- ) {
			maxValue[i] = max( maxValue[i-1], maxValue[i-3] + figures.get(i).getValue() );
		}

		int i = n-1;
		
		List<Figure> purchases = new ArrayList<Figure>();
		
		while ( i > 2 ) {
			if ( maxValue[i-3] + figures.get(i).getValue() > maxValue[i-1] ) {
				purchases.add(figures.get(i));
				i-=2;
			}
			else { i--; }
		}
		
		Collections.reverse(purchases);
		
		try {
    			PrintWriter writer = new PrintWriter(outputFilename, "UTF-8");
    			i = 0;
    			while ( i < purchases.size() ) {
    					writer.println(purchases.get(i).getId());
    					i++;
    			}
    			writer.close();
		}
		catch (IOException e) {
    			e.printStackTrace();
		}
		
	}

	private static double max(double d, double e) {
		// TODO Auto-generated method stub
		return d > e ? d : e;
	}
}
