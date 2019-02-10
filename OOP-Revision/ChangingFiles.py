import os

class fileNameChanger:
    i = 1
    def changer(self, dir, pre):

        for fileName in os.listdir(dir):
            dis = dir + "/" + pre + str(self.i) + ".txt"
            src = dir + "/" + fileName

            self.i += 1
            os.rename(src, dis)



if __name__ == '__main__':
    t = fileNameChanger()
    des = input("Enter the path of the directory of the files: ")
    prefix = input("Enter The required prefix to change the names according to: ")
    t.changer(des, prefix)
