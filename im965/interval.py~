# This module contains/defines the classes and functions used in assignment 5
# Author: Israel Malkin (im965)

#import 
from myexceptions import *


#Define the interval class 
class interval:
    '''class for integer intervals objects'''

    def __init__(self,ui):

        
            # ensure input is string
            if (type(ui) is not str): 
		raise NotStringException
            
            #remove whitespace from user input for conformability
            _nw=ui.strip()

            # ensure first and last characters are legal (either square brackets or parenthesis)         
            if not (_nw[0]=="[" or  _nw[0]=="("): 
		raise InvalidBoundException
            if not (_nw[-1]=="]" or  _nw[-1]==")"): 
		raise InvalidBoundException

            # ensure that the endpoints are seperated by a comma
            if _nw.count(",")!=1: 
		raise CommaException

            # ensure contents to the left and right of comma are digits 
            if (_nw.split(",")[0][1:].isdigit()==False) or (_nw.split(",")[1][:-1].isdigit()==False): 
		raise NotIntException

            #ensure the interval bounds are legal
            if (_nw[0]=="[" and  _nw[-1]=="]") and (int(_nw.split(",")[0][1:]) > int( _nw.split(",")[1][:-1])):
		raise IllegalRangeException
 
            if (_nw[0]=="[" and  _nw[-1]==")") and (int(_nw.split(",")[0][1:]) >= int( _nw.split(",")[1][:-1])):
                raise IllegalRangeException

            if (_nw[0]=="(" and  _nw[-1]=="]") and (int(_nw.split(",")[0][1:]) >= int(_nw.split(",")[1][:-1])):
                raise IllegalRangeException

            if (_nw[0]=="(" and  _nw[-1]==")") and (int(_nw.split(",")[0][1:]) >= (int(_nw.split(",")[1][:-1]))-1):
                raise IllegalRangeException




            #Extract Info from input
            self.raw=ui                                 # Raw input
            self._nw=ui.strip()                         # Remove whitespace (so all input conforms)
            self._l,self._r=self._nw.split(",")         # String with all contents to left/right of comma
            self.leftnum=int(self._l[1:])                  # Numeric input to the left of the comma        
            self.rightnum=int(self._r[:-1])                # Numeric input to the right of the comma
            self.leftreal=self.leftnum if self._l[0]=="[" else self.leftnum+1             # Inclusive lower bound (accounts for bracket vs. parenthesis)
            self.rightreal=self.rightnum if self._r[-1]=="]" else self.rightnum-1        # Inclusive upper bound (accounts for bracket vs. parenthesis)


    def __repr__(self):
            return self._nw


def mergeIntervals(int1,int2):
    '''Returns the union of two intervals if they overlap, otherwise returns "do not overlap" '''
    if overlapCheck(int1,int2)==False:
        raise NoOverlapException
    else:
        return interval(str(sorted([int1,int2],key=lambda element: element.leftreal)[0]._l)+","+str(sorted([int1,int2],key=lambda element: element.rightreal)[1]._r))
  

def overlapCheck(intA,intB):
    '''Returns boolean to indicate if two intervals overlap'''
    return (intA.leftreal<=intB.leftreal<=intA.rightreal) or (intB.leftreal<=intA.leftreal<=intB.rightreal) \
    or (intA.leftreal<=intB.leftreal and intB.rightreal<=intA.rightreal) or (intB.leftreal<=intA.leftreal and intA.rightreal<=intB.rightreal)

def sortIntervals(intervalstosort):
    '''Sort a list of intervals based on the smallest element in each interval'''
    if len(intervalstosort)>1:
        return sorted(intervalstosort, key=lambda element: element.leftreal)   
    else:
        return intervalstosort     	

def mergeOverlapping(intervalstomerge):
    '''Returns a list of merged intervals'''
    merged=[]
    current=sortIntervals(intervalstomerge)[:]
   
    while len(current)>1:
        if overlapCheck(current[0],current[1]):
            current[1]=mergeIntervals(current[0],current[1])
        else:
            merged.append(current[0])    
        current.remove(current[0])
    if len(current)==1:
	merged.append(current[0])    
    return sortIntervals(merged)


def insert(intervalbase,newint):
    '''Takes a list of intervals and a singlenton and merges the two, if possible'''
    combo=intervalbase[:]
    combo.append(newint)
    return mergeOverlapping(combo)

def intervalMerger():
    '''Interactive function to merge interval input from user'''
    userinp=str(raw_input("List of intervals? \n")).split(",")
    resultint=mergeOverlapping([interval(a+","+b) for (a,b) in zip(userinp[::2],userinp[1::2])])
    print resultint

    while userinp!="quit":
        userinp=str(raw_input("Interval? \n"))
	if userinp!="quit":
            new=interval(userinp)
            resultint=insert(resultint,new) 
            print resultint 
        else:
            print "........Goodbye!" 



