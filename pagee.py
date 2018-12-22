from details import scrap_details
from bs4 import BeautifulSoup

def scrap_page(page, aw):
    soup = BeautifulSoup(page.text, 'html.parser')

    details_items = soup.find_all('div', class_='details')
    #print(len(details_items))

    #firstdetail = details_items[0]
    #print(firstdetail.prettify())

    for details in details_items:
        #print(details.prettify())
        link = details.find_parent('a', class_='promoted-link')
        #It promoted item, leave it
        if not link:            
            title, building1, building2, price, bedroom, bathroom, area, url = scrap_details(details)
            print(title); print(building1); print(building2); print(price); print(bedroom)
            print(bathroom); print(area); print(url)
            print('--------------------')    
            aw.writerow([title, building1, building2, price, bedroom, bathroom, area, url])
