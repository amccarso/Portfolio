/*Austin McCarson, Fall 2015
 
 Class to create board square
 Contains Cannon and teleporter attributes
 */
#include "square.h"

//Board square constructor, sets cannon powder and teleporter energy
Square::Square(double cannon_powder, double teleporter_energy) :
  _cannon_powder(cannon_powder),
  _teleporter_energy(teleporter_energy) {}

//returns cannon powder
double Square::getCannonPowder() const { return _cannon_powder; }

//returns teleporter energy
double Square::getTeleporterEnergy() const { return _teleporter_energy; }
