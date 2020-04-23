package edu.buffalo.cse116;

import java.util.Comparator;

/**
 * Class that can be used to compare two {@link NotAmazonItem}s by their rating. We only every want to show ratings from
 * highest to lowest, so this Comparator relies upon "smaller" meaning "appears first" and "larger" to mean "appears
 * later". This should order items such that the item with a HIGHER rating would appear first (e.g., return a value such
 * that the item with the larger rating is "smaller"). If two items have the same rankings, return a value that would
 * denote the item with MORE reviews is "smaller". If items have the same rating and same number of reviews, return that
 * they are equal.
 *
 * @author Matthew Hertz
 */
public class RatingComparator implements Comparator<NotAmazonItem> {

	public int compare(NotAmazonItem first, NotAmazonItem second) {
		
		if (second.getRating() > first.getRating()) {
			return 1;
		}
		else if (first.getRating()==second.getRating()) {
			return second.getReviews()-first.getReviews();
		} else {
			return -1;
		}
	}
}