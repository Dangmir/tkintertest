import requests
from pprint import pprint
from bs4 import BeautifulSoup
from openpyxl.drawing.image import Image
import openpyxl
import datetime

my_wb = openpyxl.Workbook()
my_sheet = my_wb.active
my_sheet_title = my_sheet.title
print("My sheet title: " + my_sheet_title)
my_wb = openpyxl.Workbook()
my_sheet = my_wb.active
r = requests.get("https://game-tournaments.com/dota-2/matches")
soap = BeautifulSoup(r.text, "html.parser")


def get_names_team(d):
    names = soap.find_all("a", "mlink")
    return names[d]['href']


def get_team_compos1(url):
    d = requests.get("https://game-tournaments.com" + url)
    soap = BeautifulSoup(d.text, "html.parser")
    names = soap.find_all("div", "col-xs-6")
    team1 = names[0].get_text().split()
    return team1


def get_team_compos2(url):
    d = requests.get("https://game-tournaments.com" + url)
    soap = BeautifulSoup(d.text, "html.parser")
    names = soap.find_all("div", "col-xs-6")
    team2 = names[1].get_text().split()
    return team2


def get_team_url1(url):
    d = requests.get("https://game-tournaments.com" + url)
    soap = BeautifulSoup(d.text, "html.parser")
    a = soap.find_all("div", "teamlogo")
    return a[0].find('a')['href']


def get_team_url2(url):
    d = requests.get("https://game-tournaments.com" + url)
    soap = BeautifulSoup(d.text, "html.parser")
    a = soap.find_all("div", "teamlogo")
    return a[1].find('a')['href']


def get_team_logo1(url):
    d = requests.get("https://game-tournaments.com" + url)
    soap = BeautifulSoup(d.text, "html.parser")
    img1 = soap.find_all("div", "teamlogo")
    img = img1[0].findChild("img")['src']
    p = requests.get("https://game-tournaments.com" + img)
    a = f'{str(datetime.datetime.now().time()).replace(":", "")+".png"}'
    print(a)
    out = open(a, "wb")
    out.write(p.content)
    out.close()
    return a


def get_team_logo2(url):
    d = requests.get("https://game-tournaments.com" + url)
    soap = BeautifulSoup(d.text, "html.parser")
    img1 = soap.find_all("div", "teamlogo")
    img = img1[1].findChild("img")['src']
    p = requests.get("https://game-tournaments.com" + img)
    a = f'{str(datetime.datetime.now().time()).replace(":", "")+".png"}'
    print(a)
    out = open(a, "wb")
    out.write(p.content)
    out.close()
    return a


def get_date(url):
    d = requests.get("https://game-tournaments.com" + url)
    soap = BeautifulSoup(d.text, "html.parser")
    return soap.time.text


anchor = 1


def main():
    global anchor
    for i in range(3):
        print(f'Обратаываю ' + str(i + 1) + ' команду')
        a = get_names_team(i)
        team1 = get_team_compos1(a)[0]
        team2 = get_team_compos2(a)[0]
        img1 = get_team_logo1(a)
        img2 = get_team_logo2(a)
        img = openpyxl.drawing.image.Image(img1)
        imgteam2 = openpyxl.drawing.image.Image(img2)
        print(team1)

        lists = (get_date(a), team1, my_sheet.add_image(img, "C"+str(anchor)), get_team_url1(a),team2, my_sheet.add_image(imgteam2, "F"+str(anchor)), get_team_url2(a))
        my_sheet.append(lists)
        anchor = anchor + 6
        for d in range(6):
            a = get_names_team(i)
            team1 = get_team_compos1(a)[d]
            team2 = get_team_compos2(a)[d]
            if d == 0:
                pass
            else:
                lisa = ("", team1, "", team2)
                my_sheet.append(lisa)
    my_wb.save("Book2.xlsx")


main()
