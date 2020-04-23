package edu.buffalo.cse116;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class EntryTests {

	@Test
	public void leftChildWithGrandkidsAndGreatGrandkids() {
		
		Entry<Integer> Int = new Entry<Integer>(1, null);
		Entry<Integer> b = new Entry<Integer>(3, Int);
		Entry<Integer> a = new Entry<Integer>(2, Int);
		Entry<Integer> c = new Entry<Integer>(4, a);
		Entry<Integer> d = new Entry<Integer>(5, a);
		Entry<Integer> e = new Entry<Integer>(6, b);
		Entry<Integer> f = new Entry<Integer>(7, b);
		Entry<Integer> g = new Entry<Integer>(8, c);
		Entry<Integer> h = new Entry<Integer>(9, c);
		Entry<Integer> i = new Entry<Integer>(10, h);
		Int.setLeft(a); Int.setRight(b); a.setLeft(c); a.setRight(d); b.setLeft(e); b.setRight(f);
		c.setLeft(g); d.setRight(h); h.setLeft(i);
		assertEquals(4, Int.height());
	}
	
}
