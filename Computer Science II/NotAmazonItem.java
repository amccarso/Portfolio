package edu.buffalo.cse116;

/**
 * Class used to represent items for sale on some hypothetical online store. Any resemblence to real items is entirely
 * coincidental.<br/>
 * (C) 2018 by Matthew Hertz<br/>
 * Posting this file to a website without the explicit written permission of the author is a violation of their
 * copyright.
 * 
 * @author Matthew Hertz
 */
public class NotAmazonItem implements Comparable<NotAmazonItem> {
  /** Amount of money it would take to purchase this item. */
  private double price;

  /** Number of people who have completed reviews of this item. */
  private int reviews;

  /** Average number of stars given to this item in its reviews */
  private double rating;

  /**
   * Creates a new item with the given price, number of reviews, and rating on those reviews
   *
   * @param cost Current purchase price for this item
   * @param evals Number of people who have submitted a review for this item
   * @param avgRating Item's average rating from all of its evaluations
   */
  public NotAmazonItem(double cost, int evals, double avgRating) {
    price = cost;
    reviews = evals;
    rating = avgRating;
  }

  /**
   * Returns the average rating of this item
   *
   * @return Average score across all of the item's ratings
   */
  public double getRating() {
    return rating;
  }

  /**
   * Returns the total number of reviews of this item
   *
   * @return Number of reviews submitted for this item
   */
  public int getReviews() {
    return reviews;
  }
  
  public int compareTo(NotAmazonItem item) {
	  
	  if (this.price > item.price) {
		  return 1;
	  } else if (item.price == this.price) {
		  return 0;
	  } else { return -1; }
	  
  }
}