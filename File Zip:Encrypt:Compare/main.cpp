#include <iostream>

bool cmp_files(const std::string& lhsFilename, const std::string& rhsFilename);

void unzip_file(const std::string& filename);

void zip_file(const std::string& filename);

void encrypt_file(const std::string& filename, const std::string& password);

std::string crack_file(const std::string& originalFilename, const std::string& encryptedFilename);

int main() {
    std::string testFilename;

    // Tests your cmp_files function on test01 through test09
    for (int i = 1; i <= 9; ++i) {
        testFilename = std::string("test0") + (char) (i + 48);
        if (cmp_files(testFilename, testFilename)) {
            std::cout << "cmp_files correctly checks that " << testFilename << " is equal to itself!" << std::endl;
        } else {
            std::cout << "Something went wrong comparing the file with itself. :(" << std::endl;
            return -1;
        }
    }

    // Tests your unzip_file function on test01 through test09
    for (int i = 1; i <= 9; ++i) {
        testFilename = std::string("test0") + (char) (i + 48);
        // Test your unzip_file function.
        unzip_file(testFilename);
        if (cmp_files(testFilename + "-unzipped", testFilename + "-unzipped-expected")) {
            std::cout << "Unzipping the file went as expected!" << std::endl;
        } else {
            std::cout << "Something went wrong unzipping the file. :(" << std::endl;
            return -1;
        }
    }

    // Tests your zip_file function on test01 through test09
    for (int i = 1; i <= 9; ++i) {
        testFilename = std::string("test0") + (char) (i + 48);
        zip_file(testFilename + "-unzipped");

        if (cmp_files(testFilename, testFilename + "-unzipped" + "-zipped")) {
            std::cout << "Unzipping and then zipping successfully restored the file" << testFilename << "!"
                      << std::endl;
        } else {
            std::cout << "Something went wrong unzipping and then zipping" << testFilename << " :(" << std::endl;
            return -1;
        }
    }

    // Tests your encrypt_file function on test01 through test09
    for (int i = 1; i <= 9; ++i) {
        testFilename = std::string("test0") + (char) (i + 48);
        encrypt_file(testFilename + "-unzipped", "password");
        if (cmp_files(testFilename + "-unzipped-encrypted", testFilename + "-unzipped-encrypted-expected")) {
            std::cout << "Encryption was correctly performed for " << testFilename << "!" << std::endl;
        } else {
            std::cout << "Something went wrong encrypting " << testFilename << " :(" << std::endl;
            return -1;
        }
    }

    // Tests your crack_file function on test01 through test09
    for (int i = 1; i <= 9; ++i) {
        testFilename = std::string("test0") + (char) (i + 48);
        std::string password = crack_file(testFilename + "-unzipped", testFilename + "-unzipped-encrypted");
        if (password.compare("password") == 0 || (i == 7 && password.compare("pass") == 0)) {
            std::cout << "Password was successfully decipherd for " << testFilename << "!" << std::endl;
            std::cout << "The password you found is: \"" << password << "\"\n" << std::endl;
        } else {
            std::cout << "Something went wrong deciphering the password for " << testFilename << " :(" << std::endl;
            return -1;
        }
    }
    return 0;
}