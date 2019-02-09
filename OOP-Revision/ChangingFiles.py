import os

class FileNameChanger:
    i = 1
    def changer(self, dirName, obj):
        for fileName in os.listdir(dirName ):
            desired = obj + str(i) + '.txt'
            src = dirName + fileName
            desired = dirName + desired

            os.rename(src, desired)

        i += 1

