package edu.buffalo.cse116;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertSame;

import org.junit.Test;

public class PQueueTests {

	@Test
	public void AddEmpty() {
		PQueue<Integer> pq = new PQueue<Integer>();
		pq.add(1);
		assertSame(pq.element(), 1);
	}
	
	@Test 
	public void AddStart() {
		PQueue<Integer> pq = new PQueue<Integer>();
		pq.add(4);
		pq.add(1);
		pq.add(2);
		pq.add(0);
		assertSame(pq.element(), 0);
	}
	
	@Test
	public void AddEnd() {
		PQueue<Integer> pq = new PQueue<Integer>();
		pq.add(1);
		pq.add(2);
		pq.add(3);
		assertSame(pq.element(), 1);
		pq.remove();
		assertSame(pq.element(), 2);
		pq.remove();
		assertSame(pq.element(), 3);
	}
	
	@Test 
	public void AddMid() {
		PQueue<Integer> pq = new PQueue<Integer>();
		pq.add(12);
		pq.add(5);
		pq.add(4);
		pq.add(6);
		assertSame(pq.element(),4);
		pq.remove();
		assertSame(pq.element(), 5);
	}
}
