import requests
from pagee import scrap_page
import csv
import time



with open('JLT_appartment.csv', 'w', newline='', encoding="utf-8") as w:
    aw = csv.writer(w)
    aw.writerow(['title', 'building1', 'building2', 'price', 'bedroom', 'bathroom', 'area'])

    #url = "http://localhost:8000/jlt_appartments.html"
    url = "https://dubai.dubizzle.com/en/property-for-rent/residential/apartmentflat/?filters=(bedrooms%3E%3D1%20AND%20bedrooms%3C%3D1)%20AND%20(neighborhoods.ids%3D193)&sort=lowest"
    print('Scraping:'); print(url)
    page = requests.get(url)
    scrap_page(page, aw)

    for i in range(1,36):         
        urlp = url + "&page=" + str(i)        
        print('Scraping:'); print(urlp)
        time.sleep(10)
        page = requests.get(urlp)
        scrap_page(page, aw)

w.close()