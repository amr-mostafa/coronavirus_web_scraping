# web scraping for the coronavirus data
* A python script that extracts all countries coronavirus "COVID-19" data from
"https://www.worldometers.info/coronavirus/"
* Then save these data into **csv** file

## Resources used
* Python 3.7.3
* **Packages**: [BeautifulSoub4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), [Requests](https://requests.readthedocs.io/en/master/)

## Project Demo
https://youtu.be/26xD8Mn-V4U

## Prerequisites
You must install beautifusoup4 and Requests packages.
Open CMD and run these commands
```
pip install beautifulsoup4
```
```
pip install requests
```

## Run the project
The project is only 1 python script __main.py__  and you will run it to extract the data from the website. Open CMD and run this command to run the script
```
python main.py
```

## Script Output
Script generates __covid19.csv__ file with __7 columns__ for all scraped coronavirus data. Each country is represented as a row whith these column values:
* country's name
* country's total cases
* country's new cases
* country's total death
* country's new death
* country's total recovered
* country's population (useful for making some statistical analysis on the data)

![](https://i.ibb.co/Ptt6S5H/123.png)

And total coronavirus data:
* total cases
* total death
* total recovered

![](https://i.ibb.co/x3M8w1F/1234.png)

## License
This project is licensed under the GNU General Public License.
