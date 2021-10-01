import dropbox
import cv2
import random
import time

startTime = time.time()

def takeSnapShot():
    number = random.randint(0,100)
    videoCapture = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCapture.read()
        imgName = "image" + str(number) + ".png"
        cv2.imwrite(imgName, frame)
        startTime = time.time
        result = False
    return imgName
    print("The Image has been taken.")
    videoCapture.release()
    cv2.destroyAllWindows()

def uploadSnapshot(imageName):
    accessToken = "sl.A5g20r0UNXk8jmeWzIjrzcnaUe3_vifbyZvOBby0TPExXnWsEVAly7g6YnLm7KMnFgD0lNhIJ4HKW2E_yrZG6OsHfhbivb0xfOJAY_YXi9e-zXeWT47mT22wsID70pXenY8QdN8"
    file = imageName
    fileFrom = file
    fileTo = "/Image/" + imageName
    dbx = dropbox.Dropbox(accessToken)
    with open(fileFrom,'rb') as f:
        dbx.files_upload(f.read(),fileTo,mode=dropbox.files.WriteMode.overwrite)
        print('Your image has been uploaded successfully!')

def main():
    while(True):
        if((time.time() - startTime) >= 5):
            name = takeSnapShot()
            uploadSnapshot(name)

    main()
    




    