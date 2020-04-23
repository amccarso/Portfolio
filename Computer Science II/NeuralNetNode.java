package edu.buffalo.cse116;

/**
 * Class that defines the functions for a single neuron in a neural network (e.g., an AI algorithm). Since the number of
 * inputs can never change, it is faster (and more logical) for this class to use array than an ArrayList.
 *
 * @author Matthew Hertz
 */
public class NeuralNetNode {

  /** Inputs for this node. For purposes of this homework, the inputs are stored in an array. */
  private double[] inputs;

  /**
   * Weights used by this node. The "learning" in AI occurs by adjusting these weights.
   */
  private double[] weights;

  /**
   * Creates a new node. This stores the given weights array and allocates a new input array. As it the normal case, the
   * input at index 0 is initially set to the value 1.0.
   *
   * @param initialWeight Array of weightings to be used by this neuron
   */
  public NeuralNetNode(double[] initialWeight) {
	weights = initialWeight;  	
	inputs = new double[initialWeight.length];
	inputs[0] = 1.00;
  }

  /**
   * Assign the input at the index stored in {@code index} to have the value {@code newValue}.
   *
   * @param index Index of the input whose value will be updated
   * @param newValue New value for the input being updated.
   */
  public void updateInput(int index, double newValue) {
	  inputs[index] = newValue;
  }

  /**
   * Calculates the "output" of this artificial neuron. This is done by calculating the weighted sum of the inputs. This
   * is done by looping through each entry in the input array. At each index, multiply the values of the input and
   * weighting array at that index and add the result into the sum. Once this sum is completed, compared that sum to
   * {@code threshold}. If the sum is greater then return 1. If the sum is smaller or equal then return -1.
   *
   * @param threshold Threshold value over which this neuron should "fire".
   * @return 1 if the neuron fires and -1 if it does not.
   */
  public int evaluate(double threshold) {
	  
    double sum = 0.0;
    int x = 0;
    
    
    while ( x < weights.length ) {
    		
    	sum = sum + ( weights[x] * inputs[x] );
    	x++;
    	
    }
	if ( sum > threshold ) {
		return 1;
	} else return -1;
	
  }
}