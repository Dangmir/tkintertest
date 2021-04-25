from bs4 import BeautifulSoup
import requests
import openpyxl
my_wb = openpyxl.Workbook()
my_sheet = my_wb.active
my_sheet_title = my_sheet.title
print("My sheet title: " + my_sheet_title)
my_wb = openpyxl.Workbook()
my_sheet = my_wb.active
mul = 1
f = open("text.txt","w")
def page(url_page):
    global counti
    r = requests.get("https://www.techcult.ru/science/page/"+str(url_page))
    soap = BeautifulSoup(r.text, "html.parser")
    pad = soap.find_all("a", "pad")
    count = len(pad)
    date = soap.find_all("span", "cat_nav")
    for i in range(count):
        url = pad[i]['href']
        title = pad[i].h2.get_text()
        date1 = (date[i].get_text())
        img = pad[i].img['src']
        bd = (url,title,date1,img)
        my_sheet.append(bd)



counti = 0
while True:
    counti =counti+1
    page(counti)
    my_wb.save("Book1.xlsx")
    print(counti)
    if counti == 58:
        f.close()
        break




