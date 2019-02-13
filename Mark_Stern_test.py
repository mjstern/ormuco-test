"""
Test file for the Ormuco python technical test.
Author: Mark J. Stern, Ph.D.

Running this file will test the 3 programs defined by the following test questions:

Question A
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap.
As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).
 
Question B
The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other.
As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

Question C
Create an api that takes a string as input and returns a list of text insights from the top 5 google results of the query generated by those keywords. 

Test with the following string « keystone - Circular reference found role inference » . You will need to build a query , search the web (you can scrape google),
select the top 5 results and for each result scrape for the most relevant information on that page (relevant from a user’s perspective based on the original string ) .
The response should contain the links to the websites that were scraped with the most relevant information (could be a text insight ,  a code snippet, a patch file, etc.) for each.
In the response, feel free to add any other extra information that you think could be relevant.
"""

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#QUESTION A

from overlap import is_overlapped

#Test input for Question A:
input_A = [
    ([1,2],[3,4]),
    ([1,2],[4,3]),
    ([1,3],[2,4]),
    ([1,4],[3,2]),
    ([2.5,1.5],[3.5,4.5]),
    ([3.5,2.5],[1.5,4.5])
]

#Expected output for Question A:
expected_A = [
    False,
    False,
    True,
    True,
    False,
    True
]

#Test question A
print("Testing is_overlapped function:")
for inp, exp in zip(input_A,expected_A):
    if exp == is_overlapped(*inp):
        test_string = "pass"
    else:
        test_string = "fail"
    print("Test input: ", *inp,", expected output: ",exp ,"... ", test_string)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#QUESTION B

from version import version_compare

#Test input for Question B:
input_B = [
    ("1.0","1.1"),
    ("2.0.1","2.0"),
    ("0.0.3","0.0.3.0"),
    ("1.1a","1.1b"),
    ("2.1c","2.1")
]

#Expected output for Question B:
expected_B = [
    -1,
    1,
    0,
    -1,
    1
]

#Test question B
print("Testing version_compare function:")
for inp, exp in zip(input_B,expected_B):
    out = version_compare(*inp)
    if exp == out:
        test_string = "pass"
    else:
        test_string = "fail"
    print("Test input: ", *inp,", expected output: ",exp , "actual output: ",out,"... ", test_string)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#QUESTION C

from pandas import DataFrame
from google_insights import google_scrape

TEST_STRING = "keystone - Circular reference found role inference"

results = google_scrape(TEST_STRING)
results_df = DataFrame(results)
results_df = results_df[["rank","title","link","description"]]
print(results_df)