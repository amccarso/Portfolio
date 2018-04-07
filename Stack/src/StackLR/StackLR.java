package StackLR;

public class StackLR<E> {
	private LRStruct<E> _data;

	public StackLR() {
		_data = new LRStruct();
	}
	
	public void push (E item) {
		_data.insertFront(item);
	}
	
	public E pop() {
		return _data.removeFront();
	}
	
	public E peek() {
		return _data.getDatum();
	}
	
	public boolean isEmpty() {
		return _data.execute(new EmptyVisitor<E>(), null);
	}
}

