package edu.buffalo.cse116;

import java.util.ArrayList;

public class QuickSelect {

  /**
   * Method implementing the recursive quick select algorithm which returns the nth largest item in a list in linear
   * time.<br/>
   * Pre-requisite: list is not null AND n is between 0 and list.size() - 1
   *
   * @param list List of data whose element is wanted
   * @param n Sorted ordering of the item were the list actually sorts. When this is 0 the smallest item is returned;
   *          when this is 5 the 6th smallest item is returned; when this is the size of {@code list}-1, the largest
   *          item is returned.
   * @return {@code n}th smallest item in {@code list}
   */
  public static int quickSelect(ArrayList<Integer> list, int n) {

	  return quickSelect(list, 0, list.size()-1, n);
  }

  private static int quickSelect(ArrayList<Integer> list, int firstIdx, int lastIdx, int n) {
	  
	  int pivotIdx = QuickSelectHelper.partition(list, firstIdx, lastIdx);
	  
	  if (n == pivotIdx) {
		  return list.get(pivotIdx);
	  } else if (n < pivotIdx) {
		  return quickSelect(list, firstIdx, pivotIdx-1, n);
	  } else {
		  return quickSelect(list, pivotIdx+1, lastIdx, n);
	  }
	  
  }
}