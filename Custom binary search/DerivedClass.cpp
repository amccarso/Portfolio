/* Austin McCarson, Fall 2015
 
 Program to use inherited class to get sum and product of elements in array
 and find number in array closest to zero
 
 */

#include <algorithm>
#include "DerivedClass.h"
#include "BaseClass.h"

//empty case
int DerivedClass::findClosestToZero() {
    return this->findClosestToZero(this->numberOfValues-1);
}

//finds number in array closest to zero
int DerivedClass::findClosestToZero(int n) {
    if(n<0){
        return INT_MAX;
    }
    return std::min(std::abs(this->values[n]), this->findClosestToZero(n-1));
}

//returns sum of all values in array
int DerivedClass::getSum(){
    int sum=0;
    for(int i=0; i<this->numberOfValues; i++){
        sum += values[i];
    }
    return sum;
}

//returns product of all values in array
int DerivedClass::getMultiplication(){
    int mult=1;
    for(int i=0; i<this->numberOfValues; i++){
        mult *= values[i];
    }
    return mult;
}


int DerivedClass::evaluateAsPolynomial(int x){
    int eval=0;
    for(int i=this->numberOfValues-1; i>=0; i--){
        eval = (x*eval) + this->values[i];
    }
    return eval;
}

