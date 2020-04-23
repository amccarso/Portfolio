package edu.buffalo.cse116;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class TieBreakerTest {

	@Test
	public void tieBreakerTest() {
		
		NotAmazonItem nai = new NotAmazonItem(7, 100, 9.9);
		NotAmazonItem NAI = new NotAmazonItem(8, 101, 9.9);
		NotAmazonItem IAN = new NotAmazonItem(9, 99, 9.9);
		NotAmazonItem ian = new NotAmazonItem(10, 100, 9.9);
		RatingComparator rc = new RatingComparator();
		
		assertEquals(1, rc.compare(nai, NAI));
		assertEquals(-1, rc.compare(nai, IAN));
		assertEquals(0, rc.compare(nai, ian));
	}
}
