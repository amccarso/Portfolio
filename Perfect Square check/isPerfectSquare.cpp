#include "isPerfectSquare.h"

int isPerfectSquare(int num){

/* Instantiate variables and find square root*/
int number; number = num;
double dub_root = sqrt(number);
int int_root = dub_root;

/* Check to see if the number is a perfect square or not
if(dub_root == int_root){
	cout << "The number is a perfect square!" << endl;
} else { cout << "The number is not a perfect square" << endl; }

/* Print the square root */
cout << "The square root of the number is: " << dub_root << endl;

return 0;

}
