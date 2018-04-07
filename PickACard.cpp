#include <iostream>
#include <math.h>

int main() {
    //use numbers to represent values of cards and suits
    int cards[13] = {1,2,3,4,5,6,7,8,9,10,11,12,13};
    std::string suits[4] = {"clubs", "diamonds", "hearts", "spades"};
    int randCard = cards[rand()%14];//rand is a number between 1-13
    std::string randSuit = suits[rand()%5];//rand is a number between 1-4
    std::cout << "select a suit: " << std::endl;
    for(int i = 0; i < 4; i++) {
        std::cout << suits[i] << std::endl;
    }
    std::cout << "Enter the suit you would like to choose, or if you wish to quit, enter quit: " << std::endl;
    char choice[8];
    scanf("%s", choice);
    if(strncmp(choice, "quit", 4)) {
        std::cout << "Thanks for using this program!" << std::endl;
        return 0;
    }
    if(choice != randSuit) {
        std::cout << "Sorry, that is not the correct suit." << std::endl;
        std::cout << "Please try again" << std::endl;
        return 0;
    }
    if(choice == randSuit) {
        std::cout << "Congrats! You chose correctly! Now guess the value of the card." << std::endl;
        std::cout << "Possible values are: " << std::endl;
        for(int i = 0; i < 13; i++) {
            std::cout << cards[i] << std::endl;
        }
            char valueChoice[5];
        scanf("%s", valueChoice);
            if(strncmp(valueChoice, "quit", 4)) {
                std::cout << "Thanks for using the program" << std::endl;
                return 0;
            }
            if(std::stoi(valueChoice) == randCard) {
                std::cout << "You are correct! Congrats on the W!" << std::endl;
            }
            if(std::stoi(valueChoice) != randCard) {
                std::cout << "Sorry, that is not correct. Please try again" << std::endl;
                std::cout << "Thanks for playing" << std::endl;
                return 0;
            }
    }
    return 0;
}