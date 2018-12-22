import furl

def scrap_details(detaildiv):
    #region title
    titleh2 = detaildiv.find('h2', class_='listTitle')
    title = ""
    if titleh2:
        title = titleh2.text
    #print(title)
    #endregion title

    #region Place
    placediv = detaildiv.find('div', class_='place')
    buildings = placediv.find_all('span')
    blength  = len(buildings)
    building1 = ""
    building2= ""
    if blength == 2:
        building1 = buildings[0].text
        building2 = buildings[1].text
    elif blength == 1:
        building1 = buildings[0].text
    #print(building1)
    #print(building2)
    #endregion Place

    #region price
    pricediv = detaildiv.find('div', class_='price')
    price = pricediv.text
    price = price.replace("AED","").replace(",","").strip()
    #print(price)
    #region price

    #region area
    bedroom = ""
    bathroom = ""
    area = ""
    listSubDetailsdiv = detaildiv.find('div', class_='listSubDetails attributes')
    if listSubDetailsdiv:
        spans = listSubDetailsdiv.find_all('span')
        sdlength = len(spans)        
        if sdlength == 3:
            bedroom = spans[0].text.strip()
            bathroom = spans[1].text.strip()
            area = spans[2].text.strip()
            area = area.replace('SqFt','').strip()
    #print(bedroom)
    #print(bathroom)
    #print(area)
    #endregion area

    #region url
    link = detaildiv.find_parent('a', class_='listing-link')
    if not link:
        link = detaildiv.find_parent('a', class_='promoted-link')

    url = ''
    if link:
        url = link['href']
        url = furl.furl(url).remove(args=True, fragment=True).url

    return title, building1, building2, price, bedroom, bathroom, area, url