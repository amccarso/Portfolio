package JavaTemplate.src;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class HW4 {
	
	public class Line {
		private int _Id;
		private double _slope, _intercept, _x;
		
		public Line (int id, double slope, double intercept ) {
			_Id = id;
			_slope = slope;
			_intercept = intercept;
		}
		public Line() {
			// TODO Auto-generated constructor stub
		}
		public double ComputeX ( double intercept, double slope ) {
			
			_x = (intercept - _intercept)/(_slope - slope);
			
			return _x;
		}
		
		public double getX () {
			return _x;
		}
		
		public double getSlope () {
			return _slope;
		}
		
		public double getIntercept () {
			return _intercept;
		}
		
		public int getId () {
			return _Id;
		}
		
		public boolean isSlopePositive () {
			return _slope >= 0 ? true : false;
		}
		
		public double absValofSlope () {
			return _slope >= 0 ? _slope : _slope*-1.0;
		}
		
	}
	
	static void merge ( List<Line> left, List<Line> right, List<Line> lines) {

		int leftIndex = 0;
	    int rightIndex = 0;
	    int wholeIndex = 0;
	 
	    while ( leftIndex < left.size()-1 && rightIndex < right.size()-1 ) {
	    	
	    	Line lineFromLeft = left.get(leftIndex);
	    	Line lineFromRight = right.get(rightIndex);
	    	Line lineToCompare = left.get(leftIndex+1);
	    	
	        if ( lineFromLeft.isSlopePositive() == lineFromRight.isSlopePositive() ) {
	        		if ( left.get(leftIndex).absValofSlope() > right.get(rightIndex).absValofSlope() ) {
	        			if ( lineFromLeft.ComputeX (lineToCompare.getIntercept(), lineToCompare.getSlope()) 
	        			   > lineFromRight.ComputeX (lineToCompare.getIntercept(), lineToCompare.getSlope()) ) {
	        				lines.set(wholeIndex, lineFromLeft);
	        				wholeIndex++;
	        				leftIndex++;
	        			} else {
	        				wholeIndex++;
	        				rightIndex++;
	        			}
	        		} else if ( left.get(leftIndex).absValofSlope() > right.get(rightIndex).absValofSlope() ){ 
	        			if ( leftIndex > rightIndex ) {
	        				lines.set(wholeIndex, lineFromRight);
	        				wholeIndex++;
	        				lines.set(wholeIndex, lineFromLeft);
	        				rightIndex++;
	        			} else {
	        				leftIndex++;
	        			}
	        		}
	        } else {
	        		if ( leftIndex > rightIndex ) {
	        			rightIndex++;
	        		} else { leftIndex++; }
	        }
	    }
    }

	public static List<Line> mergeSort ( List<Line> lines ) {

		List<Line> left = new ArrayList<Line>();
	    List<Line> right = new ArrayList<Line>();
	    int center;
	 
	    if (lines.size() <= 2) {    
	        return lines;
	    } else {
	        center = lines.size()/2;
	        for (int i=0; i<center; i++) {
	                left.add(lines.get(i));
	        }
	 
	        for (int i=center; i<lines.size(); i++) {
	                right.add(lines.get(i));
	        }
	 
	        left  = mergeSort(left);
	        right = mergeSort(right);
	 
	        merge(left, right, lines);
	    }
	    
	    return lines;

    }

	public static void main (String args[]) {
		String input = args[0];
		String output =  args[1];
		
		List<Line> lines = new ArrayList<Line>();
		List<Line> visible = new ArrayList<Line>();
		HW4 hw4 = new HW4();
		try {
			Scanner scanner = new Scanner(new File(input));
			scanner.useDelimiter(",|\\n");
			while ( scanner.hasNext() ) {
				Line line = hw4.new Line(scanner.nextInt(), scanner.nextDouble(), scanner.nextDouble());
				lines.add(line);
			}
			scanner.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		mergeSort(lines);
		
		try {
			PrintWriter writer = new PrintWriter(output, "UTF-8");
			for ( Line line : visible ) {
				writer.println(line.getId());
			}
			writer.close();
		} catch ( IOException e ) {
			
		}
	}
}
