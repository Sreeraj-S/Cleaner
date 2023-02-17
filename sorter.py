import os
import shutil

current_dir = os.getcwd()

class Sorter:
    def __init__(self,currentDir):
        self.currentDir = currentDir

    def moveFile(self,folderName,file_ext):
        fileNames = []
        try:
            os.mkdir(os.path.join(self.currentDir, folderName))
        except FileExistsError:
            pass
        except:
            print('got an error in creating a folder')
        
        for f in os.listdir(self.currentDir):
            try:
                filename, ext = os.path.splitext(f)
                if ext == file_ext:
                    fileNames.append(filename)
            except (FileNotFoundError, PermissionError):
                pass
        for filename in fileNames:
            shutil.move(
                    os.path.join(self.currentDir, f'{filename}{file_ext}'),
                    os.path.join(self.currentDir, folderName , f'{filename}{file_ext}'))
            
    def deleteSetupFiles(self):
        fileNames = []
        print("started")
        for f in os.listdir(self.currentDir):
            print(f)
            try:
                filename, ext = os.path.splitext(f)
                size = os.path.getsize(os.path.join(self.currentDir,f))
                print(size)
                if size>600000000 and ext in [".exe",".msi"]:
                    print('in')
                    fileNames.append(f)
            except (PermissionError):
                pass
            except FileNotFoundError as e:
                print(e)

        try:
            for f in fileNames:
                os.remove(os.path.join(self.currentDir,f))
        except PermissionError:
            pass
    def oldFiles(self):
        pass

if __name__ == "__main__":
    pass