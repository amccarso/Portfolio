package edu.buffalo.cse116;

import java.util.ArrayList;
import java.util.List;

/**
 * Companies rely on a problem, known as FizzBuzz, to screen job and internship applicants. Because this problem is so
 * well-known, it really only tests if the applicant has seen the problem before. The rules of FizzBuzz are:
 * <ul>
 * <li>If the entry is at index 0, it should have the value "Empty"</li>
 * <li>Else if the entry is at an index which is a multiple of 15, it should have the value "FizzBuzz"</li>
 * <li>Else if the entry is at an index which is a multiple of 3, it should have the value "Fizz"</li>
 * <li>Else if the entry is at an index which is a multiple of 5, it should have the value "Buzz"</li>
 * <li>Else, it should have the value of the index in String form (e.g., "2" or "13")</li>
 * </ul>
 * You will now write a method demonstrating that you can solve this problem in a manner that you may get to experience
 * again in an interview.
 *
 * @author Matthew Hertz
 */
public class FBSource {

  /**
   * Given a non-null {@link List} and the number of entries to create, this method will first remove entries from
   * {@code fbList} until its size is {@code fillSpace}. It will then go through and either replace an entry (if one is
   * already at that index) or add an entry (if the List does not have an entry at that index) with the proper value
   * using the "FizzBuzz" rules above.<br/>
   * Prerequisites: {@code fbList} is not null AND {@code fillSpace} is greater than or equal to 0.
   *
   * @param fbList List to which the entries, using "FizzBuzz" rules, will be included
   * @param fillSpace Number of entries that should be in the list when you are done
   */
  public static void makeFizzBuzzList(List<String> fbList, int fillSpace) {

	  fbList.clear();
	  
	  for (int x = 0; x < fillSpace; x++) {
		  if (x==0) {
			  fbList.add(0,"Empty");
		  }
		  else if (x%15==0) { fbList.add(x, "FizzBuzz"); }
		  else if (x%5==0) { fbList.add(x, "Buzz"); }
		  else if (x%3==0) { fbList.add(x, "Fizz"); }
		  else {
		  fbList.add(""+x);
		  }
	  }
		
  }
  }