# #My Taylor Swift Albums C++ program but in Python!

# lists needed for program
numAlbum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
titles = ["Taylor Swift", "Fearless", "Speak Now", "Red", 
          "1989", "reputation", "Lover", "folklore", "evermore", "Midnights", "The Tortured Poets Department"]
# turns all the elements in the list lowercase to compare with the user's input
titlesLower = [title.lower() for title in titles]
taylorsVersion = ["False", "True", "True", "True", "True", "False", "True", "True", "True", "True", "True"]
# intro to user
print("Welcome user to the Taylor Swift Album Info program. The program will ask you for a Taylor Swift album and return information about the album!")
print("Disclaimer: To respect Swift's work, I will be using Taylors Version for the stolen albums.")

# user input and lowercase
albumName = input("Enter an album: ").lower()

# loop to compare two strings
for x in range(len(titles)):
        if albumName == titlesLower[x]:
            print("Album number: " + str(numAlbum[x]))
            print("Album title: " + titles[x])
            print("Is it Taylor's Version (owned by Taylor)? " + taylorsVersion[x])


