package edu.buffalo.cse116;

import java.util.AbstractSet;
import java.util.ConcurrentModificationException;
import java.util.Iterator;
import java.util.NoSuchElementException;

public class BinarySearchTree<E extends Comparable<E>> extends AbstractSet<E> {
  private Entry<E> root;

  private int size;
  
  private long modCount = 0;

  /**
   * Initializes this BinarySearchTree object to be empty, to contain only elements of type E, to be ordered by the
   * Comparable interface, and to contain no duplicate elements.
   */
  public BinarySearchTree() {
    root = null;
    size = 0;
    modCount = 0;
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
    return new TreeIterator();
  }

  /**
   * Determines if there is at least one element in this BinarySearchTree object that equals a specified element. The
   * worstTime(n) is O(n) and averageTime(n) is O(log n).
   *
   * @param obj - the element sought in this BinarySearchTree object.
   * @return true - if there is an element in this BinarySearchTree object that equals obj; otherwise, return false.
   * @throws ClassCastException - if obj cannot be compared to the elements in this BinarySearchTree object.
   * @throws NullPointerException - if obj is null.
   */
  @Override
  public boolean contains(Object obj) {
    return getEntry(obj) != null;
  }

  /**
   * Ensures that this BinarySearchTree object contains a specified element. The worstTime(n) is O(n) and averageTime(n)
   * is O(log n).
   *
   * @param element - the element whose presence is ensured in this BinarySearchTree object.
   * @return true - if this BinarySearchTree object changed as a result of this method call (that is, if element was
   *         actually inserted); otherwise, return false.
   * @throws ClassCastException - if element cannot be compared to the elements already in this BinarySearchTree object.
   * @throws NullPointerException - if element is null.
   */
  @Override
  public boolean add(E element) {
    if (element == null) {
      throw new NullPointerException();
    }
    if (root == null) {
      root = new Entry<E>(element, null);
      size++;
      modCount++;
      return true;
    } else {
      Entry<E> temp = root;

      int comp;

      while (true) {
        comp = element.compareTo(temp.element);
        if (comp == 0) {
          return false;
        }
        if (comp < 0) {
          if (temp.left != null) {
            temp = temp.left;
          } else {
            temp.left = new Entry<E>(element, temp);
            size++;
            modCount++;
            return true;
          }
        } else if (temp.right != null) {
          temp = temp.right;
        } else {
          temp.right = new Entry<E>(element, temp);
          size++;
          modCount++;
          return true;
        }
      }
    }
  }

  /**
   * Delete a leaf Entry from the BST by setting the parent's reference to it to null
   *
   * @param leaf Leaf node that needs to be deleted.
   */
  private void deleteLeafFromTree(Entry<E> leaf) {
    if (leaf == leaf.parent.left) {
      leaf.parent.left = null;
    } else {
      leaf.parent.right = null;
    }
  }

  /**
   * When we need to replace a node with its (only) child, we need to update references in the tree to make this happen.
   * This method changes references so that they are no longer to the (deleted) node.
   *
   * @param childToPromote The node that will replace it's parent in the tree.
   */
  private void replaceParentEntryWithChild(Entry<E> childToPromote) {
    Entry<E> parentEntry = childToPromote.parent;
    childToPromote.parent = parentEntry.parent;
    if (parentEntry == root) {
      root = childToPromote;
    } else if (parentEntry == parentEntry.parent.left) {
      parentEntry.parent.left = childToPromote;
    } else {
      parentEntry.parent.right = childToPromote;
    }
    modCount++;
  }

  /**
   * Once we know a node has either 0 or 1 children, we need to find the replacement node. If the node to be removed is
   * a leaf, null should be returned. If the node has only one child, then that only child should be removed.
   *
   * @param removeMe Node that we will remove from the tree
   * @return null if {@code removeMe} has no children; {@code removeMe}'s only child otherwise.
   */
  private Entry<E> findReplacement(Entry<E> removeMe) {
    Entry<E> replacement;
    if (removeMe.left != null) {
      replacement = removeMe.left;
    } else {
      replacement = removeMe.right;
    }
    return replacement;
  }

  /**
   * Ensures that this BinarySearchTree object does not contain a specified element. The worstTime(n) is O(n) and
   * averageTime(n) is O(log n).
   *
   * @param obj - the object whose absence is ensured in this BinarySearchTree object.
   * @return true - if this BinarySearchTree object changed as a result of this method call (that is, if obj was
   *         actually removed); otherwise, return false.
   * @throws ClassCastException - if obj cannot be compared to the elements already in this BinarySearchTree object.
   * @throws NullPointerException - if obj is null.
   */
  @Override
  public boolean remove(Object obj) {
    Entry<E> e = getEntry(obj);
    if (e == null) {
      return false;
    }
    size--;
    

    // If p has two children, replace p's element with p's successor's
    // element, then make p reference that successor.
    if ((e.left != null) && (e.right != null)) {
      // Get the successor for this node
      Entry<E> tribute = successor(e);
      // Move that node's element to the node which we originally wanted to delete.
      e.element = tribute.element;
      e = tribute;
      
    }
    // At this point, p has either no children or one child.
    Entry<E> replacement = findReplacement(e);

    if (replacement != null) {
      replaceParentEntryWithChild(replacement);
    } else if (e != root) {
      deleteLeafFromTree(e);
    } else {
      root = null;
    }
    modCount++;
    return true;
  }

  /**
   * Finds the Entry object that houses a specified element, if there is such an Entry. The worstTime(n) is O(n), and
   * averageTime(n) is O(log n).
   *
   * @param obj - the element whose Entry is sought.
   * @return the Entry object that houses obj - if there is such an Entry; otherwise, return null.
   * @throws ClassCastException - if obj is not comparable to the elements already in this BinarySearchTree object.
   * @throws NullPointerException - if obj is null.
   */
  @SuppressWarnings("unchecked")
  private Entry<E> getEntry(Object obj) {
    int comp;

    if (obj == null) {
      throw new NullPointerException();
    }
    if (!(obj instanceof Comparable)) {
      return null;
    }
    Comparable<E> compObj = (Comparable<E>) obj;
    Entry<E> e = root;
    while (e != null) {
      comp = compObj.compareTo(e.element);
      if (comp == 0) {
        return e;
      } else if (comp < 0) {
        e = e.left;
      } else {
        e = e.right;
      }
    }
    return null;
  }

  /**
   * Finds the successor of a specified Entry object in this BinarySearchTree. The worstTime(n) is O(n) and
   * averageTime(n) is constant.
   *
   * @param e - the Entry object whose successor is to be found.
   * @return the successor of e, if e has a successor; otherwise, return null.
   */
  private Entry<E> successor(Entry<E> e) {
    if (e == null) {
      return null;
    } else if (e.right != null) {
      // successor is leftmost Entry in right subtree of e
      Entry<E> p = e.right;
      while (p.left != null) {
        p = p.left;
      }
      return p;

    } else {
      // go up the tree to the left as far as possible, then go up
      // to the right.
      Entry<E> p = e.parent;
      Entry<E> ch = e;
      while ((p != null) && (ch == p.right)) {
        ch = p;
        p = p.parent;
      }
      return p;
    }
  }

  protected class TreeIterator implements Iterator<E> {

    private Entry<E> lastReturned, next;
    long expectedModCount;
    /**
     * Positions this TreeIterator to the smallest element, according to the Comparable interface, in the
     * BinarySearchTree object. The worstTime(n) is O(n) and averageTime(n) is O(log n).
     */
    protected TreeIterator() {
    	  expectedModCount = modCount;
      next = root;
      if (next != null) {
        while (next.left != null) {
          next = next.left;
        }
      }
    }

    /**
     * Determines if there are still some elements, in the BinarySearchTree object this TreeIterator object is iterating
     * over, that have not been accessed by this TreeIterator object.
     *
     * @return true - if there are still some elements that have not been accessed by this TreeIterator object;
     *         otherwise, return false.
     */
    @Override
    public boolean hasNext() {
      return next != null;
    }

    /**
     * Returns the element in the Entry this TreeIterator object was positioned at before this call, and advances this
     * TreeIterator object. The worstTime(n) is O(n) and averageTime(n) is constant.
     *
     * @return the element this TreeIterator object was positioned at before this call.
     * @throws NoSuchElementException - if this TreeIterator object was not positioned at an Entry before this call.
     */
    @Override
    public E next() {
       		
    		if (hasNext()) {
    			if (expectedModCount == modCount) {
    				lastReturned = next;
    				next = successor(next);
    				return lastReturned.element;
    			} else { throw new ConcurrentModificationException(); }
    		}  else { throw new NoSuchElementException(); }
    		
    } // method next

    /**
     * Removes the element returned by the most recent call to this TreeIterator object's next() method. The
     * worstTime(n) is O(n) and averageTime(n) is constant.
     *
     * @throws IllegalStateException - if this TreeIterator's next() method was not called before this call, or if this
     *           TreeIterator's remove() method was called between the call to the next() method and this call.
     */
    @Override
    public void remove() {
      throw new UnsupportedOperationException();
    }
  }

  protected static class Entry<E> {
    private E element;

    protected Entry<E> left = null, right = null, parent;

    /**
     * Initializes this Entry object. This default constructor is defined for the sake of subclasses of the
     * BinarySearchTree class.
     */
    public Entry() {}

    /**
     * Initializes this Entry object from element and parent.
     */
    public Entry(E element, Entry<E> parent) {
      this.element = element;
      this.parent = parent;
    }

  }
}