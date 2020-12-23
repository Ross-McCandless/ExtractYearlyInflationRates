import requests
from bs4 import BeautifulSoup
from datetime import datetime
import xlwt

output = r"Inflation_CPI.xls"
curr_date = datetime.now()
wb = xlwt.Workbook()
ws = wb.add_sheet("Data")
ws.write(0,0, 'YEAR')
ws.write(0,1, 'CPI')
oldest_year = 1950

for year in range(oldest_year, curr_date.year):
    url = "http://www.inflation.eu/inflation-rates/canada/historic-inflation/cpi-inflation-canada-" + str(year) + ".aspx"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')    
    for tag in soup.findAll('span'):
        if len(tag.text) != 0 and len(tag.text) != 15:
            CPI = tag.text[:tag.text.find("&", 1, 20)]
    current_row =  year - oldest_year + 1
    ws.write(current_row, 0, year)
    ws.write(current_row, 1, CPI)
    wb.save(output)
    print(year, CPI)
    

    
    

    

