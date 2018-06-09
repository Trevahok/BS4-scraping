import json
import lxml.html as lh
import urllib.request as ul
from bs4 import BeautifulSoup as bs
def extract_details(page):
    soup = bs(page,'lxml')
    addresses=[bs(str(i).replace('<br/>',','),'lxml').text.strip() for i in soup.find_all('address')]
    city=[address.split(',')[-2] for address in addresses]
    zipcode=[address.split()[-1] for address in addresses]
    keyword=[''.join(i.text.strip().split()) for i in soup.find_all(class_='category-str-list')]
    website=[bs(ul.urlopen('https://www.yelp.com'+i.get('href')),'lxml').find(class_='biz-website js-biz-website js-add-url-tagging') for i in soup.find_all(class_='biz-name js-analytics-click')]
    website=[i.a.text if i!=None else '' for i in website]
    reg_names=[i.a.span.text for i in soup.find_all(class_='search-result-title')]
    phno=[i.text.strip() for i in soup.find_all('span',class_='biz-phone')]
    for rn,zp,k,web,ct,add,ph in zip(reg_names,zipcode,keyword,website,city,addresses,phno):
        data={
                'state':"California",
                'country':"United States",
                'registered_name':rn,
                'zipcode':zp,
                'keywords':k,
                'website':web,
                'city':ct,
                'address':add,
                'phone_number':ph,
                'license':'',
                'depends_on':'',
                }
        with open('summer_camp_bay_area.json','a') as f:
            print(str(data))
            f.write(json.dumps(data)+'\n')
for i in range(100,1000,10):
    page = ul.urlopen('https://www.yelp.com/search?find_loc=San+Francisco+Bay+Area,+CA&start='+str(i)+'&cflt=summer_camps')
    extract_details(page)
    print('done one more')
