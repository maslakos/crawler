import requests

def pagedownloader(page):

    #This function download the Allegro Website, and formats it to the Human readable form.
    #Web address (link) should be given between quoters " "

    page = requests.get(page)
    print(page.status_code)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page.content, 'html.parser')
    list(soup.children)
    [type(item) for item in list(soup.children)]
    html = list(soup.children)[2]
    list(html.children)
    body = list(html.children)[3]
    list(body.children)
    p = list(body.children)[3]
    text = p.get_text()
    text = text.encode('ascii', 'ignore').decode('ascii')
    print(text)

pagedownloader("https://allegro.pl/kategoria/laptopy-491?order=m")

