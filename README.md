# ormuco-test
PYTHON TECHNICAL TEST

To test the submitted programs download and extract the entire repository and then run Mark_Stern_test.py in Python3.

## Question A

To use the `is_overlapped` function, copy the file overlap.py into the folder containing your code and add the line `from overlap import is_overlapped` to the beginning of your python file. The function takes two lists as arguments. Each list should only contain two numeral elements, the endpoints of the line segments.  The function returns `True` if the given line segments are overlapped and `False` otherwise.

Notes: For this question, I tried to use the most straightforward implementation I could come up with for ease of reading and understanding. I found a very simple conditional works given that the line segment endpoints are in increasing order. Overlap is `False` if and only if `x2<x3 or x4<x1`.

## Question B

To use the `version_compare` function, copy the file version.py into the folder containing your code and add the line `from version import version_compare` to the beginning of your python file. The function takes two strings as arguments (e.g. '1.0', '2.0b'). The function returns `1` if the first version is more recent, `-1` if the second version is more recent and `0` if they are equivalent.

Notes: This question had more depth as there are many different possible versioning schemes. I implemented a simple but generally applicable implementation that accounts for alphaneumeric ordering. It does not handle some specific versioning schemes (e.g. PEP 440), which would need to be detected and handled on a case by case basis. 

## Question C

To use the `google_scrape` function, copy the file google_insights.py into the folder containing your code and add the line `from google_insights import google_scrape` to the beginning of your python file. The function take a string, the search term text, and an optional integer, the number of results, as arguments. The function returns an array of dictionaries with the search result components, including the rank, title, link url, and description of the result.

Notes: This was by far the most challenging and open-ended question. I believe a project trying to extract the most relevant information from a google search result is would have endless potential for improvement. Again, here I made the simplest but effective implementation I could come up with in a short amount of time, taking advantage of the google search result descriptions found below each search result as easiest to get, relevant information. Clearly, much improvment can be made by scraping the individual search results for more specific information. But given my time restrictions this seems to be an effective starting point. Note that there is a bug in the code that if a news article is detected the link text will not work. But it works fine for web results.