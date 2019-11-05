#Author: Jashanpreet Singh
#Drexel_ID: js4683
#Lab Section: 66
#Purpose: CS172 Homework 2
#Written on: 04/29/2019

from media import Movie, Song, Picture #to import our classes

#dictionary with objects of each class and sorted by the type of object
media = {
    'Movies': [
        Movie('Movie', 'Batman: The Dark Knight', 10, 'Christopher Nolan', 152),
        Movie('Movie', 'Avengers', 9.4, 'Anthony Russo and Joe Russo', 160),
        Movie('Movie','Superman', 9.8, 'Richard Donner', 188),
        Movie('Movie', 'The Conjuring 2', 8.2, 'James Wan', 134),
        Movie('Movie', 'Jaws', 8.8, 'Steven Spielberg', 130)
    ],
    'Songs': [
        Song('Song', 'Thriller', 9.9, 'Micheal Jackson', 'Thriller'),
        Song('Song', 'Old Town Road', 5.6, 'Lil Nas X', 'Old Town Road'),
        Song('Song','XO Tour Llif3', 10, 'Lil Uzi Vert', 'Luv Is Rage 2'),
        Song('Song', "God's Plan", 3.5, 'Drake', 'Scorpion'),
        Song('Song', "Sanguine Paradise", 9.9, 'Lil Uzi Vert', 'Eternal Atake')
    ],
    'Pictures': [
        Picture('Picture', 'Joseph', 5.8, 300),
        Picture('Picture', 'CS', 9.5, 250),
        Picture('Picture', 'Photo', 6.8, 450),
        Picture('Picture','Image', 7.6, 500),
        Picture('Picture','Hello', 8.7, 212)
    ]
}

def allfunction(userInpLower): #a function which will list all of the items in each key
    mediaKey = '' #variable which will be the key
    #sets the variable according to the user input
    if userInpLower == 'all songs': mediaKey = 'Songs'
    elif userInpLower == 'all movies': mediaKey = 'Movies'
    else: mediaKey = 'Pictures'
    print('\nThese are the {} in the libray.'.format(mediaKey)) #a title which tells the user which option they picked
    print('----------------------------------')
    counter = 1 #variable to number each item in the key when listed
    for item in media[mediaKey]: #to get each item in the key the user selected by typing in a specifc command
        print(str(counter) + '.', item)
        counter += 1
    print('')
print('Welcome to the Media Player')#welcome message
print('---------------------------')

while True: #a loop which keeps the program running and validates the input until the user quits 
    userInp = input("\n Enter 'All' to display all items in the library. \n Enter 'All songs' to only display songs. \n Enter 'All movies' to only display movies. \n Enter 'All pictures' to only display pictures. \n Enter 'song' to play a song. \n Enter 'movie' to play a movie. \n Enter 'picture' to display a picture. \n Enter 'quit' to quit the program \n")
    userInpLower = userInp.lower() #to get rid of the nuances of a string literal

    if userInpLower == 'all': #handles if the user decides to display all of the files
        for key, value in media.items(): #a for loop to loop through each key and its values
            print('\n' + key) #prints the title of the objects it is about to display, which is songstored in the key
            print('')
            for item in value: #loops through each value stored in each keys
                print(item)
    elif userInpLower == 'all songs' or userInpLower == 'all movies' or userInpLower == 'all pictures': #handles if the input is to display only one type of files
        allfunction(userInpLower) #calls the function to list the user's selection

    elif userInpLower == 'song' or userInpLower == 'movie': #handles if the user decided to play a specific movie or song
        mediaKey = userInpLower #sets the mediakey to the user input which is the type of media they want to play
        userInp2 = 'all ' + userInpLower + 's'
        allfunction(userInp2) #call to function to list all the items of the category selected available in the library
        userInp2 = input('Enter the name of the {} you want to play:\n'.format(mediaKey)) #asks for the name of the specific media file they want to play
        mediaKey = userInpLower.capitalize() + 's' #adds an "s" as the input will now match the keys stored
        for item in media[mediaKey]: #loops through each item in the key selected
            if userInp2.lower() == item.getName().lower(): #if the second input matches the name of an item stored then play
                    item.play()
                    print('')
                    break
        else: #handles if the media file is not in the library
            print( userInp2 + ' is not in the media library.')
            print('')
    elif userInpLower == 'picture': #if the user decides to see a specific picture 
        allfunction(userInpLower)
        mediaKey = userInpLower #gets rid of the nuances
        userInp2 = input('Enter the name of the {} you want to see:\n'.format(mediaKey)) #asks for the name of the picture
        mediaKey = 'Pictures' 
        for item in media[mediaKey]: #loops through the pictures key
            if userInp2.lower() == item.getName().lower(): #if the name matches one of the items then show
                    item.show()
                    print('')
                    break
        else: #handles if the media file is not in the library
            print( userInp2 + ' is not in the media library.')
            print('')
    elif userInpLower == 'quit': #if the user decides to quit
        break
    else: #handles if input is not of the options listed
        print('\nInvalid Response')
        print("Let's try again.\n")