package edu.buffalo.cse116;

/**
 * Class that defines a method which performs matrix addition. This gives students their first practice at creating and using
 * the code needed for higher dimensional arrays.
 *
 * @author Matthew Hertz
 */
public class MatrixAddition {

  /**
   * Given two equally-sized matrices, return a newly allocated matrix containing the result of adding the two.<br/>
   * Precondition: a &amp; b must have the same number of rows and each row will have the same number of columns. You should
   * assume preconditions hold and can write your code knowing this is always be true.
   *
   * @param a The first matrix we will be adding
   * @param b The second matrix whose entries will be added
   * @return Newly allocated array whose entries are equal to the sum of the entries in a &amp; b
   * at the identical row and column.
   */
  public int[][] add(int[][] a, int[][] b) {
	  
	  int [][] retArr;
	  
	  if(a.length == 0) {
		  retArr = new int[0][0];
		  return retArr;
	  }
	  
	  int size = a.length;
	  int length = a[0].length;
	  
	  retArr = new int[size][length];
	  for (int i = 0; i < size; i++) {
		  for (int j = 0; j < length; j++) {
			  retArr[i][j] = a[i][j] + b[i][j];
		  }
	  }
	  return retArr;
  }
}