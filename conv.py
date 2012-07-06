import math

#Done:
#Base Function Temp: From Kalvin to Celcile
#Base Function Lenght: From sm to meters
#Experemental Function FlameRate: Taking- Message Count, Threads Count, Registration Date, Karma. Giving - FlameRate.
#Work:
#Make more base function
#Add options to choose Category
#add normal outprint

def main():
    a = raw_input(' Input value')
    a_list = a.split(' ')
    print a_list

    b = len(a_list)
    print b
    i = 0

    new_list = float(a_list[i])
    new_board = int(a_list[i+1])
    new_count = float(a_list[i+2])    

    print new_list
    print new_board
    print new_count

    T = new_list - 10 # Temp 
    print('Temp:', T)

    L = new_board/100 # Len
    print ('Len:', L)

    F = (new_count*10-51+666)/1.5
    print ('Trollstate:', F)

    

#    num = 373
 #   T = (num - 273)
  #  print T

main()

