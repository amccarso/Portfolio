package arraylist;

import java.util.ArrayList;

public class QueueArray<E> {
	private ArrayList<E> _data;
	
	public QueueArray(){
		_data = new ArrayList<E>();
	}
	
	public void enqueue (E item) {
		_data.add(item);
	}
	
	public E dequeue() {
		if(isEmpty()){
			throw new EmptyQueueException();
		}
		return _data.remove(0);
		
	}
	
	public E peek(){
		if(isEmpty()){
			throw new EmptyQueueException();
		}
		return _data.get(0);
	}
	
	public boolean isEmpty(){
		return _data.isEmpty();
	}

}
