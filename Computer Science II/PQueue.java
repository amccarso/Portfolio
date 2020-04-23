package edu.buffalo.cse116;

import java.util.LinkedList;
import java.util.List;
import java.util.NoSuchElementException;

/**
 * This class implements a PriorityQueue using a List. It is implemented so that elements are stored in sorted order.
 *
 * @author Matthew Hertz
 * @param <E> Type used for the element in this queue. To simplify coding, this type must be Comparable.
 */
public class PQueue<E extends Comparable<? super E>> {

  /** ArrayList holding the Entries in our PriorityQueue. */
  private List<E> linkedL;

  /**
   * Create a new instance of our priority queue that compares entries with a given key and value type. At the outset
   * this priority queue will be empty.
   */
  public PQueue() {
    linkedL = new LinkedList<E>();
  }


  /*
   * (non-Javadoc)
   * @see PriorityQueue#insert(java.lang.Object, java.lang.Object)
   */
  public boolean add(E elem) {
	  
	  int i = 0;
	  if(linkedL.contains(elem)) { return false; }
	  if (linkedL.size() == 0) {
		  linkedL.add(elem);
		  return true;
	  }
	  while (elem.compareTo(linkedL.get(i)) > 0 && i < linkedL.size()-1) {
		  i++;
	  }
	   
	  
	  linkedL.add(i, elem);
	  
	  return true;
  }

  /*
   * (non-Javadoc)
   * @see PriorityQueue#min()
   */
  public E element() throws NoSuchElementException {

	  if(linkedL.size() == 0) {
		  throw new NoSuchElementException();
	  }
	  return linkedL.get(0);
	
  }

  /*
   * (non-Javadoc)
   * @see PriorityQueue#removeMin()
   */
  public E remove() throws NoSuchElementException {

	  if (linkedL.size()==0) { throw new NoSuchElementException(); }
	  return linkedL.remove(0);
  }

  /**
   * Returns if the priority queue currently contains any entries.
   *
   * @return True if the queue has no entries, false otherwise.
   */
  public boolean isEmpty() {
    return linkedL.isEmpty();
  }

  /**
   * Returns the number of entries currently in the priority queue.
   *
   * @return Number of entries that are currently stored in the priority queue.
   */
  public int size() {
    return linkedL.size();
  }
}