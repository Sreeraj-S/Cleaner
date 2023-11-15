# Importing Library

import os
import datetime
import time 
import shutil
import json
import math
from tqdm import tqdm

#Defining

INFOLOC ="info.json"
CURDIR = os.getcwd()
listFile = os.listdir(CURDIR)
listFileDetails = {}
global count
count = 1

# Functions
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
    
listFileDetails = {}

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])
    
def FindFile(dirPath):
    with os.scandir(dirPath) as entries:
        for entry in entries:
            if entry.is_file():
                filename,ext = os.path.splitext(entry.path)
                creationTime = os.path.getctime(entry.path)
                creationTime = datetime.date.fromtimestamp(creationTime)
                modificationTime = os.path.getmtime(entry.path)
                modificationTime = datetime.date.fromtimestamp(modificationTime)
                currDate = datetime.date.today()
                diffFromCreationDate = currDate-creationTime 
                diffDate = currDate-modificationTime
                creationTime = str(creationTime)
                modificationTime = str(modificationTime)
                fileSize = os.path.getsize(entry.path)
                sizeFileFormated = convert_size(fileSize)
                tempDetails = {"name":filename,"ext":ext,"path":entry.path,'size':fileSize,"diffModDate":str(diffDate),"diffCurrDate":str(diffFromCreationDate),"sizeFormated":sizeFileFormated}
                listFileDetails[entry.name] = tempDetails
            else:
                FindFile(os.path.join(dirPath,entry))
                
def ResetFile(dirPath):
    with os.scandir(dirPath) as entries:
        for entry in entries:
            if entry.is_file():
                shutil.move(entry.path,os.path.join(CURDIR,entry.name))
            else:
                ResetFile(os.path.join(dirPath,entry))

def SortFile(dirPath):
    listFile = os.listdir(dirPath)
    for file in listFile:
        filename,ext = os.path.splitext(file)
        ext =ext[1:]
        if file == "info.json":
            continue
        if os.path.exists(os.path.join(dirPath,ext)):
            shutil.move(os.path.join(dirPath,file),os.path.join(dirPath,ext,file))
        else:
            os.makedirs(os.path.join(dirPath,ext))
            shutil.move(os.path.join(dirPath,file),os.path.join(dirPath,ext,file))
def StoreModPath(dirPath):
    with os.scandir(dirPath) as entries:
        for entry in entries:
            if entry.is_file():
                tempDetails = listFileDetails[entry.name]
                tempDetails["pathMod"] = entry.path
                listFileDetails[entry.name] = tempDetails
            else:
                StoreModPath(os.path.join(dirPath,entry))
def Cleaning(dirPath,infoPath):
    with open(infoPath,'r') as file:
        listFileDetails = json.load(file)
        files = list(listFileDetails.keys())
        tempDirPath = dirPath
        for i in tqdm(range(len(files)),"Files:"):
            dirPath = os.path.join(tempDirPath,listFileDetails[files[i]]['ext'][1:])
            try:
                diffDate = int(listFileDetails[files[i]]['diffCurrDate'].split()[0])
            except:
                diffDate = 0
            if (listFileDetails[files[i]]['ext'] in ['.exe','.msi'] and listFileDetails[files[i]]['size'] > 1e+8) or diffDate > 15:
                if os.path.exists(os.path.join(dirPath,"trash")):
                    shutil.move(os.path.join(dirPath,files[i]),os.path.join(dirPath,"trash",files[i]))
                else:
                    os.makedirs(os.path.join(dirPath,"trash"))
                    shutil.move(os.path.join(dirPath,files[i]),os.path.join(dirPath,"trash",files[i])) 

def Deleteing(dirPath,infoPath):
    with open(infoPath,'r') as file:
        listFileDetails = json.load(file)
        files = list(listFileDetails.keys())
        tempDirPath = dirPath
        for i in tqdm(range(len(files)),"Files:"):
            dirPath = os.path.join(tempDirPath,listFileDetails[files[i]]['ext'][1:],"trash")
            try:
                diffDate = int(listFileDetails[files[i]]['diffCurrDate'].split()[0])
            except:
                diffDate = 0
            if (listFileDetails[files[i]]['ext'] in ['.exe','.msi'] and listFileDetails[files[i]]['size'] > 1e+8) or diffDate > 15:
                print(f"File Name:{files[i]} - File Size:{listFileDetails[files[i]]['sizeFormated']}")
                yesno = input("[y]/n?")
                if yesno == "":
                    yesno = 'y'
                if yesno == 'y':
                    os.remove(os.path.join(dirPath,files[i]))
def DelDir(dirPath,infoPath):
    listFile = os.listdir(dirPath)
    print(listFile)
    with open(infoPath,'r') as file:
        listFileDetails = json.load(file)
        files = list(listFileDetails.keys())
        folderWithFiles = [listFileDetails[files[i]]['ext'][1:] for i in tqdm(range(len(files)),"Files:")]
        folderWithFiles = list(set(folderWithFiles))
        for file in tqdm(listFile,"Files"):
            if file not in folderWithFiles and not os.path.isfile(file):
                shutil.rmtree(os.path.join(dirPath,file))
        
                
    
if __name__ == "__main__":
    print("Getting InFo...")     
    FindFile(CURDIR) 
    time.sleep(3)
    print("Moving Files To Current Dir...")
    ResetFile(CURDIR)
    time.sleep(3)
    print("Sorting File...")
    SortFile(CURDIR)
    time.sleep(3)
    print("Store Modified Path...")
    StoreModPath(CURDIR)
    time.sleep(1)
    print("Storeing File...")
    listFileDetails = json.dumps(listFileDetails)
    with open(INFOLOC,'w') as infoFile:
        infoFile.write(listFileDetails)
    time.sleep(3)
    print("Started Cleaning...")
    Cleaning(CURDIR,INFOLOC)
    print("Deleting...")
    print("Do you wanna delete the file?")
    Deleteing(CURDIR,INFOLOC)
    time.sleep(3)
    print("Moving Files To Current Dir...")
    ResetFile(CURDIR)
    time.sleep(3)
    print("Sorting File...")
    SortFile(CURDIR)
    print("Deleteing Empty Dir...")
    DelDir(CURDIR,INFOLOC)
    
    
