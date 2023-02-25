import os
import shutil
from datetime import datetime
import pathlib
import pickle

version = 1.03
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
        for f in os.listdir(self.currentDir):
            try:
                filename, ext = os.path.splitext(f)
                size = os.path.getsize(os.path.join(self.currentDir,f))
                if size>600000000 and ext in [".exe",".msi"]:
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
        fileNames = []
        for f in os.listdir(self.currentDir):
            print(f)
            #unixTimeStamp = os.path.getmtime(os.path.join(self.currentDir,f))
            unixTimeStamp = pathlib.Path(os.path.join(self.currentDir,f)).stat().st_mtime
            print(unixTimeStamp)
            dateTime = datetime.utcfromtimestamp(unixTimeStamp).strftime('%Y-%m-%d %H:%M:%S')
            dateTimeNow = datetime.now()
            print(dateTime,dateTimeNow)
            
    def allocateFolder(self, dirAllocate):
        try:
            dirAllocate = os.path.join(dirAllocate,"allocated.cleaner")
            with open(dirAllocate,"wb+") as files:
                pickle.dump(version,files)
                return True
        except FileExistsError as fe:
            return False
        except Exception as e:
            print(e)
    
    def trash(self):
        fileNames = []
        try:
            os.mkdir(os.path.join(self.currentDir, "Trash"))
        except FileExistsError:
            pass
        except:
            print('got an error in creating a folder')
        
        for f in os.listdir(self.currentDir):
            try:
                filename, ext = os.path.splitext(f)
                if ext not in ["",".BIN"]:
                    shutil.move(
                    os.path.join(self.currentDir, f'{filename}{ext}'),
                    os.path.join(self.currentDir, "Trash" , f'{filename}{ext}'))
            except (FileNotFoundError, PermissionError):
                pass
            
            

if __name__ == "__main__":
    pass