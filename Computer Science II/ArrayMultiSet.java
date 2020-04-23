package edu.buffalo.cse116;

import java.util.AbstractCollection;
import java.util.Arrays;
import java.util.ConcurrentModificationException;
import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * Instances of this class are used to represent a multiset -- a searchable collection in which one can add multiple
 * copies of an element.
 *
 * @author Carl Alphonce
 * @author Matthew Hertz
 * @param <E> Element type for this collection
 */
@SuppressWarnings("unchecked")
public class ArrayMultiSet<E> extends AbstractCollection<E> {
  /** Array in which the elements in this multiset are stored. */
  private E[] _store;

  /**
   * Array indices below this amount contain the active elements in this collection.
   */
  private int _size;
  /**
   * Modification counter used to preserve the fail-fast nature of its iterators.
   */
  private long _modCount;

  // Class invariants:
  // * _store has all of the elements in the multi-set.
  // * All elements in _store are in indices < _size

  /**
   * Create a new empty multiset using the default initial capacity.
   */
  public ArrayMultiSet() {
    _size = 0;
    _store = (E[]) (new Object[16]);
  }

  /**
   * Update the multiset so that it includes all of the elements from before the call AND the given element.
   *
   * @param e Element to be added to this collection.
   */
  @Override
  public boolean add(E e) {
    // Check if we do not have enough space in the underlying array to store the
    // new element
    if (_size == _store.length) {
      // We do not have space, so create a new larger space (doubling the size
      // is the most time efficient)
      _store = Arrays.copyOf(_store, _store.length * 2);

    }
    // Add the element to the store
    _store[_size] = e;
    // Finally, we can increase _size, since this change will no longer violate
    // any class invariants.
    _size += 1;
    _modCount++;
    return true;
  }

  /**
   * Return true if at least one element in the multiset is equal to the given object. When {@code obj} is null, it must
   * use the {@code ==} operator to perform these checks, but when {@code obj} is not null, the {@link Object#equals}
   * method is used.
   *
   * @param obj Object (or null) for which we will search
   * @return {@code true} if {@code obj} was found; {@code false} if a match could not be found.
   */
  @Override
  public boolean contains(Object obj) {
    // Only scan through _size, since those are the only "real" entries for the
    // multiset.
    for (int i = 0; i < _size; i++ ) {
      // Need to use the == operator to match when we are searching for null;
      // once we know obj is not null, we need to use the .equals() method to be certain we match objects
      if ((obj == _store[i]) || ((obj != null) && obj.equals(_store[i]))) {
               return true;
      }
      // No else clause possible, since the match could be at a higher index!
    }
    return false;
  }


  /**
   * Removes the first instance of the given object, if one can be found in the ArrayMultiSet. The method returns
   * {@code true} when an instance was successfully removed and {@code false} if an instance was not found.
   *
   * @param obj Object (or null) which we want to remove
   * @return {@code true} if {@code obj} was found and removed; {@code false} if a match could not be found.
   */
  @Override
  public boolean remove(Object obj) {
    // Only scan through _size, since those are the only indices in _store at which elements are found
    for (int i = 0; i < _size; i++ ) {
      // Need to use the == operator to match when we are searching for null;
      // once we know obj is not null, we need to use the .equals() method to be certain we match objects
      if ((obj == _store[i]) || ((obj != null) && obj.equals(_store[i]))) {
        // Move the last element to plug the hole created by removing this object
        _store[i] = _store[_size - 1];
        // Be nice to the garbage collection system by nulling out the reference
        _store[_size - 1] = null;
        // Record that the size of the collection has decreased
        _size -= 1;
        _modCount++;
        return true;
      }
      // No else clause possible, since the match could be at a higher index!
    }
    return false;
  }

  @Override
  public int size() {
    return _size;
  }

  @Override
  public boolean isEmpty() {
    return _size == 0;
  }

  @Override
  public Iterator<E> iterator() {
    return new MultiSetIterator();
  }

  /**
   * This inner-class defines the Iterator instances of this multiset. This must be an inner-class in order to gain access to the elements.
   *
   * @author Carl Alphonse
   * @author Matthew Hertz
   */
  private class MultiSetIterator implements Iterator<E> {

    /**
     * The index of the _store entry which will be returned by the next call to next()
     */
    private int _cursor;

    /**
     * In keeping with the fail-fast convention, the iterator is only valid while _modCount remains on this version.
     */
    private long _expectedModCount;

    /**
     * Create a new instance of this class that will go through the (valid) entries in the store.
     */
    public MultiSetIterator() {
      _cursor = 0;
      _expectedModCount = _modCount;
    }

    public boolean hasNext() {
    	
    		if(_cursor < _size) {
    			return true;
    		}
    		
    		return false;
    }

    public E next() throws NoSuchElementException, ConcurrentModificationException {
    	
    		if(_modCount != _expectedModCount) {
    		throw new ConcurrentModificationException();
    		}
    		if(_cursor < _size) {
    			E e = _store[_cursor];
    			_cursor++;
    			return e;
    		} else if (_cursor <= _size) {
    			throw new NoSuchElementException();
    		} 
    		return null;
    		
    }
  }
}