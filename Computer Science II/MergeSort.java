package edu.buffalo.cse116;

import java.util.ArrayList;
import java.util.List;

/** Instances of this class can be used to guarantee a list is sorted using the merge sort algorithm. */
@SuppressWarnings("unchecked")
public class MergeSort<E extends Comparable<E>> {
  /**
   * Performs merge sort on the list of data. While this is recursive, we only need a single public method to do all the
   * work.
   *
   * @param list List of data to be sorted by this call
   * @return List in which all of the elements have been ordered from smallest to largest
   */
  public List<E> sort(List<E> list) {
    // Base case: we have 0 or 1 element to sort
    if (list.size() < 2) {
      return list;
    }
    // Recursive step

    // Partition the data
    List<E>[] subLists = partition(list);
    // Recurse!
    subLists[0] = sort(subLists[0]);
    subLists[1] = sort(subLists[1]);

    // Combine the data
    List<E> merged = merge(subLists[0], subLists[1]);
    // No combine step needed!
    return merged;
  }

  /**
   * This is a helper method which splits the list into two halves as appropriate for merge sort.
   *
   * @param list Data to be split into two separate Lists
   * @return An array with the two lists after the partitioning.
   */
  private List<E>[] partition(List<E> list) {
    List<E>[] retVal = new List[2];
    retVal[0] = new ArrayList<E>();
    retVal[1] = new ArrayList<E>();
    int size = list.size();
    for (int i = 0; i < size / 2; i++) {
      E elem = list.remove(0);
      retVal[0].add(elem);
    }
    while (!list.isEmpty()) {
      E elem = list.remove(0);
      retVal[1].add(elem);
    }
    return retVal;
  }

  /**
   * This is the helper method that merges the two sublists into a single, sorted list.
   *
   * @param list1 First half of the data to be recombined into a single list
   * @param list2 Second half of the data to be recombined into a single list
   * @return New List instance containing the two merged lists.
   */
  private List<E> merge(List<E> list1, List<E> list2) {
    
	  List<E> retVal = new ArrayList<E>();

	  while ( !list1.isEmpty() && !list2.isEmpty() ) {
		  if ( list1.get(0).compareTo(list2.get(0)) < 0 ) {
			  retVal.add(list1.remove(0));
		  } else {
			  retVal.add(list2.remove(0));
		  }
	  }
	  
	  while ( !list1.isEmpty() ) {
		  retVal.add(list1.remove(0));
	  }
	  
	  while ( !list2.isEmpty() ) {
		  retVal.add(list2.remove(0));
	  }
	  
	  return retVal;
  }
}