#include "PacketsToFile.h"


// Reassembles a queue of packets into a the contents of a file. Assumes the packets are given in sequence order.
vector<char> packetsToFile(queue<Packet> packets){
    vector<char> fileContents;
	queue<Packet> packs = packets;
    // TODO: Reassemble the contents of each packet into the full contents of the original file
	packs.front();
    return fileContents;
}

// Takes two command line parameters.
// The first is the output file where the queue of packets is saved  which can be loaded by calling loadPackets
// provided in Packet.cpp/h.
// The second parameter is an output file where the reassembled file will be saved.
//
// usage: ./a.out inputFilename outputFilename
int main(int argc, char *argv[]){

    // TODO: Reassemble the original file from a saved queue of packets and save the file
	string filename; cin >> filename;
	string output = *argv;
	queue<Packet> packets = loadPackets(filename);
	vector<char> out = packetsToFile(packets);

}
