import time

def getNum(in_filename):
    while True:
        print('waiting..')
        time.sleep(5)
        with open(in_filename, "r") as textfile:
            randNum = textfile.read()
        if randNum == '':
            continue
        else:
            return randNum


def generateImagePath(randNum, out_filename):
    if int(randNum) > 202:
        randNum = str(int(randNum) % 202)
    time.sleep(3)
    print("/Users/jackdugan/Desktop/cs361/assignment1/horses/horse-" + randNum + ".jpg")
    with open(out_filename, "w") as textfile:
        textfile.write("/Users/jackdugan/Desktop/cs361/assignment1/horses/horse-" + randNum + ".jpg")


if __name__ == "__main__":
    randNum = getNum("image-service.txt")
    generateImagePath(randNum, "image-service.txt")

