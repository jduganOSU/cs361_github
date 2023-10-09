import time
import random

def readFile(in_filename):
    while True:
        with open(in_filename, "r") as textfile:
            userInput = textfile.read()
            if userInput != 'run':
                print('waiting..')
                time.sleep(3)
                continue
            else:
                break


def generateInt(out_filename):
    time.sleep(5)
    randNum = random.randint(1, 300)
    print(randNum)
    with open(out_filename, "w") as textfile:
        textfile.write(str(randNum))


if __name__ == "__main__":
    readFile("prng-service.txt")
    generateInt("prng-service.txt")