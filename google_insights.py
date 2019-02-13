import requests
import re
from string import punctuation
from bs4 import BeautifulSoup

TEST_STRING = "keystone - Circular reference found role inference"

def prepare_string_for_url(search_string = TEST_STRING):
    """ Prepare search string so that it works in a google search url"""
    # Make regular expression for removing punctuation.
    regex_punctuation = re.compile('[%s]' % re.escape(punctuation))
    search_string = regex_punctuation.sub('',search_string)
    #Reduce multiple spaces to single spaces
    search_string = re.sub(' +', ' ',search_string)
    #Replace ' ' with '+' for Google search url
    search_string = search_string.replace(' ', '+')
    return search_string

def parse_search_results(html, keyword):
    """ Parse search results using Beautiful Soup and return a dictionary of the title, link url, and description,
     code based on http://edmundmartin.com/scraping-google-with-python/"""
    soup = BeautifulSoup(html,'html.parser')
    #initiallize variables
    found_results = []
    rank = 1
    #Search results are in class 'g' divs
    result_block = soup.find_all('div', attrs={'class': 'g'})
    for result in result_block:
        #Try to find a link and a title, also look for link url 
        link = result.find('a', href=True)
        title = result.find('h3', attrs={'class': 'r'})
        link_url = result.find('cite')
        description = result.find('span', attrs={'class': 'st'})
        #if both a link and a title are found it is an organic search result block
        if link and title:
            link = link['href']
            title = title.get_text()
            # Pass the results to a dictionary
            if description:
                description = description.get_text()
            if link != '#':
                found_results.append({'rank': rank, 'title': title, 'link': link_url.text, 'description': description})
                rank += 1
    return found_results

def google_scrape(search_term, num_search_results = 5):
    """ Returns the top Google search results from the search_term in the form of a dictionary. 
    Dictionary entries are 'rank', 'title', 'link' and 'description'."""
    google_url = f"https://www.google.com/search?q={prepare_string_for_url(search_term)}&num={num_search_results}"
    response =  requests.get(google_url)
    results = parse_search_results(response.text, search_term)
    return results