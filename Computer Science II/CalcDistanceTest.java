package edu.buffalo.cse116;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class CalcDistanceTest extends CalcDistance {

	
	@Test
	public void totalTest() {
		assertEquals(9.00, totalDistance( 1.0,2.0,3.0,1.0,4.0,1.0), .001);
	}
	
	@Test
	public void dist1Test() {
		assertEquals(2.00, totalDistance( 1.0, 2.0, 0.0, 0.0, 0.0, 0.0), .001);
	}
	
	@Test
	public void dist2Test() {
		assertEquals(3.00, totalDistance( 0.0, 0.0, 3.0, 1.0, 0.0, 0.0), .001);
	}
	
	@Test
	public void dist3Test() {
		assertEquals(4.00, totalDistance( 0.0, 0.0, 0.0, 0.0, 4.0, 1.0), .001);
	}
	
	@Test
	public void noRunningTest() {
		assertEquals(0.00, totalDistance( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), .001);
	}
	
	
}
