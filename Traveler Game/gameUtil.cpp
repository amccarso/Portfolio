/* Austin McCarson, Fall 2015
 
 Game where player has to find way to finish line in as little moves as possible without running out of chi
 
 */
#include "gameUtil.h"
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>

//returns max of cannon powder or teleporter energy
int GameUtil::compute(Square* square, Player* player){
  // TODO: Part 1 debug
    
    //set initial chi, weight, teleporter energy, and cannon powder
  double chi = player->getChi();
  double weight = player->getWeight();
  double teleporterEnergy = square->getTeleporterEnergy();
  double cannonPowder = square->getCannonPowder();

    //compute teleporter energy
  double teleporterCompute = 0;
  for(double i = 0.0; i < floor(chi); i=i+1.0){
    teleporterCompute += sqrt(chi * i * teleporterEnergy);
  }
  teleporterCompute *= 1.0/(1.0 + chi);

    //compute cannon powder
  double cannonCompute = pow(pow(cannonPowder,1.7)/pow(weight,1.5),2)/9.8;

  return std::max(cannonCompute < teleporterCompute ? cannonCompute : teleporterCompute, 1.0);
}

//Function to determine if path being taken is valid
bool GameUtil::isValidPath(std::vector<int>& path, Player* player, Game* game){
  // TODO: Part 2
    
    //create game board
	for (int i = 0; i<Game.size(); i++){
		path.insert(Game[i]);
	}
    
    //if i exceeeds the length of the board then it is an invalid path
	for (int i = 0; i<path.size(); i++){
		if(path[i]<path[i+1]){return true;} else{return false;}
	}
    
    //if board path is not exactly the same as the game board then it is an invalid path
	if(path.begin() == Game.begin()){return true;} else{return false;}
	if(path.end() == Game.end()){return true;} else{return false;}
    
    //check to see if point on path exceeds the possible distance that can be traveled
	if(path[i]+path[i+1]<compute){return true;} else{return false;}
return false;
}

int GameUtil::shortestPathDistance(Game* game, Player* player){
  // TODO: Part 3
  return -1;
}
