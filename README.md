# ormuco-test
PYTHON TECHNICAL TEST

To test the submitted programs download and extract the entire repository and then run Mark_Stern_test.py in Python3.

##Question A

To use the is_overlapped function, copy the file overlap.py into the folder containing your code and add the line `from overlap import is_overlapped` to the beginning of your python file.

Notes: For this question, I tried to use the most straightforward implementation I could come up with for ease of reading and understanding. I found a very simple conditional works given that the line segment endpoints were given in increasing order. Overlap is `False` when `x2<x3 or x4<x1`.