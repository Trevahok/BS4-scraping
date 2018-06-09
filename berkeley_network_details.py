import lxml.html as lh
import urllib.request as ul
from bs4 import BeautifulSoup as bs
berkeleynet_root='https://www.berkeleyparentsnetwork.org/'
berkeleynet='https://www.berkeleyparentsnetwork.org/daycares-preschools'
cities='''
Alameda
Albany
Berkeley
Brentwood
Castro Valley
Concord
Crockett
Danville
Dublin
El Cerrito
El Sobrante
Emeryville
Fremont
Hayward
Hercules
Kensington
Lafayette
Moraga
Oakland
Orinda
Pacifica
Piedmont
Pinole
Pleasant Hill
Pleasanton
Richmond
San Francisco
San Leandro
San Lorenzo
San Pablo
San Ramon
Union City
Vallejo
Walnut Creek
'''.split('\n')
# page = ul.urlopen(berkeleynet)
# soup= bs(page,'lxml')
# for link in soup.find_all('a'):
    # if link.text in cities :
        # print( '1'+link.text)
        # page=ul.urlopen(berkeleynet_root+link.get('href'))
        # print(page)
page = ul.urlopen('https://www.berkeleyparentsnetwork.org/recommend/preschool/garner')
soup = bs(page,'lxml')
def extract_details(page):
    soup = bs(page,'lxml')
    phno=soup.find(class_="field field-name-field-daycare-phone").text
    country = "United States"
    state='California'
    license=soup.find('a', class_='ext-link').text
    city = soup.find(class_="field field-name-daycare-city-ca field-location").p.text.split(',')[0]
    address = soup.find(class_="field field-name-field-neighborhood").text + ','+ city +','+state+','+country
    zipcode= soup.find(class_='field field-name-field-zip').text
    try:
        website = soup.select_one('#content > div > div.field.field-name-field-website.field-type-link-field.field-label-inline.clearfix > div.field-items > div > a').text
    except:
        website = ''
    dependson=''
    keyword=soup.select_one('#content > div > div:nth-of-type(3) > div.field.field-name-field-daycare-type.field-label-inline > div.field-items').text
    reg_name = soup.find(class_='page__title').text
    data={
            'state':state,
            'country':country,
            'registered_name':reg_name,
            'zipcode':zipcode,
            'keyword':keyword,
            'website':website,
            'city':city,
            'address':address,
            'phone_number':phno,
            'license':license,
            'depends_on':dependson,
            }


