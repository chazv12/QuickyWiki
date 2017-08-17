"""
QuickyWiki: Command Line Wikipedia Summaries
"""
import requests


def search_wiki(subject):
    wiki_endpoint = 'https://en.wikipedia.org/w/api.php'
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'extracts',
        'titles': subject,
        'redirects': 1,
        'explaintext': 1,
        'exintro': 1
    }

    response = requests.get(wiki_endpoint, params=params).json()
    pages = response['query']['pages']
    try:
        for page_number in pages:
            print(pages[page_number]['title'])
        return pages[page_number]['extract']
    except:
        print('Error:', subject, 'not found.')
        return

if __name__ == "__main__":
    print("QuickyWiki")
    SEARCH_TERM = input('Enter in term:')
    print(search_wiki(SEARCH_TERM))
