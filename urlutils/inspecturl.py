import requests
from bs4 import BeautifulSoup

from motor import Motor

class InspectUrl(object):

    _url_list = []
    _searched_url_list = []

    def __init__(self, user_agent=False, proxy=False):
        if user_agent and proxy:
            self.network = Motor()#user_agent=True, proxy=True)
        elif user_agent:
            self.network = Motor()#user_agent=True)
        elif proxy:
            self.network = Motor()#proxy=True)
        else:
            self.network = Motor()

    def is_site_up(self, value):
        url = value.replace(" ","%20")
        response = self.network.get(url)
        return response

    def parse_href_links(self, soup):
        return_list = []
        for link in soup.find_all('a'):
            return_list.append(link.get('href'))
        return return_list

    def parse_indexof(self, soup, url):
        return_list = []
        try:
            if 'index of' in (soup.title.string).lower():
                for link in self.parse_href_links(soup):
                    new_link_path = '{}/{}'.format(url.rstrip('/'), link)
                    if new_link_path.endswith('//'):
                        new_link_path = new_link_path[:-1]
                    return_list.append(new_link_path)
                return return_list
        except:
            pass

    def __check_title(self, soup):
        try:
            if '404' in (soup.title.string).lower():
                return False
            else:
                return True
        except:
            pass

    def run(self, domain):
        url_list = []
        if not isinstance(domain,list):
            url_list = ['http://{}'.format(domain)]
        else:
            url_list = domain
        for url in url_list:
            print(url)
            url_info = self.is_site_up(url)
            if url_info:
                try:
                    print(url_info)
                    content = url_info['content'].decode('utf-8')
                    soup = BeautifulSoup(content, 'html.parser')
                    title_status = self.__check_title(soup)
                    if not title_status:
                       # print('404 in title')
                        return '404 in title'
                    #else:
                       # return 
                    if 'page is parked ' in soup:
                        return 'website is parked: {}'.format(url)
                    if 'Server:' in soup and 'PARKED' in soup:
                        return 'website is parked: {}'.format(url)
                    if 'Registered at' in soup:
                        return 'website is parked: {}'.format(url)
                    if 'parked' in soup or 'Parked' in soup:
                        return 'website is parked: {}'.format(url)
                    index_of = self.parse_indexof(soup, url)
                    if index_of:
                        for item in index_of:
                            print('item in index_of is %s' % item)
                            if item not in self._searched_url_list:
                                self._searched_url_list.append(item)
                    else:
                        print(soup)
                        for item in self.parse_href_links(soup):
                            try:
                                new_url = None
                                print('item is {}'.format(item))
                            # print('parsed_url is {}'.format(parsed_url_list))
                            # raw_input()
                                if item:
                                    if item not in url:
                                        if url not in item:
                                            if not item.startswith('http'):
                                                new_url = None
                                                if url.endswith('/'):
                                                    if item.startswith('/'):
                                                        new_url = url + item.replace('/','',1)
                                                        print('new url is %s' % new_url)
                                                    else:
                                                        new_url = '{}{}'.format(url, item)
                                                        print('new url is %s' % new_url)
                                                else:
                                                    if item.startswith('/'):
                                                        new_url = url.replace('/','',1) + item
                                                        print('new url is %s' % new_url)
                                                    else:
                                                        new_url = '{}{}'.format(url, item)
                                                        print('new url is %s' % new_url)
                                                
                                            else:
                                                new_url = item
                                            #raw_input()
                                        else:
                                            new_url = item
                                            print('new url is %s' % new_url)
                                            #raw_input()
                                    if new_url not in self._searched_url_list:
                                        self._searched_url_list.append(new_url)
                            except:
                                pass
                            
                    if self._url_list:
                        for item in self._url_list:
                            if len(self._url_list) < 200:
                                self._url_list.append(item)
                        self.run(self._url_list)
                except:
                    print('URL {} Not Up'.format(url))
            else:
                return 'No Response Received'

#count = 0
#total = 100
#response = requests.get('https://blacklist.cyberthreatcoalition.org/unvetted/domain.txt')
#for domain in response.text.split():
#    inspect = InspectUrl().run(domain)
#    print(inspect)
#    input('test')