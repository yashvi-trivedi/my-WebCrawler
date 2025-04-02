#installing dependencies
import requests
import sys
from bs4 import BeautifulSoup
from argparse import ArgumentParser, Namespace
from urllib.parse import urlparse
import re

parser=ArgumentParser()

parser.add_argument('-u', '--geturl', help='provides url')

parser.add_argument('-t', '--tvalue', help='provides threshold')

parser.add_argument('-o', '--outputfile', help='creates outputfile', required=False)

args: Namespace= parser.parse_args()

url=args.geturl

passedfile= args.outputfile

threshold_token=int(args.tvalue)

urls=[]

pattern = r"(?P<domain>^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/\n]+))"

match = re.search(pattern, url)
orgdomain = match.group("domain")


def scrape_links(url,n=0, maxdepth=threshold_token):
    print(n)
    if n >= maxdepth:
        return
    else:
    
        #Get Site data and make it into a BS4 object
        webpage = requests.get(url)
        html_content = webpage.content
        soup = BeautifulSoup(html_content, "lxml")

        for tag in soup.find_all('a', href=True): #For all <a> tags with href attributes on the current page
            href = tag.get("href") #Get the href of the a tag
            if href.startswith("/"): 
                href = url + href
                
            if href.startswith("#"): #If it starts with # (HTML class link) then skip
                continue #Skip this link
            if passedfile:
                with open(passedfile, 'a') as writer:
                    for x in (href):
                        writer.write(x)
                    writer.write("\n")

            else:
                print(" "*n*4+href) #Print the link to check

            
           
            if href not in urls: #if link has not already been seen
                urls.append(href) #add url to the list
                
                scrape_links(href, n + 1, maxdepth) #recursive function call
       
scrape_links(url, 0, threshold_token)