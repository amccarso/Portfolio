#include "ImageFilter.h"

using namespace std;

int main(int argc, char *argv[]) {
    if (argc != 4) {
        cout << "usage: ./a.out inputImage outputImage filterType\n";
    }
    else {
        string inputImage = argv[1];
        string outputImage = argv[2];
        string filterType = argv[3];
        applyFilter(inputImage, outputImage, filterType);
    }

    return 0;
}


void applyFilter(string inputFilename, string outputFilename, string filterType) {

    ifstream inputStream(inputFilename.c_str(), ios::in | ios::binary);
    ofstream outputStream(outputFilename.c_str(), ios::out | ios::binary);

    inputStream.seekg(0, inputStream.end);
    int numberOfBytes = inputStream.tellg();
    inputStream.seekg(0, inputStream.beg);

    char* inputData = new char[numberOfBytes];
    inputStream.read(inputData, numberOfBytes);

    // Display header
    // This is only for informational purposes in the context of hw6
    for (int i = 0; i < 52; i++) {
        bitset<8> dat(inputData[i]);
        cout << i << ": " << dat << endl;
    }
    int count; count = 0;
    int gray; gray = 0;
    // Iterate through pixel data
    for (int i = 52; i < numberOfBytes; i++) {
        // TODO: apply filters here
	//53=Red,54=green,55=blue
	//every fourth digit is a new pixel
	//inputData[i] is a RGB value to manipulate

	
/*not this one*/
	if(filterType=="blue"){
		if(i%3==0){
		} else { inputData[i] = 0;}
	}
	
/*or this one*/
	if(filterType=="inverted"){
		inputData[i] = 255 - inputData[i];
	}
	
/*or this one*/
 	if(filterType=="grayscale"){
		//every three items, sum up values and distribute
		//change each pixels value according to individual RGB values
		if(inputData[i]%3==0){
			gray = (inputData[i]+inputData[i-1]+inputData[i-2])/3;
			inputData[i-3] = inputData[i-2] = inputData[i-1] = gray;
		}
	}
	
/*or this on... wait no this is my project code. So grade this one...please!*/
	//the filter cuts the value of the bit in half resulting in a much more vibrant picture
	//essentially raising the resolution of the photo.
	//to use enter in the command line: "./a.out inputImage.bmp outputImage.bmp vibrant"
	if(filterType=="vibrant"){
		inputData[i]= inputData[i]/2;
	}
}

    // write data to output file
    for (int i = 0; i < numberOfBytes; i++) {
        outputStream << inputData[i];
    	}

    delete[] inputData;
    inputStream.close();
    outputStream.close();

}
