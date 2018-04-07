/*Austin McCarson, Spring 2016
 
 Program to check if entered string is a palindrome
 */
#include "isPalindrome.h"

int isPalindrome(int num){


// declare variable
	int number; 
	number = num;
	int dig;
	int flip;

// run a loop to flip the number around
	while(number!=0) {
	     dig = number%10;
	     //cout << dig << endl;
	     flip = (flip*10) + dig;
	     //cout << flip << endl;
	     number = number/10;
	     //cout << num << endl;
	}

	cout << "The number written in reverse order is: " << flip << endl;

// state whether the number is a palindrome or not
	if(flip==num){
		cout << "The number is a palindrome!" << endl; }
	else { cout << "The number is not a palindrome :(" << endl; }

	return 0;
}

