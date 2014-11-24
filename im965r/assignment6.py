# -*- coding: utf-8 -*-
"""
 Run program for assignment 6, ask user for input and merge intervals as
 more are added. Stop when 'quit' is entered
@author: Israel
"""

from assign6 import *

if __name__=="__main__":
    resultint=[]
    rawuserinp=""
    while len(resultint)==0 and rawuserinp!='quit': 
        try:
            rawuserinp=str(raw_input("List of intervals? \n"))
            userinp=rawuserinp.split(",")
            resultint=mergeOverlapping([interval(a+","+b) for (a,b) in zip(userinp[::2],userinp[1::2])])
            print resultint
        except (NotStringException,InvalidBoundException,CommaException,NotIntException,IllegalRangeException,NoOverlapException) as e:
            print "Last input not valid \n"
        except (KeyboardInterrupt) as e:
            print "Caught a keyboard interrupt, to quit enter 'quit' \n"
    if rawuserinp=='quit':
        print "........Goodbye!"


    while rawuserinp!="quit":
        rawuserinp=str(raw_input("Interval? \n"))
        if rawuserinp!="quit":
            print 't'
            try:
                new=interval(rawuserinp)
                resultint=insert(resultint,new) 
                print resultint
            except (NotStringException,InvalidBoundException,CommaException,NotIntException,IllegalRangeException,NoOverlapException) as e:
                print "Last input not valid \n"
            except (KeyboardInterrupt) as e:
               print "Caught a keyboard interrupt, to stop enter 'quit'"
            
        else:
            print "Final interval: "+ str(resultint) +"\n........Goodbye!" 

           
            
    

