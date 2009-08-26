from GChartWrapper import *
from math import pi, radians, degrees, sin, cos, atan2

class Rose(object):
    def __init__(self, lst, bad_value=-32768, color='red'):
        self.color = color
        lst = [i for i in filter(lambda x: x != bad_value, lst)]
        h = 'ABCDEFGH123456789' # Hex values for use in the URL
        bins = {0:0} # Initialize with a zero value at due north
        a = 0
        # Separate values into bins of 10 degree increments. The values
        # Are the number of azimuth readings within each 10 degree increment
        # where 10 degrees includes all readings in the range (5,15], 20
        # degrees includes all readings in the range (15,25], and 0 degrees
        # includes all readings in the range (355,5].
        for b in range(5,360,10):
            rng = lambda x: (x >= a) and (x < b)
            bins[b+5] = len([i for i in filter(rng, lst)])
            a = b

        try:
            # Move values at 360 to zero and copy. This is so that we
            # can have a full circle of data
            bins[0] += bins[360]
            bins[360] = bins[0]
        except KeyError:
            pass

        highest = max(bins.values())
        # Re-interpret values as percentages of a hex value from 1-16
        for k,v in bins.items():
            try:
                bins[k] = h[int((v/highest) * 16)]
            # We have no azimuth values.
            except ZeroDivisionError:
                bins[k] = 'A'
        vals = '' # values at each label
        for i in range(0,370,10):
            try: vals += bins[i]
            except KeyError: vals += 'A' # Minimum if there's no value

        if not len(lst): mean = 0 # We're blank, throw up a placeholder chart
        else:
            #########################################
            # Calculate the average azimuth
            rads = [radians(i) for i in lst] #Convert to radians
            # Convenience functions
            ave = lambda x: sum(x)/len(x)
            rotate = lambda x: x+(2*pi) if x<0 else x # bring back to positive angle values
    
            sa = ave([sin(i) for i in rads])
            ca = ave([cos(i) for i in rads])
            # Take the arctan of this, using atan2 to preserve the quadrant information
            # We divide this (in degrees) by ten because there are only 36 values
            # around our rose diagram
            mean = degrees(rotate(atan2(sa,ca)))/10
            ########################################
        
        ########################################
        # Create the pseudo-rose diagram using Google's Radar
        self.G = Radar([vals],encoding='simple')
        self.G.size(200,200)
        self.G.color(self.color)
        self.G.line(2,4,0)
        self.G.line(2,4,0)
        self.G.axes('x')
        self.G.axes.label(0, 'N',10,20,30,40,50,60,70,80,'E',100,110,120,130,140,150,160,170,'S',190,200,210,220,230,240,250,260,'W',280,290,300,310,320,330,340,350)
        self.G.axes.range(0, 0.0,360.0)
        self.G.marker('h','blue',0,1.0,1)
        self.G.marker('V','008000',0,mean,5)
        self.G.marker('B','FF000080',0,1.0,5.0)


    def URL(self):
        return self.G.url
    def tag(self, imgid='chart'):
        return self.G.img(height=200,id=imgid)

