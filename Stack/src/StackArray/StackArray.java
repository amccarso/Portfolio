package StackArray;

import java.util.ArrayList;

public class StackArray<E> {
	private ArrayList<E> _data;
	
	public StackArray() {
		_data = new ArrayList<E>();
	}

	public void push (E item) {
		_data.add(item);
	}
	
	public E pop(){
		return _data.remove(0);
	}
	
	public E peek(){
		return _data.get(0);
	}
	
	public boolean isEmpty(){
		return _data.isEmpty();
	}
	
}
