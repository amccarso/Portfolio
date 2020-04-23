package edu.buffalo.cse116;

/**
 * This class can be used to compute a few statistics for a given data set. This will compute both the average and
 * standard deviation.
 *
 * @author Matthew Hertz
 */
public class StatUtils {

  /**
   * Compute the mean value of the data in the array.
   *
   * @param arr Array of doubles whose average we want to compute.
   * @return Mean of the values in {@code data}.
   * @throws NoDataException Exception thrown if arr is null.
   * @throws DivideByZeroException Exception thrown when the array does not contain anything (its length is 0).
   */
  public static double computeMean(double[] arr) throws DivideByZeroException, NoDataException {
  if(arr == null) {
	  throw new NoDataException();
  }
  else if(arr.length == 0) {
	  throw new DivideByZeroException();
  }
  
  double retval = 0.0;
  
  for ( int x = 0; x < arr.length; x++ ) {
	  retval += arr[x];
  }
  
  retval = retval/arr.length;
  
  return retval;
  
  }

  /**
   * Computes the standard deviation of the data in the array.
   *
   * @param arr Array of doubles whose standard deviation we want to compute.
   * @return Standard deviation of the values in {@code data}.
   * @throws InvalidDataSetException Exception thrown when the array is not large enough to compute a standard deviation
   *           (its length is 1).
   * @throws NoDataException Exception thrown when arr is null.
   */
  public static double computeStdDev(double[] arr) throws InvalidDataSetException, NoDataException {

	  double retval = 0.0;
	  double mean = 0.0;
	  
	  if(arr == null) {
		  throw new NoDataException();
	  }
	  if(arr.length == 1) {
		  throw new InvalidDataSetException();
	  }
	  try {
		mean = computeMean(arr);
	  } catch (NoDataException | DivideByZeroException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
		return 0;
	  } 
	  
	  for(int x = 0; x < arr.length; x++) {
		  try {
			retval += Math.pow(arr[x]-computeMean(arr),2);
		  } catch (DivideByZeroException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	  }
	  return Math.sqrt(retval/(arr.length-1));
  }
}
