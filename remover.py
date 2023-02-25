import Sorter
import sys
try:
    directory = sys.argv[1]

    Sort = Sorter.Sorter(directory)

    Sort.moveFile("PDF Files",".pdf")
    Sort.moveFile("Word Files",".doc")
    Sort.moveFile("Word Files",".docx")
    Sort.moveFile("Presentation Files",".ppt")
    Sort.moveFile("Presentation Files",".pptx")
    Sort.moveFile("Images Files(png)",".png")
    Sort.moveFile("Images Files(jpg)",".jpg")
    Sort.moveFile("Video Files",".mp4")
    Sort.moveFile("Executable File(exe)",".exe")
    Sort.moveFile("Executable File(msi)",".msi")
    Sort.moveFile("Zip Files",".zip")
    Sort.trash()
    Sort.allocateFolder(directory)
except Exception as e:
    print(e)
#Sort.deleteSetupFiles()

#Sort.oldFiles()