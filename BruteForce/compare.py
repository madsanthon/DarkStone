# -*- coding: iso-8859-1 -*-
import numpy as np

end = "-BruteForce-EndData-N10.txt"

listData = ['OT'+end,'MA'+end,'MM'+end]

##print listData

all_data = map(np.loadtxt,listData);
##print all_data

def compare(X,Y):
    """ Function compares matrices X and Y to each other by
taking the difference of the absolute values of both"""
    return np.sum(np.abs(X)-np.abs(Y));

print "Den sammenligner først Orhans med alle, \
Mads' med alle og dernæst Mossas' med alle"
np.set_printoptions(precision=4)
for data in all_data:
    result = map(lambda a: compare(data,a),all_data)
    print np.array(result)
