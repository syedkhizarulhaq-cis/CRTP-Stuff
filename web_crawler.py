from bs4 import BeautifulSoup
import requests
from urllib.parse import quote
from pprint import pprint
import re

class GoogleSpider(object):
        def __init__(self):
                super().__init__()
                self.headers = {
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:79.0) Gecko/20100101 Firefox/79.0",
                        "Host": "www.google.com",
                        "Referer": "https://www.google.com/"
                }

        def __get_source(self, url:str) -> requests.Response:
                return requests.get(url, headers=self.headers)

        def search(self, query: str) -> list:
                
                response = self.__get_source("https://www.google.com/search?q=%s" % quote(query))
                soup = BeautifulSoup(response.text, "html5lib")
                result_containers = soup.findAll("div",attrs = {'class': "yuRUbf"})
                urls = []
                for container in result_containers:
                        url = container.find("a")["href"]
                        urls.append(re.findall('://([\w\-\.]+)',url))
                return urls
                
if __name__ == "__main__":
        print(GoogleSpider().search(input("Search for what? ")))