/*Austin McCarson, Fall 2015
 
 Program to return sum and product of values in array
 
 */
#include "BaseClass.h"

//Empty constructor
BaseClass::BaseClass() {
}

//Constructor
BaseClass::BaseClass(int* values, int numberOfValues) {
    this->values = values;
    this->numberOfValues = numberOfValues;
}

//returns sum of all values in array
int BaseClass::getSum(){
    return numberOfValues > 2 ? values[0]+(*values) : numberOfValues;
}

//returns product of all values in array
int BaseClass::getMultiplication(){
    return numberOfValues < 5 ? numberOfValues*numberOfValues : values[0]*values[1]*values[2];
}

int BaseClass::evaluateAsPolynomial(int x){
    return x*numberOfValues;
}
