package edu.buffalo.cse116;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import java.util.Arrays;
import java.util.List;

import org.junit.Test;

public class ProperStackTests {

	@Test
	public void testPushNotEmpty() {
		
		ProperStack<Integer> stack = new ProperStack<Integer>();
		stack.push(100);
		stack.push(200);
		stack.push(300);
		if(300 == stack.peek()) {
			assertTrue(true);
		}
		
	}
}
