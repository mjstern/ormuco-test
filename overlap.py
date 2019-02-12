"""
overlap.py

Functions for ormuco technical test Question A
Author: Mark J. Stern, Ph.D.

Question A
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap.
As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
"""

def is_overlapped(line1in,line2in):
    """ Returns true if the two given number line segments overlap. Otherwise returns False.

    line1in, line2in - Lists of length 2 defining the end points of the two line segments (eg. line1in = [1,2] line2in =  [3.5,4.5])
    """
    # Sort the lines so that the first element is always smaller than the second
    line1 = sorted(line1in)
    line2 = sorted(line2in)
    #Overlap is False when x2<x3 or x4<x1 after sorting, True otherwise.
    if (line1[1] < line2[0]) or (line2[1] < line1[0]):
        return False
    else:
        return True
