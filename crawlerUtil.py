import requests    
import re    
from urllib.parse import urlparse
from pymonad.Reader import curry
   

def get_html(url):    
    try:    
        html = requests.get(url)    
    except Exception as e:    
        print(e)    
        return ""    
    return html.content.decode('utf-8')    

def get_links(url):    
    html = get_html(url)    
    parsed = urlparse(url)    
    base = f"{parsed.scheme}://{parsed.netloc}"    
    links = re.findall('''<a\s+(?:[^>]*?\s+)?href="([^"]*)"''', html)    
    for i, link in enumerate(links):    
        if not urlparse(link).netloc:    
            link_with_base = base + link    
            links[i] = link_with_base       

    return set(filter(lambda x: 'mailto' not in x, links))    

def extract_info(url):                                
    html = get_html(url)                  

def crawl(url, getLinks):   
    linkToWork = []                
    for links in getLinks(url):
        linkToWork = linkToWork + links
    return linkToWork
                        
    

if __name__ == "__main__":                           
    crawler = PyCrawler("https://google.com")        
    crawler.start()