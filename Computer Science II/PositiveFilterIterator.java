package edu.buffalo.cse116;

import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * Class that can be used to iterate through the positive numbers (e.g., numbers GREATER THAN 0) in an array.
 *
 * @author Matthew Hertz
 */
public class PositiveFilterIterator implements Iterator<Integer> {
  /** Array of numbers; we will only return the positive numbers from this Iterator. */
  private int[] source;

  /** Index in the array whose entry will be returned by the Iterator. */
  private int cursor;

  /**
   * Helper method for this Iterator. It will return the index of the next positive entry in
   * {@link PositiveFilterIterator#source} starting from {@code startIndex}. If there are no positive entries in
   * {@link PositiveFilterIterator#source} starting from {@code startIndex}, then it returns the {@code source.length}
   *
   * @param startIndex Index in {@link PositiveFilterIterator#source} from which we will search for an entry whose value is
   *          greater than 0.
   * @return Starting at {@code startIndex}, the index of the next entry in {@code source} whose value is positive.
   */
  private int advance(int startIndex) {
    int retVal = startIndex;
    while (retVal < source.length && source[retVal] <= 0) {
      retVal += 1;
    }
    return retVal;
  }

  /**
   * Create a new Iterator that will be used to return the positive numbers in this array.
   *
   * @param arr Array of numbers through which we will be iterating.
   */
  public PositiveFilterIterator(int[] arr) {
	  
	  source = arr;
	  
	  cursor = advance(0);
	  
  }

  /** Return true if there is another character for the instance to return. */
  public boolean hasNext() {
	  
	  if (cursor < source.length) {
		  return true;
	  }
	  
	  return false;
  }

  /** Returns the next positive number in the array. */
  public Integer next() throws NoSuchElementException {


	  
	  if(hasNext() == true) {
		  int retVal = source[cursor];
		  cursor++;
		  cursor = advance(cursor);
		  return retVal;
	  }
	  
	  if(source.length == 0 || cursor == source.length) {
		  throw new NoSuchElementException();
	  }
	  
	  return source[cursor];		  
  }

  public void remove() {
    throw new UnsupportedOperationException();
  }
}