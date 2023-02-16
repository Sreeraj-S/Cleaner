import Sorter
import sys

dir = sys.argv[1]

Sort = Sorter.Sorter(dir)

#Sort.moveFile("PDF Files",".pdf")

Sort.deleteSetupFiles()