package edu.buffalo.cse116;

/**
 * Class representing a solver for the total distance being traversed.
 *
 * @author Matthew Hertz
 */
public class CalcDistance {
  /**
   * Returns the total distance using the time needed and distance covered in each of the three sections. For students
   * who have forgotten from their algebra class: distance equals rate * time.
   *
   * @param rate1 Velocity of the runner in the section they completed first.
   * @param time1 Time the racer needed to complete their first section.
   * @param rate2 Velocity of the runner in the section they completed second.
   * @param time2 Time the racer needed to complete their second section.
   * @param rate3 Velocity of the runner in the section they completed third
   * @param time3 Time the racer needed to complete their third section.
   */
  public double totalDistance(double rate1, double time1, double rate2, double time2, double rate3,
                              double time3) {
    double distance1 = rate1 * time1;
    double distance2 = rate2 * time2;
    double distance3 = rate3 * time3;
    double retVal = distance1 + distance2 + distance3;
    return retVal;
  }
}