package edu.buffalo.cse116;

import static org.junit.Assert.assertEquals;

import java.util.ArrayList;

import org.junit.Test;

public class ListSumNegTest extends ListSumNeg {

	@Test
	public void t1() {
		ArrayList<Double> list = new ArrayList<Double>();
		list.add(-1.00);
		list.add(2.00);
		list.add(-3.00);
		list.add(-1000.00);
		list.add(-.005);
		list.add(.05);
		assertEquals( -1.00 + -3.00 + -1000.00 + -.005, sumNegatives(list) , .001);
	}
	
	@Test
	public void t2() {
		ArrayList<Double> list = new ArrayList<Double>();
		list.add(-2.00);
		list.add(4.00);
		list.add(-98.00);
		assertEquals(-2.00 + -98.00, sumNegatives(list), .001);
	}
}
