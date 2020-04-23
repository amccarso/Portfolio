package edu.buffalo.cse116;

import java.util.AbstractCollection;
import java.util.Arrays;
import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * Implementation of a priority queue using an array-based binary tree. This is used to help students understand the
 * basic properties binary trees and will have more details explained in future lectures.
 *
 * @author William J. Collins
 * @author Matthew Hertz
 * @param <E> Data type (which must be Comparable) of the elements in this tree.
 */
@SuppressWarnings("unused")
public class PriorityQueue<E extends Comparable<E>> extends AbstractCollection<E> {
  /** Index where the root node can be found. */
  private static final int ROOT = 0;

  /** Array used to store the elements in the binary tree. */
  private E[] store;

  /** Number of elements within the tree. */
  private int size;

  /**
   * Initializes this ArrayBinaryTree object to be empty. This creates the array in which items will be stored.
   */
  @SuppressWarnings("unchecked")
  public PriorityQueue() {
    store = (E[]) new Comparable[31];
    size = 0;
  }

  /**
   * Checks if the binary tree contains an element at the given index. This requires checking both that the array is
   * large enough (to avoid triggering an exception) AND (when the array is large enough) that the array has a non-null
   * value at that index.
   *
   * @param idx Index to be checked out.
   * @return True if there is an element at the given index; false otherwise.
   */
  private boolean nodeExists(int idx) {
    boolean arrayLocationExists = idx < store.length;
    return arrayLocationExists && (store[idx] != null);
  }

  /**
   * Given an index, returns the element in that node's left child. If the left child node does not exist, null should
   * be returned. It is important that this NOT trigger an index out of bounds exception.
   *
   * @param idx Index of the node for which we want the left child.
   * @return Value of the node's left child or null if no left child exists.
   */
  private E leftChild(int idx) {
    int leftChild = (idx * 2) + 1;
    if (!nodeExists(leftChild)) {
      return null;
    }
    return store[leftChild];
  }

  /**
   * Given an index, returns the element in that node's right child. If the right child node does not exist, null should
   * be returned. It is important that this NOT trigger an index out of bounds exception.
   *
   * @param idx Index of the node for which we want the right child.
   * @return Value of the node's right child or null if no right child exists.
   */
  private E rightChild(int idx) {
    int rightChild = (idx * 2) + 2;
    if (!nodeExists(rightChild)) {
      return null;
    }
    return store[rightChild];
  }

  /**
   * Returns the size of this ArrayBinaryTree object.
   *
   * @return the size of this ArrayBinaryTree object.
   */
  @Override
  public int size() {
    return size;
  }

  /**
   * Returns an iterator that will return the elements in this ArrayBinaryTree, but without any specific ordering.
   *
   * @return Iterator positioned at the smallest element in this ArrayBinaryTree object.
   */
  @Override
  public Iterator<E> iterator() {
    // Skipped for now.
    throw new UnsupportedOperationException();
  }

  /**
   * Adds the specified element to this heap in the appropriate position according to its key value.
   *
   * @param obj the element to be added to the heap
   * @return Since this method will always succeed, it only returns true.
   */
  @Override
  public boolean add(E obj) {
    // Make certain the store has space to add an element.
    if (size == store.length) {
      store = Arrays.copyOf(store, store.length * 2);
    }
    store[size] = obj;
    size += 1;
    // Should contain the code to sift up here, but I skipped it to make the problem interesting.
    return true;
  }

  /**
   * Remove the element with the lowest value in this heap and returns a reference to it. Throws an
   * NoSuchElementException if the heap is empty.
   *
   * @return the element with the lowest value in this heap
   */
  public E remove() {
    if (isEmpty()) {
      throw new NoSuchElementException("Cannot call remove on an empty PriorityQueue");
    }
    E retVal = store[0];
    store[0] = store[size - 1];
    size -= 1;
    // Should contain the code to sift down here, but I skipped it to make the problem interesting.
    return retVal;
  }

  /**
   * Returns the most important element. Throws an NoSuchElementException if the heap is empty.
   *
   * @return the element with the lowest value in this heap
   */
  public E element() {
	  
    if (isEmpty()) {
      throw new NoSuchElementException("Cannot call remove on an empty PriorityQueue");
    }
    
    return store[0];
    
  }

  public boolean heapOrderValid() {
	  
	  for ( int i = 0; i < (size/2); i++) {
		  if ( store[2*i+1] != null && store[i].compareTo(store[2*i+1]) > 0 || 
				  store[2*i+2] != null && store[i].compareTo(store[2*i+2]) > 0 ) {
			  return false;
		  }
	  }
	  return true;
	  
  }

  public boolean isCompleteTree() {

	  for ( int i = 0; i < size; i++ ) {
		  if ( store[i] == null ) {
			  return false;
		  }
	  }
	  return true;
  }
  
}