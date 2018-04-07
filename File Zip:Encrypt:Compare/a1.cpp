/*
 * CSE 250 Fall 2017
 * Assignment 1
 * Name: Austin McCarson
 * Person number: 50103630
 *
 * Note: the only includes you are allowed in this file are <fstream>,
 * <string>, and <algorithm>. Additional includes will cause your code
 * to be disregarded by the grader and receive 0 points.
 *
 * You must complete all of your work within this a1.cpp file.
 */

#include <fstream>
#include <string>
#include <algorithm>


/**
 * compute_filesize
 * A helper function to perform the computation of the size of the file.
 *
 * @param file - A valid open file.
 * @return The size of the file that was input.
 *         Upon return, the stream position is at the start of the file with all flags cleared.
 */
inline int compute_filesize(std::ifstream& file) {
    // Variables to store the positions for the start and end of the file.
    std::streampos fileStart, fileEnd;

    // Seek to end of the file.
    file.seekg(0, std::ios::end);
    // Get the end of file position.
    fileEnd = file.tellg();
    // Seek to start of the file.
    file.seekg(0, std::ios::beg);
    // Get the start of file position.
    fileStart = file.tellg();

    // Clear any bad flags.
    file.clear();

    return fileEnd - fileStart;
}


/**
 * cmp_files
 * Open the two files provided and compare them bytewise for equality.
 * Note that we assume that both files exist. If this is not the case,
 * this code will produce runtime errors.
 *
 * @param lhsFilename - A (relative) path to one file to compare.
 * @param rhsFilename - A (relative) path to another file to compare.
 * @return true - if the two files are the same bytewise.
 *         false - if the two files differ (either in size or in contents).
 */
bool cmp_files(const std::string& lhsFilename, const std::string& rhsFilename) {
    // Open lhs file in binary mode.
    std::ifstream lhsInputFile(lhsFilename, std::ios::binary);

    // Get the lhs file size in bytes.
    const int lhsFilesize = compute_filesize(lhsInputFile);
    // Compute the number of "blocks" in the lhs file.
    const int lhsNumBlocks = lhsFilesize / 4;

    // We want to treat data as 4 byte blocks (and know the size is divisible by 4).
    // We can do this by loading data in as 32 bit values from the binary file.
    uint32_t* lhsFileData = new uint32_t[lhsNumBlocks];

    // Read the lhs input file into the data array.
    lhsInputFile.read((char*) (lhsFileData), lhsFilesize);

    // Close the input file.
    lhsInputFile.close();

    // Open files in binary mode.
    std::ifstream rhsInputFile(rhsFilename, std::ios::binary);

    // Get the rhs file size in bytes.
    const int rhsFilesize = compute_filesize(rhsInputFile);
    // Compute the number of "blocks" in the rhs file.
    const int rhsNumBlocks = rhsFilesize / 4;

    // We want to treat data as 4 byte blocks (and know the size is divisible by 4).
    // We can do this by loading data in as 32 bit values from the binary file.
    uint32_t* rhsFileData = new uint32_t[rhsNumBlocks];

    // Read the rhs input file into the data array.
    rhsInputFile.read((char*) (rhsFileData), rhsFilesize);

    // Close the input file.
    rhsInputFile.close();

    // Compute whether the file data are equal or not.
    // Note that if the size is different, this doesn't run into issues because the && short circuits to false.
    bool returnValue = lhsFilesize == rhsFilesize && std::equal(lhsFileData, lhsFileData + lhsNumBlocks, rhsFileData);

    // Clean up allocated memory.
    delete[] lhsFileData;
    delete[] rhsFileData;

    // Return if they are equal or not.
    return returnValue;
}

/**
 * unzip_file
 * Opens a file and shifts alternating blocks of 4 bytes to the front or back of the file, respectively.
 * Writes a new output file with the same filename as the input with the appended suffix "-unzipped"
 * Note that we assume that the file exists. If this is not the case, this code will produce runtime errors.
 *
 * @param filename - A (relative) path to a file to perform the unzip operation on.
 */
void unzip_file(const std::string& filename) {
    // Open file in binary mode.
    std::ifstream inputFile(filename, std::ios::binary);

    // Compute the file size in bytes.
    const int filesize = compute_filesize(inputFile);
    const int numBlocks = filesize / 4;

    // We want to treat data as 4 byte blocks.
    // We can do this by loading data in as 32 bit values from the binary file.
    uint32_t* fileData = new uint32_t[numBlocks];

    // Read the input file into the data array.
    inputFile.read((char*) (fileData), filesize);

    // Close the input file.
    inputFile.close();

    // Our output data should have the same size as the input file.
    uint32_t* outputFileData = new uint32_t[numBlocks];


    // First "odd positioned" block to write is at the first block of the file data.
    uint32_t* currentBlock = fileData;

    // First "odd positioned" block in to write in output is the first block.
    uint32_t* currentOutputBlock = outputFileData;

    for (int i = 0; i < (numBlocks + 1) / 2; ++i) {
        // Load block to output file.
        (*currentOutputBlock) = (*currentBlock);

        // Move odd block output position by one.
        currentOutputBlock++;

        // Move pointer to next block to write (skip over 1).
        currentBlock += 2;
    }

    // First "even positioned" block in the input is at the second block of the data.
    currentBlock = fileData + 1;

    // First "even positioned" block in to write in output is the first block (+1 if odd number of blocks).
    currentOutputBlock = outputFileData + (numBlocks + 1) / 2;

    for (int i = 0; i < numBlocks / 2; ++i) {
        // Load block to output file.
        (*currentOutputBlock) = (*currentBlock);

        // Move even block output position by one.
        currentOutputBlock++;

        // Move pointer to next block to write (skip over 1).
        currentBlock += 2;
    }

    // Open output file with -unzipped appended to the original filename.
    std::string outputFilename = filename + "-unzipped";
    std::ofstream outputFile(outputFilename, std::ios::binary);

    // Write output data
    outputFile.write((char*) (outputFileData), filesize);

    // Close file to ensure it is written properly.
    outputFile.close();

    // Clean up file data that was loaded into memory.
    delete[] fileData;

    // Clean up output data that was created.
    delete[] outputFileData;
}

/**
 * zip_file
 * Opens a file and moves alternating blocks of 4 bytes alternating from the front and middle of the file,
 * to follow one another. This process is the reverse of the unzip_file operation.
 * Writes a new output file with the same filename as the input with the appended suffix "-zipped"
 * Note that we assume that the file exists. If this is not the case, this code will produce runtime errors.
 *
 * @param filename - A (relative) path to a file to perform the zip operation on.
 */
void zip_file(const std::string& filename) {
    // Open file in binary mode.
    std::ifstream inputFile(filename, std::ios::binary);

    // Compute the file size in bytes.
    const int filesize = compute_filesize(inputFile);
    const int numBlocks = filesize / 4;

    // We want to treat data as 4 byte blocks.
    // We can do this by loading data in as 32 bit values from the binary file.
    uint32_t* fileData = new uint32_t[numBlocks];

    // Read the input file into the data array.
    inputFile.read((char*) (fileData), filesize);

    // Close the input file.
    inputFile.close();

    // Our output data should have the same size as the input file.
    uint32_t* outputFileData = new uint32_t[numBlocks];


    // First "odd positioned" block to write is at the first block of the file data.
    uint32_t* currentBlock = fileData;

    // First "odd positioned" block in output is the first block.
    uint32_t* currentOutputBlock = outputFileData;

    for (int i = 0; i < (numBlocks + 1) / 2; ++i) {
        // Load block to output file.
        (*currentOutputBlock) = (*currentBlock);

        // Move to next odd block to output (skip over 1).
        currentOutputBlock += 2;

        // Move pointer to next block to write.
        currentBlock++;
    }

    // First "even positioned" block in the input is at the second block of the data (+1 if odd number of blocks).
    currentBlock = fileData + (numBlocks + 1) / 2;

    // First "even positioned" block in to write in output is the first block.
    currentOutputBlock = outputFileData + 1;

    for (int i = 0; i < numBlocks / 2; ++i) {
        // Load block to output file.
        (*currentOutputBlock) = (*currentBlock);

        // Move to next even block to output (skip over 1).
        currentOutputBlock += 2;

        // Move pointer to next block to write.
        currentBlock++;
    }

    // Open output file with -unzipped appended to the original filename.
    std::string outputFilename = filename + "-zipped";
    std::ofstream outputFile(outputFilename, std::ios::binary);

    // Write output data
    outputFile.write((char*) (outputFileData), filesize);

    // Close file to ensure it is written properly.
    outputFile.close();

    // Clean up file data that was loaded into memory.
    delete[] fileData;

    // Clean up output data that was created.
    delete[] outputFileData;
}

/**
 * encrypt_file
 * Opens a file and encrypts the file by bytewise XORing the file bytes with the bytes of a given password.
 * If the file is longer than the password, we cycle back to the beginning of the password as needed.
 * Writes a new output file with the same filename as the input with the appended suffix "-encrypted"
 * Note that we assume that the file exists. If this is not the case, this code will produce runtime errors.
 *
 * @param filename - A (relative) path to a file to perform the encryption operation on.
 * @param password - A non-empty string.
 */
void encrypt_file(const std::string& filename, const std::string& password) {
    // Open file in binary mode.
    std::ifstream inputFile(filename, std::ios::binary);

    // Compute the file size in bytes.
    const int filesize = compute_filesize(inputFile);

    // We want to act on the bytes in the file so we load the data as characters.
    char* fileData = new char[filesize];

    // Read the input file into the data array.
    inputFile.read(fileData, filesize);

    // Close the input file.
    inputFile.close();

    // Open output file with -encrypted appended to the original filename.
    std::string outputFilename = filename + "-encrypted";
    std::ofstream outputFile(outputFilename, std::ios::binary);

    const char* endOfData = fileData + filesize;
    char* currentByte = fileData;

    // Get sequence of characters from the password string.
    const char* passwordArray = password.c_str();

    // Get start of password sequence.
    const char* currentChar = passwordArray;

    // Get end of password sequence.
    const char* const endOfPassword = passwordArray + password.length();

    while (currentByte != endOfData) {
        *currentByte = *currentByte ^ *currentChar;
        currentByte++;
        currentChar++;
        if (currentChar == endOfPassword) {
            // Reset current char to the start of the password.
            currentChar = passwordArray;
        }
    }

    // Write the "encrypted" data to the output file.
    outputFile.write(fileData, filesize);

    // Close file to ensure it is written properly.
    outputFile.close();

    // Clean up memory allocated to hold file data.
    delete[] fileData;
}

/**
 * crack_file
 * Opens two files, one which is any file and the second which is an encrypted version of the file.
 * This uses the respective data from the two files to recover the password that was used to create the encrypted file.
 * Note that we assume that both files exist. If this is not the case, this code will produce runtime errors.
 *
 * @param originalFilename - A (relative) path to a file to any file.
 * @param encryptedFilename - A (relative) path to a file to an encrypted version of the original file.
 * @return A string containing as much of the password as possible that can be recovered given the two files.
 */
std::string crack_file(const std::string& originalFilename, const std::string& encryptedFilename) {
    // Open original file and read data.
    std::ifstream originalInputFile(originalFilename, std::ios::binary);

    // Compute the file size in bytes.
    const int filesize = compute_filesize(originalInputFile);

    // We want to act on the bytes in the file so we load the data as characters.
    char* originalFileData = new char[filesize];

    // Read the input file into the data array.
    originalInputFile.read(originalFileData, filesize);

    // Close the input file.
    originalInputFile.close();

    // Open encrypted file and read data.
    std::ifstream encryptedInputFile(encryptedFilename, std::ios::binary);

    // We want to act on the bytes in the file so we load the data as characters.
    char* encryptedFileData = new char[filesize];

    // Read the input file into the data array.
    encryptedInputFile.read(encryptedFileData, filesize);

    // Close the input file.
    encryptedInputFile.close();

    // XOR the two files together, storing the result in the array for the original data.
    const char* originalEndOfData = originalFileData + filesize;
    char* originalCurrentByte = originalFileData;
    char* encryptedCurrentByte = encryptedFileData;

    while (originalCurrentByte != originalEndOfData) {
        // Update the original data to store the result of the XOR.
        *originalCurrentByte = *originalCurrentByte ^ *encryptedCurrentByte;
        originalCurrentByte++;
        encryptedCurrentByte++;
    }

    // Find where the password repeats.
    std::string password;

    // Password must be between 1 and length of file characters long.
    for (int passwordLength = 1; passwordLength <= filesize; ++passwordLength) {
        password = std::string(originalFileData, passwordLength);
        originalCurrentByte = originalFileData;
        const char* passwordArray = password.c_str();
        const size_t currentPasswordLength = password.length();
        size_t position = 0;
        for (; position < filesize; ++position) {
            if (originalFileData[position] == passwordArray[position % currentPasswordLength]) {
                continue;
            }
            else {
                break;
            }
        }
        if (position == filesize) {
            break;
        }
    }
    return password;
}