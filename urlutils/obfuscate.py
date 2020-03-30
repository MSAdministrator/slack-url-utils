from collections import Counter


class Obfuscate(object):

    scheme = None
    domain = None
    path = None

    url_format = '{scheme}://{domain}/{path}'


    def __replace_multiple_characters(self, string, character): 
        new_str = [] 
        l = len(string) 
        
        for i in range(len(string)): 
            if (string[i] == character and i != (l-1) and
            i != 0 and string[i + 1] != character and string[i-1] != character): 
                new_str.append(string[i]) 
                
            elif string[i] == character: 
                if ((i != (l-1) and string[i + 1] == character) and
                (i != 0 and string[i-1] != character)): 
                    new_str.append(string[i]) 
                    
            else: 
                new_str.append(string[i]) 
            
        return ("".join(i for i in new_str))

    def __parse_domain(self,url):
        return url.split('/')[0]
        
    def __parse_path(self,url):
        new_path = url.lstrip('/').rstrip('/')
        return self.__replace_multiple_characters(new_path,'/')

    def __parse_scheme(self,url):
        if url.startswith('https'):
            return 'hxxps'
        else:
            return 'hxxp'

    def url(self, url):
        print(url)
        scheme = None
        domain= None
        path = None
        temp_url = None
        if isinstance(url, bytes):
            url = url.decode("utf-8")
        if isinstance(url,str):
            scheme = self.__parse_scheme(url)
            if 'https://' in url:
                temp_url = url.replace('https://','')
                domain = self.__parse_domain(temp_url)
                temp_url = temp_url.replace(domain,'')
            else:
                temp_url = url.replace('http://','')
                domain = self.__parse_domain(temp_url)
                temp_url = temp_url.replace(domain,'')
            
            path = self.__parse_path(temp_url)

            return self.url_format.format(
                scheme=scheme,
                domain=domain,
                path=path
            )