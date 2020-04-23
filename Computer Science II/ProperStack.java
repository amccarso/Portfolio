package edu.buffalo.cse116;

import java.util.ArrayList;
import java.util.EmptyStackException;
import java.util.List;

/**
 * Proper Stack implementation -- unlike Java, this eliminates all of the List methods that do not make sense in this
 * environment.
 *
 * @author Matthew Hertz
 * @param <E> Element type for this data structure
 */
public class ProperStack<E> {
  /** The backing store in which all the elements are stored. */
  private List<E> store;

  /** Create a new (empty) instance of this class. */
  public ProperStack() {
    store = new ArrayList<E>();
  }

  /**
   * Pushes an item onto the top of this stack. Traditionally, this is the only method available to add data to a Stack.
   *
   * @param item Element to be added to the top of the stack.
   * @return Element added to the Stack (e.g., {@code item}).
   */
  public E push(E item) {

	 //List<E> newStore = new ArrayList<E>();
	  store.add(store.size(), item);
	  
	  return item;
  }

  /**
   * Removes and returns the element at the top of this stack. Traditionally, this is the only method available to
   * remove data from the Stack.
   *
   * @return Element that was removed from the top of the stack.
   * @throws EmptyStackException Thrown when the Stack does not have any elements to remove.
   */
  public E pop() {
	  return store.remove(store.size()-1);
  }

  /**
   * Like {@link #pop()}, this returns the element at the top of the stack, but unlike {@link #pop} this method DOES NOT
   * remove it from the stack.
   *
   * @return Element that is at the top of the stack.
   * @throws EmptyStackException Thrown when the Stack does not have any elements to remove.
   */
  public E peek() {

	  if(store.size() == 0) {
		  throw new EmptyStackException();
	  }
	  return store.get(store.size()-1);
  }

  /**
   * Returns the number of elements in this Stack.
   *
   * @return Items available in the Stack.
   */
  public int size() {
    return store.size();
  }

  /**
   * Returns whether there are any elements in this Stack.
   *
   * @return True if the Stack does not have any elements; false otherwise.
   */
  public boolean isEmpty() {
    return store.isEmpty();
  }
}