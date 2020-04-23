package edu.buffalo.cse116;

/**
 * This class was created to include a method used by students to use recursion to count the number of Entrys in a linked list
 * whose element is a negative number.
 *
 * @author Matthew Hertz
 */
public class CountNegatives {

  /**
   * Method that returns the number of {@link Entry} instances whose element is negative.
   * One way to think about how we would solve this problem is:
   * <ul>
   * <li>If {@code ent} is null, then there are no Entrys and so the answer must be 0.</li>
   * <li>If {@code ent} is not null AND {@code ent}'s element is LESS THAN 0, then the answer is:<br/>
   * 1 + the number of Entrys starting from the Entry following {@code ent} whose element is negative</li>
   * <li>If {@code ent} is not null AND {@code ent}'s element is GREATER THAN OR EQUAL TO 0, then the answer is:<br/>
   * the number of Entrys starting from the Entry following {@code ent} whose element is negative</li>
   * </ul>
   *
   * @param ent Entry at the start of the linked list whose elements we are checking.
   * @return Number of Entrys starting from {@code ent} with a negative element
   */
  public static int numNegative(Entry<Integer> ent) {
	  if(ent == null) {
		  return 0;
	  }
	  if(ent.getElement() < 0) {
		  return numNegative(ent.getNext())+1;
	  }
	  else {
		  return numNegative(ent.getNext());
	  }

  }
}