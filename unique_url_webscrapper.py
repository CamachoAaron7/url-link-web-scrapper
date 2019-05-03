from bs4 import BeautifulSoup, SoupStrainer
from urllib.parse import urljoin
from urllib.request import urlopen


url = "https://www.census.gov/data/tables/2016/demo/popest/state-total.html"

""" Pulls unique links from specified web link and creates a
    csv file with the web links with the header web_link."""
def getalllinks(url):
    urlContent = urlopen(url)
    urlClient = urlContent.read() 
    soup = BeautifulSoup(urlClient, 'html.parser')  
    urlContent.close()
    
    filename = "web_links.csv" 
    f = open(filename, "w") 
    headers = "web_links\n" 
    f.write(headers) 
    
    """ Soups all 'a' tags where 
        a href tag is present """
    links = soup.find_all('a', href = True)

    url_set = set()
    
    """ Retuns all hrefs and makes each relative 
        link into an absolute link through urljoin. 
        all links ending with a pdf, xlsx, doc, etc
        are not retuned. Code also checks for 
        duplicate links and returns only unique links """
    for link in links: 
        base_url = "https://www.census.gov/data/tables/2016/demo/popest/state-total.html/"
        link = urljoin(base_url, link['href']) 
        if link [-1] == '/': # Ensures that HTML link is a directory and not a file. 
            link = link[:-1]  
        ext = ["pdf", "xlsx", "doc", "docx", "mov",\
            "mp4", "mpg", "wmv", "javascript:window.print()"]
        if not link.endswith(tuple(ext)):                
            if link and link not in url_set:
                f.write(str(link) + "\n")
        url_set.add(link)             
        print(link) # used to view results of function
    f.close() #stops wrting file
print(getalllinks(url)) # prints results of the function                

