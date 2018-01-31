import bs4


def parse_wiki_response(response_xml):
    message = 'По вашему запросу данных не найдено'

    soup = bs4.BeautifulSoup(response_xml, 'xml')
    item = soup.find('Item')
    attributes_dict = {}

    if item:
        for element in filter(lambda x: bool(x.name), item):
            attributes_dict[element.name] = element.get_text(strip=True)

        message = '{Text}\n{Description}\n{Url}'.format(**attributes_dict).strip()

    return message
