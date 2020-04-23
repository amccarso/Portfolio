package edu.buffalo.cse116;

public class Entry<E> {
  /** Tree's element which is stored within this Node. */
  private E element;

  /** Left child of the current Node. */
  private Entry<E> left;
  /** Right child of the current Node. */
  private Entry<E> right;
  /** Parent in the binary tree for the current Node. */
  private Entry<E> parent;

  /**
   * Initializes this Entry object. This default constructor is defined for future expansion purposes.
   */
  public Entry() {}

  /**
   * Initializes this Entry object from element and parent.
   */
  public Entry(E element, Entry<E> parent) {
    this.element = element;
    this.parent = parent;
  }

  /** Return the element stored in this node. */
  public E getElement() {
    return element;
  }

  /** Specify a new element to be stored at this node. */
  public void setElement(E element) {
    this.element = element;
  }

  /** Get the node's left child. */
  public Entry<E> getLeft() {
    return left;
  }

  /** Specify a node to be the left child of the current node. */
  public void setLeft(Entry<E> left) {
    this.left = left;
  }

  /** Get the node's right child. */
  public Entry<E> getRight() {
    return right;
  }

  /** Specify a node to be the right child of the current node. */
  public void setRight(Entry<E> right) {
    this.right = right;
  }

  /** Get the node's parent in the tree. This is null if the node is a root. */
  public Entry<E> getParent() {
    return parent;
  }

  /** Specify a node to be the parent of the current node. */

  public void setParent(Entry<E> parent) {
    this.parent = parent;
  }

  /**
   * Implement the node's portion of the Visitor pattern. This allows the TreeVisitor to work and return the result of
   * the traversal.
   *
   * @param visitor TreeVisitor instance doing the work.
   * @param data Data being passed along as part of this visiting traversal.
   * @return The result returned by the TreeVisitor.
   */
  public <S, T> T apply(TreeVisitor<E, S, T> visitor, S data) {

	  if(this.getLeft()==null && this.getRight()==null) {
		  return visitor.visitLeaf(this, data);
	  } else { return visitor.visitInterior(this, data); }
	  
  }

}