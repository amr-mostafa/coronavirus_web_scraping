from bs4 import BeautifulSoup as bs
import requests

# make HTTP request with the url, save the request to http_request variable
url = 'https://www.worldometers.info/coronavirus/'
http_request = requests.get(url)

# read the response which is the HTML resource document
html_document = http_request.text

# create BeautifulSoup object from the HTML document
html_parser = bs(html_document, 'html.parser')

# extract total cases, death, recovered
total_cases = html_parser.find('h1', string='Coronavirus Cases:').parent.div.span.text
total_death = html_parser.find('h1', string='Deaths:').parent.div.span.text
total_recovered = html_parser.find('h1', string='Recovered:').parent.div.span.text

# extract all countries rows from the table
countries_table = html_parser.find('tbody')
countries_rows = countries_table.find_all(name='tr', style=True, class_=False)

# save columns headers into csv file
with open('covid19.csv', 'w') as covid19_file:
    covid19_file.write('country' + ',' + 'total_cases' + ',' + 'new_cases'
                       + ',' + 'total_death' + ',' + 'new_death'
                       + ',' + 'total_recovered' + ',' + 'population' + '\n')

    for country_row in countries_rows:

        # find all cells
        country_cells = country_row.find_all('td')

        # scrap each cell
        country_name = country_cells[1].text
        country_total_cases = country_cells[2].text
        country_new_cases = country_cells[3].text
        country_total_death = country_cells[4].text
        country_new_death = country_cells[5].text
        country_total_recovered = country_cells[6].text
        country_population = country_cells[14].text

        # insert country data as a row in the csv file
        covid19_file.write(country_name + ',' + country_total_cases.replace(',', '') + ','
                           + country_new_cases.replace(',', '') + ',' + country_total_death.replace(',', '') + ','
                           + country_new_death.replace(',', '') + ',' + country_total_recovered.replace(',', '') + ','
                           + country_population.replace(',', '') + '\n')

    # insert total cases, total death, total recovered into the last row of the file
    covid19_file.write('total cases' + ',' + total_cases.replace(',', '') + '\n')
    covid19_file.write('total death' + ',' + total_death.replace(',', '') + '\n')
    covid19_file.write('total recovered' + ',' + total_recovered.replace(',', '') + '\n')
