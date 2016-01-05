import requests
import lxml.html
from bs4 import BeautifulSoup

def extractLinks(url, base):
        '''
        Return links from the website
        :param url: Pass the url
        :param base: this is the base links
        :return: list of links
        '''
        links = [] #it will contain all the links from the website
        try:
            r = requests.get(url)
        except:
            return []
        obj = lxml.html.fromstring(r.text)
        potential_links = obj.xpath("//a/@href")
        links.append(r.url)
        # print potential_links
        for link in potential_links:
            if base in link:
                links.append(link)
            else:
                if link.startswith("http"):
                    links.append(link)

                elif base.endswith("/"):
                    if link.startswith("/"):
                        link = link.lstrip("/")
                        link = base + link
                    else:
                        link = base + link
                    links.append(link)

        return links
