package edu.buffalo.cse116;

import java.util.ArrayList;

/**
 * Instances of this class can be used to calculate the sum of negative numbers that were in an ArrayList. This is a
 * silly example, but the straightforward problem provides an excellent first opportunity for students to write AND TEST
 * code.
 *
 * @author Matthew Hertz
 */
public class ListSumNeg {

  /**
   * Create a new instance of this class this does not need to do anything.
   */
  public ListSumNeg() {
  }

  /**
   * Calculate and return the sum of the negative numbers in the list. Only negative numbers should be included in the
   * sum. If there are no negative numbers, your code should return 0.
   *
   * @param list List whose negative elements we wish to sum.
   * @return Sum of the negative numbers in the list or 0 if there is no list/no negative numbers in the list.
   */
  public double sumNegatives(ArrayList<Double> list) {

	  int x = 0;
	  double sum = 0.000;
	  
 	  while(x < list.size()) {
		  if( list.get(x) < 0.000 ) {
			  sum = sum + list.get(x);
		  }
		  x++;
	  }
 	  
	  return sum;	
	  }	
  }