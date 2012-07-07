import math

#Done:
#Base Function Lenght.

#Work:
#Make more base function
#Add options to choose Category
#add normal outprint

def main():
    a = raw_input('   Input value   ')
    a_list = a.split(' ')
    print a_list
    lenght(a_list)
 

def lenght(a_list):
    i = 0
    while i < len(a_list):
       val = float(a_list[i])
       n = raw_input('  Choose const: 1 - mm, 2 - inch, 3 - sm, 4 - meters, 5 - kilometers   ')
       if n == '1': ## mm
        res1 = val/25.4 # mm -> inch
        res2 = val/10 # mm -> sm
        res3 = val/1000 # mm -> meters
        res4 = val/10000 # mm -> kilometers
        print   'inch, sm, meters, kilometers:', res1,',', res2,',', res3,',', res4
       if n == '2': ## inch
        res1 = val*25.4 # inch -> mm
        res2 = res1/10 # inch -> sm
        res3 = res2/1000 # inch -> meters
        res4 = res3/10000 # inch -> kilometers
        print   'mm, sm, meters, kilometers:', res1,',', res2,',', res3,',', res4
       if n == '3': ## sm
        res1 = val*10 # sm -> mm
        res2 = res1/25.4 # sm -> inch
        res3 = val/100 # sm -> meters
        res4 = val/1000 # sm -> kilometers
        print   'mm, inch, meters, kilometers:', res1,',', res2,',', res3,',', res4
       if n == '4': ## meters
        res1 = val*1000 # meters -> mm
        res2 = val*100 # meters -> sm
        res3 = res1/25.4 # meters -> inch
        res4 = val/1000 # meters -> kilometers
        print   'mm, sm, inch, kilometers:', res1,',', res2,',', res3,',', res4
       if n == '5': ## kilometers
        res4 = val*1000 # km -> meters
        res3 = res4*100 # km -> sm
        res1 = res3*10 # km -> mm
        res2 = res1/25.4 # km -> inch
        print   'mm, inch, sm, meters:', res1,',', res2,',', res3,',', res4
       if n <> '1' or '2' or '3' or '4' or '5':
        print 'Failed'
       i =i +1
           
    




#Basic tests for GUI:


 #   b = len(a_list)
  #  print b
   # i = 0

  #  new_list = float(a_list[i])
   # new_board = int(a_list[i+1])
    #new_count = float(a_list[i+2])    

 #   print new_list
#    print new_board
  #  print new_count

   # T = new_list - 10 # Temp 
    #print('Temp:', T)

    #L = new_board/100 # Len
    #print ('Len:', L)

 #   F = (new_count*10-51+666)/1.5
#    print ('Trollstate:', F)

    

#    num = 373
 #   T = (num - 273)
  #  print T

main()

