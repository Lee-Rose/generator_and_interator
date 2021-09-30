import wikipediaapi as wiki
import json

class DataWiki:

    ''' An iterator class that looks for a wikipedia page for each country in the countries.json file.
Writes to a file a pair: country - link.'''

    def __init__(self, path, start=0):
        self.file = open(path, encoding='utf-8')
        self.json = json.load(self.file)
        self.start = start - 1
        self.wiki = wiki.Wikipedia('en')

    def __iter__(self):
        return self

    def __next__(self):

        self.start += 1

        if self.start == len(self.json):
            raise StopIteration

        country = self.json[self.start]['name']['common']
        country_page = self.wiki.page(country)
        country_link = country_page.fullurl

        return country, country_link


if __name__ == '__main__':

    with open('countries_links.txt', 'w') as output_file:
        for country, item in DataWiki('countries.json'):
            output_file.write(f'{country} -> {item}\n')
            print('---load---')

