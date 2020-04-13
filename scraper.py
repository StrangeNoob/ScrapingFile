from bs4 import BeautifulSoup
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
import time
import schedule


def spreadSheet():
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    page1 = requests.get("https://www.moneycontrol.com/indian-indices/nifty-50-9.html", headers=headers).text
    page2 = requests.get("https://www.moneycontrol.com/indian-indices/nifty-bank-23.html",headers=headers).text
    soup1 = BeautifulSoup(page1,'lxml')
    soup2 = BeautifulSoup(page2,'lxml')
    var2 = soup1.find('span',attrs={'class':'lastprice'})
    var2 = var2.text
    var2 = var2.replace(',','')
    var2 = var2.strip()
    niftyClose = float(var2)
    print('niftyClose is ',niftyClose)
    var3 = soup1.find('strong',attrs={'class':'high'})
    var3 = var3.text
    var3 = var3.replace(',','')
    var3 = var3.strip()
    niftyHigh = float(var3)
    print('niftyHigh is ',niftyHigh)
    var4 = soup1.find('strong',attrs={'class':'low'})
    var4 = var4.text
    var4 = var4.replace(',','')
    var4 = var4.strip()
    niftyLow = float(var4)
    print('niftyLow is ',niftyLow)
    var5 = soup2.find('span',attrs={'class':'lastprice'})
    var5 = var5.text
    var5 = var5.replace(',','')
    var5 = var5.strip()
    niftyBNClose = float(var5)
    print('niftyBNClose is ' ,niftyBNClose)
    var6 = soup2.find('strong',attrs={'class':'high'})
    var6 = var6.text
    var6 = var6.replace(',','')
    var6 = var6.strip()
    niftyBNHigh = float(var6)
    print('niftyBNHigh is ',niftyBNHigh)
    var7 = soup2.find('strong',attrs={'class':'low'})
    var7 = var7.text
    var7 = var7.replace(',','')
    var7 = var7.strip()
    niftyBNLow = float(var7)
    print('niftyBNLow is ',niftyBNLow)

    # assign Values of Pivot,BC,TC,R1,R2,R3,R4,S1,S2,S3,S4,H1,H2,H3,H4,L1,L2,L3,L4 of nifty
    niftyPivot = (niftyClose+niftyHigh+niftyLow)/3
    niftyBC = (niftyHigh+niftyLow)/3
    niftyTC = (niftyPivot-niftyBC)+niftyPivot
    niftyR1 = 2*(niftyPivot-niftyLow)
    niftyR2 = niftyPivot+(niftyHigh-niftyLow)
    niftyR3 = niftyR1+(niftyHigh-niftyLow)
    niftyR4 = niftyR3+(niftyR2-niftyR1)
    niftyS1 = (2*niftyPivot)-niftyHigh
    niftyS2 = niftyPivot-(niftyHigh-niftyLow)
    niftyS3 = niftyS1-(niftyHigh-niftyLow)
    niftyS4 = niftyS3-(niftyS1-niftyS2)
    niftyH4 = niftyClose + (((niftyHigh-niftyLow)*1.1)/2)
    niftyH3 = niftyClose + (((niftyHigh-niftyLow)*1.1)/4)
    niftyL4 = niftyClose - (((niftyHigh-niftyLow)*1.1)/2)   
    niftyL3 = niftyClose - (((niftyHigh-niftyLow)*1.1)/4)
    niftyRow = ["Nifty",niftyHigh,niftyClose,niftyLow,niftyR4,niftyR3,niftyR2,niftyR1,niftyTC,niftyPivot,niftyBC,niftyS1,niftyS2,niftyS3,niftyS4,niftyH4,niftyH3,niftyL3,niftyL4]
    
    # assign Values of Pivot,BC,TC,R1,R2,R3,R4,S1,S2,S3,S4,H1,H2,H3,H4,L1,L2,L3,L4 of niftyBN

    niftyBNPivot = (niftyBNClose+niftyBNHigh+niftyBNLow)/3
    niftyBNBC = (niftyBNHigh+niftyBNLow)/3
    niftyBNTC = (niftyBNPivot-niftyBNBC)+niftyBNPivot
    niftyBNR1 = 2*(niftyBNPivot-niftyBNLow)
    niftyBNR2 = niftyBNPivot+(niftyBNHigh-niftyBNLow)
    niftyBNR3 = niftyBNR1+(niftyBNHigh-niftyBNLow)
    niftyBNR4 = niftyBNR3+(niftyBNR2-niftyBNR1)
    niftyBNS1 = (2*niftyBNPivot)-niftyBNHigh
    niftyBNS2 = niftyBNPivot-(niftyBNHigh-niftyBNLow)
    niftyBNS3 = niftyBNS1-(niftyBNHigh-niftyBNLow)
    niftyBNS4 = niftyBNS3-(niftyBNS1-niftyBNS2)
    niftyBNH4 = niftyBNClose + (((niftyBNHigh-niftyBNLow)*1.1)/2)
    niftyBNH3 = niftyBNClose + (((niftyBNHigh-niftyBNLow)*1.1)/4)
    niftyBNL4 = niftyBNClose - (((niftyBNHigh-niftyBNLow)*1.1)/2)
    niftyBNL3 = niftyBNClose - (((niftyBNHigh-niftyBNLow)*1.1)/4)
    niftyBNRow = ["Nifty BN",niftyBNHigh,niftyBNClose,niftyBNLow,niftyBNR4,niftyBNR3,niftyBNR2,niftyBNR1,niftyBNTC,niftyBNPivot,niftyBNBC,niftyBNS1,niftyBNS2,niftyBNS3,niftyBNS4,niftyBNH4,niftyBNH3,niftyBNL3,niftyBNL4]

    Row1= ['Fundamental','High','Close','Low','R4','R3','R2','R1','TC','P','BC','S1','S2','S3','S4','H4','H3','L3','L4']
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("ScrapingTest.json",scopes=scope)
    client = gspread.authorize(creds)
    sheet = client.open("Test Scraping").sheet1
    for i in range(19):
        if(i == 0):
            row = [d1,Row1[i],niftyRow[i],niftyBNRow[i]]
        else:
            row = ['',Row1[i],niftyRow[i],niftyBNRow[i]]
        sheet.insert_row(row,i+1)
        print(i+1," is inserted to SpreadSheet")
