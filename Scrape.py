import requests
import csv
import time
from bs4 import BeautifulSoup

url = 'https://report.boonecountymo.org/mrcjava/servlet/RMS01_MP.I00030s?max_rows=500'
response = requests.get(url, headers = {'User-Agent': 'Mozilla/8.0'})
html = response.content #site documents

soup = BeautifulSoup(html, 'html.parser') #parsing site documents
#print(soup.prettify())
table = soup.find('tbody', attrs = {'class': 'stripe'}) #only prints the table we are after

list_of_rows=[]
#BeautifulSoup allows us to dig down into our table and return a list of rows
for row in table.findAll('tr'):
    list_of_cells = []
    #loop through each cells in each row by select them inside the loop
    for cell in row.findAll('td'):
        #print the text inside the cells
        text = cell.text.replace("\n\xa0Details\n", '')
        '''
        To repace any weird character inside the content
        cell.text.replace('character', '')
        '''
        #add each cell in a row to a new python list
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)
#print(list_of_rows)
outfile = open("./hereRtheList.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["Last Name", "First Name", "Middle","Prefix", "Gender", "Race", "Age", "City", "States"])
writer.writerows(list_of_rows)
