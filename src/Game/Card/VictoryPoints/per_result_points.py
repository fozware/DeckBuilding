
class PerResultPoints:
    """ Represents a VP based on a condition """
    
    def __init__(self, filter):
        """ Initialize the filter to get results from """
        self.filter = filter
        
    def calculatePoints(self, args):
        """ Return the number of Points """
        return len(self.filter.evaluate(args))