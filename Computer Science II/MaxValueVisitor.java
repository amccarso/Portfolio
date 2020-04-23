package edu.buffalo.cse116;

/**
 * When correctly implemented, this class will complete the Visitor pattern and create a system which returns the largest
 * value in the binary tree. It is important that each of the methods only do the work appropriate for their calculating the maximum value.
 *
 * @author Matthew Hertz
 */
public class MaxValueVisitor implements TreeVisitor<Double, Void, Double> {

  @Override
  public Double visitLeaf(Entry<Double> leaf, Void data) {
	  return leaf.getElement();
  }

  @Override
  public Double visitInterior(Entry<Double> node, Void data) {

	  Double maxl,maxr;
	  maxl = maxr = node.getElement();
	  
	  
	  if (node.getLeft() != null) {
		  maxl = node.getLeft().apply(this, data);
	  } 
	  if (node.getRight() != null) { 
		  maxr = node.getRight().apply(this, data);
	  }
	  if(node.getLeft() != null && node.getRight() != null) {
		  maxl = node.getLeft().apply(this, data);
		  maxr = node.getRight().apply(this, data);
	  }
	  
	  return Math.max(node.getElement(), Math.max(maxl, maxr));
  }

  @Override
  public Void getInitialValue() {	  
	  return null;
  }

}