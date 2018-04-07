package lrstruct;

public class QueueLRStruct<E>{
	private LRStruct<E> _data;
	public QueueLRStruct() {
		_data = new LRStruct<E>();
	}
	
	public void enqueue (E item) {
		_data.insertFront(item);
	}
	
	public E pop () {
		return _data.removeFront();
	}
	
	public E peek () {
		return _data.getDatum();
	}
	
	public boolean isEmpty () {
		return _data.execute(new EmptyVisitor<E>(), null);
	}
}
