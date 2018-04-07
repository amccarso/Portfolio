/*Austin McCarson, Fall 2015
 
 Class to set player attributes and get Weight and Chi
 
*/
#include "player.h"

//Player Constructor
Player::Player(double weight, double chi) : _weight(weight), _chi(chi) {}

//get weight of player
double Player::getWeight() const {
  return _weight;
}

//get players chi level
double Player::getChi() const {
  return _chi;
}
