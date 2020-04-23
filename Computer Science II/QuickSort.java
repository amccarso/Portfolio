package edu.buffalo.cse116;

import java.util.List;

/** Instances of this class can be used to guarantee a list is sorted using the quick sort algorithm. */
public class QuickSort<E extends Comparable<E>> {
  /**
   * Starts the quick sort algorithm and returns the sorted list.
   *
   * @return List of data that has been ordered from smallest to largest
   */
  public List<E> sort(List<E> list) {
    return sort(list, 0, list.size() - 1);
  }

  /**
   * Performs quick sort on the list of data for the elements at indices from {@code lo} through {@code high},
   * inclusive. This is the private method of the recursion where all the work gets done.
   *
   * @param lo First index in {@code list} that this call will be working with
   * @param high Last index in {@code list} whose element this call will sort.
   * @return The list in which the elements from {@code lo} through {@code high} have been ordered from smallest to
   *         largest
   */
  private List<E> sort(List<E> list, int lo, int high) {
    // Base case: we have 0 or 1 element to sort
    if (lo >= high) {
      return list;
    }
    // Recursive step

    // Chose the pivot
    int pivotIdx = (lo + high) / 2;
    // Partition the data
    pivotIdx = partition(list, pivotIdx, lo, high);
    // Recurse!
    sort(list, lo, pivotIdx - 1);
    sort(list, pivotIdx + 1, high);
    // No combine step needed!
    return list;
  }

  /**
   * This is a helper method which partition the list into left and right parts. The left part of the list will contain
   * all of the values smaller than the pivot. The right part of the array list will contain all of the values larger
   * than the pivot. The pivot will be placed between these two parts
   *
   * @param pivotIdx Index at which the pivot to be use for this partitioning is found.
   * @param loIdx Leftmost index to be included in the partition
   * @param highIdx Rightmost index to be included in the partition
   * @return The index at which the pivot is eventually placed.
   */
  private int partition(List<E> list, int pivotIdx, int loIdx, int highIdx) {
	  
	  E swap = list.get(pivotIdx);
	  list.set(pivotIdx, list.get(loIdx));
	  list.set(loIdx, swap);  
	  pivotIdx = loIdx;
	  
	  while ( highIdx < list.size() && loIdx < highIdx ) {
		  while ( highIdx < list.size() && loIdx < highIdx && list.get(pivotIdx).compareTo(list.get(loIdx)) >= 0 ) {
			  loIdx++;
		  }
		  while ( highIdx < list.size() && highIdx >= loIdx && list.get(pivotIdx).compareTo(list.get(highIdx)) < 0 ) {
			  highIdx--;
		  }
		  if ( loIdx >= highIdx ) {
			  swap = list.get(pivotIdx);
			  list.set(pivotIdx, list.get(highIdx));
			  list.set(highIdx, swap);
			  return highIdx;
		  }
		  if ( highIdx < list.size() ) {
		  swap = list.get(loIdx);
		  list.set(loIdx, list.get(highIdx));
		  list.set(highIdx, swap);
		  }
	  }
	  return highIdx;
	  
  }
}