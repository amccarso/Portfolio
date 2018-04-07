/*Austin McCarson, Fall 2015

Program to count characters in a string
 
 */
#include "Character_counter.h"
#include <iostream>

std::string getCustomString();
int countChars(std::string, char);
int countCharsCustom(char);


std::string getCustomString(){
    return "Austin McCarson and then some more words";
}

/*@parameters
    word - the word that is being iterated through
    characer - character that is being looked for
 
 @return number of times the character appears in the word
 
 */
int countChars(std::string word, char character){
    int count=0;
    for(int i=0; i<words.length(); i++){
        if(words[i] == character){
            count++;
        }
    }
    return count;
}


int countCharsCustom(char character){
    return countChars(getCustomString(), character);
}
