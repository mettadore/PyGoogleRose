# PyGoogleRose
This is something of a quick hack of the Google Chart API's Radar diagram to support a psuedo-rose diagram. 

I needed to quickly generate some rose diagrams for use in Google Earth at work, and couldn't find a simple programmatic solution. Unfortunately, the Google Chart API doesn't support rose diagrams natively, so I created this, a somewhat kludged, solution.

This class is something I created specifically to display the average of a list of azimuths on a rose diagram showing a graphic of the total list. It's a bit of a simplified solution, but should give someone a quick headstart on creating rose diagrams for themselves.

The module uses the Google-Chartwrapper library from: http://code.google.com/p/google-chartwrapper/, which is the only pre-requisite. I've also used Python 3.1, but one should be able to quickly port it to the Python 2.x series.