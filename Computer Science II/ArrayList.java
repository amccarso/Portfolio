package edu.buffalo.cse116;

import java.util.AbstractList;
import java.util.Arrays;

/**
 * Defines an array-based class to implement List functionality.
 *
 * @author Matthew Hertz
 * @param <E> Element type for this Collection
 */
@SuppressWarnings("unchecked")
public class ArrayList<E> extends AbstractList<E> {
  /** First index in the array at which elements cannot be found. Only indices LESS THAN this value are valid. */
  private int _size;

  /** Array in which the elements are stored. */
  private E[] _store;

  /**
   * Creates an empty list using the default capacity.
   */
  public ArrayList() {
    _size = 0;
    _store = (E[]) new Object[32];
  }

  /**
   * Update the value at an existing index so that it now is equal to the new value.
   *
   * @param index Location in the list where we will replace the element.
   * @return Original element at the specified index in this list
   */
  @Override
  public E set(int index, E elem) {
	  
	  if(!(index < _size)) {
		  throw new IndexOutOfBoundsException();
	  }
	  
	  E original = _store[index];
	  _store[index] = elem;
	  return original;
  }

  /**
   * Removes the element in the list at the given index, if that index is a valid one for the ArrayList. The method
   * returns the element that this method has removed from the ArrayList. Since the order of elements in a List IS
   * guaranteed, we need to make changes relative to the use in an ArrayMultiSet.
   *
   * @param index Index of the element to be removed from the List.
   * @return Element removed from the List.
   */
  @Override
  public E remove(int index) {
	  
	  if(!(index < _size)) {
		  throw new IndexOutOfBoundsException();
	  }
	  
	  E original = _store[index];
	  
	  while(index< _size-1) {
		  _store[index] = _store[index+1];
		  index++;
	  }
	  _store[index] = null;
	  _size--;
	  return original;
  }

  /**
   * Returns the element at the specified index in this list.
   *
   * @param index List location whose element should be returned.
   * @return Element at the specified index in this list
   */
  @Override
  public E get(int index) {
    if ((index < 0) || (index >= _size)) {
      throw new IndexOutOfBoundsException();
    }
    return _store[index];
  }

  /**
   * Returns true if this list is empty and false otherwise.
   *
   * @return true if the list is empty, false otherwise
   */
  @Override
  public boolean isEmpty() {
    return _size == 0;
  }

  /**
   * Returns the number of elements currently in this list.
   *
   * @return the number of elements in the list
   */
  @Override
  public int size() {
    return _size;
  }
}
