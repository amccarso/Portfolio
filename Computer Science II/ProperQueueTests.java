package edu.buffalo.cse116;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class ProperQueueTests {

	@Test
	public void elementNulltest() {
		ProperQueue<Integer> queue = new ProperQueue<Integer>();
		
		if(queue.element()==null) {
			assertTrue(true);
		}	else {
			assertTrue(false);
		}
	}
	
	@Test
	public void elementOnetest() {
		ProperQueue<Integer> queue = new ProperQueue<Integer>();
		queue.add(2);
		//assertEquals would not work for with parameters of int type
		if(queue.element() == 2) {
			assertTrue(true);
		}
		else{
			assertTrue(false);
		}
	}
	
	@Test
	public void elementManytest() {
		ProperQueue<Integer> queue = new ProperQueue<Integer>();
		queue.add(3);
		queue.add(69);
		queue.add(420);
		queue.add(8);
		if(queue.element() == 3) {
			assertTrue(true);
		} else {
			assertFalse(true);
		}
	}
	
	@Test
	public void addOnetest() {
		ProperQueue<Integer> queue = new ProperQueue<Integer>();
		queue.add(1);
		if(queue.element()==1) {
			assertTrue(true);
		} else { 
			assertFalse(true);
		}
		if(queue.size() == 1) {
			assertTrue(true);
		} else { assertFalse(true); }
	}
	
	@Test 
	public void removeNulltest() {
		ProperQueue<Integer> queue = new ProperQueue<Integer>();
		if(queue.remove() == null) {
			assertTrue(true);
		} else {
			assertFalse(true);
		}
	}
	
	@Test
	public void removeOnetest() {
		ProperQueue<Integer> queue = new ProperQueue<Integer>();
		queue.add(2);
		if (queue.remove() == 2) {
			assertTrue(true);
		} else { assertFalse(true); }
		if (queue.element() == null) {
			assertTrue(true);
		} else { assertFalse(true); }
	}
	
	@Test
	public void removeManytest() {
		ProperQueue<Integer> queue = new ProperQueue<Integer>();
		queue.add(3);
		queue.add(12);
		queue.add(65);
		queue.add(100);
		if(queue.remove() == 3) {
			assertTrue(true);
		} else { assertFalse(true); }
		if(queue.element() == 12) {
			assertTrue(true);
		} else { assertFalse(false);}
		if(queue.size() == 3) {
			assertTrue(true);
		} else { assertFalse(true); }
	}
}
