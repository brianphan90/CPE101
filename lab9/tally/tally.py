from sys import *

def open_files(argv):
   try:
      f = open(argv[1], 'r')
      return f
   except:
      print("error")
      exit()

def column_nums(list):
   line_n = 0
   col = int(argv[2])
   try:
      line_n += 1
      list[col]
   except:
      return False

def column_letter(columns):
   column = int(argv[2])
   column_tot = 0
   line_tot = 0
   try:
      for i in range(len(columns)):
         if i == col:
            float(columns[i])
            column_tot+= float(columns[i])
            return column_tot
   except:
      columns = 0
      return False

def main(): 
   f = open_files(argv)
   total = 0
   line_n = 0
   for line in file:
      line_n +=1
      list = line.split()
      if column_nums(list) == False:
         print str(line_n) + ""+"out of range"
      elif column_letter(list) == False:
         print(str(line_n) +"" +"not a number")
      else:
         sum += column_letter(list)
   print("sum:", total)

if __name__ == "__main__":
   main()        
