package edu.buffalo.cse116;

/**
 * When correctly implemented, this class will be usable to calculate the Huffman encodings for this binary tree.
 * These encodings are based upon the path from the binary tree's root down to each node. With how Huffman trees are built,
 * the final encodings cannot be calculated until the tree is finalized.
 *
 * @author Matthew Hertz
 */
public class HuffmanEncodingVisitor implements TreeVisitor<String, String, Void> {

  @Override
  public Void visitLeaf(Entry<String> leaf, String data) {
	  leaf.setElement(data);
	  return null;
  }

  @Override
  public Void visitInterior(Entry<String> node, String data) {
	  
	  
	  if (node.getLeft() != null) {
		  node.getLeft().apply(this, data+"0");
	  } 
	  
	  node.setElement(data);
	  
	  if (node.getRight() != null) {
		  node.getRight().apply(this, data+"1");
	  }
	return null;
  }

  @Override
  public String getInitialValue() {
	  return "";
  }

}