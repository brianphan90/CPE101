
from sys import *

def open_file(argv):
   try:
      file = open(argv[1], 'r')
      return file
   except:
      print "error"
      exit()

def columnrange(list):
   linenum=0
   col=int(argv[2])
   try:
      linenum+=1
      list[col]
   except:
      return False

def columnalpha(columns):
   col = int(argv[2])
   columnsum = 0 
   linenum = 0
   try:
      for i in range(len(columns)):
         if i == col:
            float(columns[i])
            columnsum += float(columns[i])
            return columnsum
   except:
      columns = 0   
      return False

def main():
   file = open_file(argv)
   sum=0
   linenum=0
   for lines in file:
      linenum +=1
      list = lines.split()
      if columnrange(list)==False:
        print str(linenum) + " " + "out of range"
      elif columnalpha(list)==False:
        print str(linenum) + " " + "not a number"
      else:
         sum+=columnalpha(list)
   print "sum:", sum






if __name__ == "__main__":
    main()


