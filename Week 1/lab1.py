from spellchecker import spellchecker
SP = spellchecker('english_words.txt')
def spellcheck(name):
    fcount = 0
    for line in name:
        for word in line.split(" ")
        x = SP.check(line)
        print(x) 
    
def get_file(fname):
    while True:
        try:
            x = open(fname)
            spellcheck(fname)
            break
        except:
            get_file(input('enter a valid file name:\n'))

                        



print('Welcome to Spellchecker')
inp = input('Enter the name of the file you want to spellcheck:\n')
get_file(inp)

        
        
        
