#Author: Jashanpreet Singh
#Drexel_ID: js4683
#Lab Section: 66
#Purpose: CS172 Homework 2
#Written on: 04/29/2019

class Media(): #the base class for all the media types
    #has the parameters of type of media, name of the media file and its rating
    def __init__(self, typ = '', name = '', rating = 0):
        self.__type = typ
        self.__name = name
        self.__rating = rating

    #all of these methods are getters for each of the parameters
    def getType(self): 
        return self.__type
    def getName(self):
        return self.__name
    def getRating(self):
        return self.__rating
    
    #methods to enable the user to set the attributes to desired values
    def setType(self, option): #
        self.__type = option
    def setName(self, option):
        self.__name = option
    def setRating(self, option):
        self.__rating = option
    #when the Media class is called, it returns a string with the media type, name and rating
    def __str__(self):
        return self.getType() + ': ' + self.getName() +', with a rating of '+ str(self.getRating()) + ' out of 10.'
    
class Movie(Media):
    #a sub-class of Media, which is for movies, in addition to the media's attributes of type, name and media, it also has the attributes of the movies's director name and its runtime.
    def __init__(self, typ = "", name = "", rating = 0, director = "", runtime = 0.0):
        super().__init__(typ, name, rating) #allows us to pass in the appropriate attributes to Media class without repetitve code
        self.__director = director
        self.__runtime = runtime

    #both are the getters for the additional attributes, director name and runtime, of the Movie class
    def getDirector(self):
        return self.__director
    def getRuntime(self):
        return self.__runtime
    
    #allow the user to set to change the additonal attributes,director name and runtime, of the Movie class
    def setDirector(self, option):
        self.__director = option
    def setRuntime(self, option):
        self.__runtime = option
    
    #this is the play method, when called, it returns a string with the name of the movie playing and "playing now"
    def play(self):
        print(super().getName() + ' playing now') #calls the getter method for the media file's name in the Media base class

    #when the class is called upon, this ensures it will return the relevant information about the movie in a string
    def __str__(self):
        return super().__str__() + ' The director is ' + self.getDirector() + ', the movie runs for ' + str(self.getRuntime()) + ' minutes.'

class Song(Media):
    #a sub-class of the Media class, which for songs in the media library, in addition to the media's attribute of type, name and media, it also has the attributes of the artist name and the album the song is from
    def __init__(self, typ = '', name = '', rating = 0, artist = '', album = ''):
        super().__init__(typ, name, rating)
        self.__artist = artist
        self.__album = album
    
    #both are the getters for the additional attributes, artist name and the album, of the Song class
    def getArtist(self):
        return self.__artist
    def getAlbum(self):
        return self.__album
    
    #both methods are setters for the additonal attributes, which allow the user to change or set the aritst name/album name
    def setArtist(self, option):
        self.__artist = option
    def setAlbum(self, option):
        self.__album = option

    #when the class is called, this returns a string which has all the attributes passed through the Media parent class and the additonal attributes of the artist name and the album name
    def __str__(self):
        return super().__str__() + ' The song is by ' + self.getArtist() + ' in the album ' + self.getAlbum() + '.'

    #when the play method is called, it returns the getName method of the Movie base class and the name of the artist
    def play(self):
        print(super().getName() + ' by ' + self.getArtist() + ' playing now')

class Picture(Media):
    #a sub-class of the Media class, which for pcitures in the media library, in addition to the media's attribute of type, name and media, it also has the attribute of the resolution of the picture
    def __init__(self, typ = '', name = '', rating = 0, resolution = 200):
        super().__init__(typ, name, rating)
        self.__resolution = resolution

    #getters for the additonal attribute of resolution
    def getResolution(self):
        return self.__resolution
    
    #setter for the additonal attribute of resolution
    def setResolution(self,option):
        if option >= 200: #ensures no resolution less than 200 is set
            self.__resolution = option
        else:
            print('The minimum resolution of any picture is 200 dpi.')
    
    #when the class is called, this returns a string which has all the attributes passed through the Media parent class and the additonal attribute of resolution
    def __str__(self):
        return super().__str__() + ' It has a resolution of ' + str(self.getResolution()) + ' dpi.'
    
    #when the show method is called, it returns the getName method of the Movie base class
    def show(self):
        print('Showing ' + super().getName() + '.jpeg')