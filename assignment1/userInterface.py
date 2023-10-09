# This file contains all the UI for assignment1. This UI tells the user to
# type run in the console. Once the user does so, the program writes the 
# word run in a text file. Another program will notice this, and generate a random
# integer (i). Then, the userInterface program will read that random integer, and 
# write it to a seperate text file. A third program will take that integer 
# and return the (i)th image from a set of images. Lastly, the userInterface
# will return the image to the user. 

import time
def userInput(out_filename):
    print("Please enter the word 'run' to have the software" 
          "generate your image!")
    
    while True:
        userInput = input()
        if userInput.lower() != 'run':
            print("You must enter the word 'run'")
            continue
        else:
            with open(out_filename, "w") as textfile:
                textfile.write(userInput.lower())
            print('done')
            break


def handleNum(in_filename, out_filename):
    while True:
        with open(in_filename, "r") as textfile:
            randNum = textfile.read()
        if randNum == "" or randNum == "run":
            print('waiting on randNum')
            time.sleep(2)
            continue
        else:
            time.sleep(5)
            with open(in_filename, "w") as infile:
                infile.write("") 
            break
    
    print(randNum)
    with open(out_filename, "w") as textfile:
        textfile.write(randNum)


def generateImage(in_filename):
    while True:
        print("waiting on image path")
        time.sleep(5)
        with open(in_filename, "r") as textfile:
            imagePath = textfile.read()
        if len(imagePath) < 10:
            continue
        break
    time.sleep(5)
    with open(in_filename, "w") as outfile:
            outfile.write("")
    print(imagePath)

if __name__ == "__main__":
    
    userInput("prng-service.txt")
    handleNum("prng-service.txt", "image-service.txt")
    generateImage("image-service.txt")