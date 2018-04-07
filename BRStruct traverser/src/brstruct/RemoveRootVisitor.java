package brstruct;

import brstruct.BRStruct.IAlgo;
import brstruct.visitors.LeftmostVisitor;

/**
 * RemoveRootVisitor.java
 *
 * @author alphonce
 *
 *  Created: Thu Apr  4 2002
 * Modified: Tue Apr  4 2006 - added Generics
 * Modified: Wed Apr 16 2008 - renamed class to LeftRemoveRootVisitor
 * 							 - added comments regarding setState and
 * 							   packaging
 * Modified: Wed Nov 13 2013 - renamed class to RemoveRootVisitor
 *
 * This visitor is designed to be executed on the binary tree whose
 * root value we wish to remove.  The BinarySearchTree class' remove
 * method should first execute the FindVisitor on its _brs.
 *
 * If the value to be removed is not in the tree, the tree returned
 * by the FindVisitor is an empty BRStruct.  This is handled by the
 * emptyCase below.
 *
 * If the value to be removed does appear in the tree, the tree
 * returned by the FindVisitor is a non-empty BRStruct.  This is
 * handled by the nonEmptyCase below.  How this works is described
 * by the comments embedded in the code below.
 *
 * This visitor is in the brstruct package because the setState method
 * has package access.
 */
public class RemoveRootVisitor<E> implements IAlgo<Object, E, Object> {
	@Override
	public Object emptyCase(BRStruct<E> host, Object input) {
		return host;
	}

	@Override
	public Object nonEmptyCase(final BRStruct<E> mainTree, Object input) {
		// mainTree has root datum we want to remove
		mainTree.getRight().execute(new IAlgo<Object, E, Object>() {
			@Override
			public Object emptyCase(BRStruct<E> host, Object input) {
				// RIGHT SUBTREE IS EMPTY - PULL UP LEFT SUBTREE
				// OF mainTree
				mainTree.setState(mainTree.getLeft().getState());
				return null;
			}

			@Override
			public Object nonEmptyCase(BRStruct<E> rightSubtreeOfMainTree, Object input) {
				// RIGHT SUBTREE IS NOT EMPTY - FIND SMALLEST IN RIGHT...
				BRStruct<E> smallestTree = rightSubtreeOfMainTree.execute(
						new LeftmostVisitor<E>(), rightSubtreeOfMainTree);
				E smallestValue = smallestTree.getDatum();
				// SET VALUE IN mainTree TO smallestValue
				mainTree.setDatum(smallestValue);
				// REMOVE THE NODE WHERE WE FOUND smallestValue
				smallestTree.setState(smallestTree.getRight().getState());
				return null;
			}
		}, null);
		return null;
	}
}
