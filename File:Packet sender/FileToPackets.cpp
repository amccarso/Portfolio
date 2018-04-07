#include "FileToPackets.h"
#include "Packet.h"

// Takes a file and returns the file contents in packets each with a payload size less than or equal to maxPayloadSize
// The queue must be returned in sequence order with the front of the queue containing the contents at the beginning
// of the file.
queue<Packet> fileToPackets(string filename, int maxPayloadSize){
    queue<Packet> packets;
	vector<char> payload;
	int sequenceNumber; sequenceNumber = 0;
	Packet pack_it;
	string file = filename;
//steal code from hw6 to open file
	ifstream inputStream(filename.c_str(), ios::in | ios::binary);

	inputStream.seekg(0, inputStream.beg);
	int numberOfBytes = inputStream.tellg();
	inputStream.seekg(0, inputStream.end);

	char* inputData = new char[numberOfBytes];
	inputStream.read(inputData, numberOfBytes);
    // TODO: Chop the file into packets
//need filename, sequenceNumber, payload
//add info from file to payloads. each payload should contain a portion of the file info
//store packet into queue of packets	
//use for loop to store info into payload and if statement to store full payload into packet into queue
	for(int i = 0; i<numberOfBytes; i++){
		vector<char> acket(maxPayloadSize);
		for (int j = i; j<maxPayloadSize; j++){
			payload.push_back(inputData[j]);
			i = j+1;
		}
		sequenceNumber++;
		packets.push(pack_it(file, sequenceNumber, payload));		
	}
    return packets;
}

// Takes three command line parameters.
// The first is an input file to be converted into packets.
// The second is the output file where the queue of packets will be saved by calling savePackets provided in Packet.cpp/h
// The third parameter is the maximum payload size for each packet. All packets except the last should have this payload
// size.
//
// usage: ./a.out inputFilename outputFilename payloadSize
int main(int argc, char *argv[]){

    // TODO: Convert a file into a queue of packets and save the queue to a file

	string inputfile; cin >> inputfile;
	string outputfile; cin >> outputfile;
	int maxPayloadSize; cin >> maxPayloadSize;
	queue<Packet> packets = fileToPackets(inputfile, maxPayloadSize);
	savePackets(packets, outputfile);
}
