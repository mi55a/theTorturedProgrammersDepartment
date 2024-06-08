
// This program asks for a Taylor Swift album from the user and returns information about the album
// needed libraries
#include <iostream>
#include <string>
#include <cctype>



using namespace std;
// function that converts to lowercase
string LowerString(const string& str) {
    string lowerStr = str;
    for(char &c : lowerStr) {
        c = tolower(static_cast<unsigned char>(c));
    }
    return lowerStr;
}

int main() {
// variables
    string albumName;

    int numAlbum[11] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};

    string titles[] = {"Taylor Swift", "Fearless", "Speak Now", "Red", "1989", "reputation", "Lover", "folklore", "evermore", "Midnights", "The Tortured Poets Department"};

    string taylorsVersion[] = {"False", "True", "True", "True", "True", "False", "True", "True", "True", "True", "True"};

// intro to user
    cout << "Welcome user to the Taylor Swift Album Info program. The program will ask you for a Taylor Swift album and return information about the album!" << endl;
    cout << "Disclaimer: To respect Swift's work, I will be using Taylors Version for the stolen albums." << endl;

    getline(cin, albumName);
// converts to lowercase
    string lowAlbum = LowerString(albumName);
// compares two strings and gives information about album
    for(int i = 0; i < 11; i++) {
        if(lowAlbum == LowerString(titles[i])) {
            cout << "Album number: " << numAlbum[i] << endl;
            cout << "Album title: " << titles[i] << endl;
            cout << "Is it Taylor's Version (owned by Taylor)? " << taylorsVersion[i] << endl;
        }
    }

}

