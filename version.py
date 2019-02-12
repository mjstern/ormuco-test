"""
version.py

Functions for ormuco technical test Question B
Author: Mark J. Stern, Ph.D.

Question B
The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other.
As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.
"""
def add_zeros(list1,list2):
    """ Adds zeroes to the end of the shorter of (list1, list2) to equalize the list lengths """
    length_diff = len(list2) - len(list1)
    if length_diff > 0:
        return list1 + [0]*length_diff, list2
    if length_diff < 0:
        return list1, list2 + [0]*(-length_diff)
    else:
        return list1, list2
    


def version_compare(version_string1, version_string2, versioning_scheme = None):
    """ Returns a integer from (1, 0, -1) and a string from ("greater than", "equal", "less than") describing the relationship between version_string1 and version_string2

    version_string1, version_string2 - versions to be compared
    versioning_scheme - key for a specified versioning scheme from the following list:
        TODO: Populate list of versioning schemes.

    returns compare_string
    """
    # For the case where no versioning scheme is specified, sort alphanumerically.
    if versioning_scheme is None:
        version_list_1, version_list_2 = add_zeros(version_string1.split("."),version_string2.split("."))
        print(version_list_1,version_list_2)
        
        
