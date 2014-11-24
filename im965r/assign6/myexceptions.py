# This module defines the exceptions

class NotStringException(Exception) :
        def __init__(self,msg="Input must be string") :
            self.m=msg
        def __str__(self):
            return repr(self.m)


class InvalidBoundException(Exception) :
        def __init__(self,msg="Bounds must be specified with either '(' or '['"):
            self.m=msg
        def __str__(self):
	    return repr(self.m)

class CommaException(Exception) :
        def __init__(self,msg="Endpoints must be split be a comma"):
            self.m=msg
	def __str__(self):
	    return repr(self.m)

class NotIntException(Exception) :
        def __init__(self,msg="Upper and lower bounds must be integers"):
            self.m=msg
	def __str__(self):
	    return repr(self.m)

class IllegalRangeException(Exception) :
        def __init__(self,msg="The range described is not legal"):
            self.m=msg
        def __str__(self):
            return repr(self.m)


class NoOverlapException(Exception) :
	def __init__(self,msg="Intervals do not overlap"):
	    self.m=msg
	def __str__(self):
	    return repr(self.m)

