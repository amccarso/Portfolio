package edu.buffalo.cse116;

import java.util.AbstractCollection;
import java.util.Iterator;

/**
 * Instances of this class represent a vanilla binary tree (e.g., and not a binary search tree).
 *
 * @author Matthew Hertz
 * @param <E> Type of data stored in each node of this tree. Since this is not a BST, E can be anything.
 */
public class BinaryTree<E> extends AbstractCollection<E> {

  /** Root node of this binary tree */
  private Entry<E> root;

  /** Number of nodes/elements within this binary tree. */
  private int size;

  /**
   * Initializes this BinarySearchTree object to be empty, to contain only elements of type E, to be ordered by the
   * Comparable interface, and to contain no duplicate elements.
   */
  public BinaryTree() {
    root = null;
    size = 0;
  }

  public <S, T> T visit(TreeVisitor<E, S, T> visitor) {
	  S initVal = visitor.getInitialValue();
	  return root.apply(visitor, initVal);
  }

  /**
   * Returns the size of this BinarySearchTree object.
   *
   * @return the size of this BinarySearchTree object.
   */
  @Override
  public int size() {
    return size;
  }

  /**
   * Iterator method that has, at last, been implemented.
   *
   * @return an iterator positioned at the smallest element in this BinarySearchTree object.
   */
  @Override
  public Iterator<E> iterator() {
    // Skipped until next week
    throw new UnsupportedOperationException();
  }

  /**
   * Determines if there is at least one element in this binary tree object that equals a specified element.
   *
   * @param obj - the element sought in this binary tree
   * @return true if the object is an element in the binary tree; false othrwise.
   */
  @Override
  public boolean contains(Object obj) {
    // Skipped on behalf of the first homework problem.
    throw new UnsupportedOperationException();
  }
}