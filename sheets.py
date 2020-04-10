import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("ScrapingTest.json",scopes=scope)

client = gspread.authorize(creds)

sheet = client.open("Test Scraping").sheet1
# sheet.insert_col([1,2,3,4],4)


niftyPivot = (niftyClose+niftyHigh+niftyLow)/3
niftyBC = (niftyHigh+niftyLow)/3
niftyTC = (niftyPivot-niftyTC)+niftyPivot
niftyR1 = 2*(niftyPivot-niftyLow)
niftyR2 = niftyPivot+(niftyHigh-niftyLow)
niftyR3 = niftyR1+(niftyHigh-niftyLow)
niftyR4 = niftyR3+(niftyR2-niftyR1)
niftyS1 = 2*(niftyPivot-niftyHigh)
niftyS2 = niftyPivot-(niftyHigh-niftyLow)
niftyS3 = niftyS1-(niftyHigh-niftyLow)
niftyS4 = niftyS3-(niftyS1-niftyS2)
niftyH4 = niftyClose + (((niftyHigh-niftyLow)*1.1)/2)
niftyH3 = niftyClose + (((niftyHigh-niftyLow)*1.1)/4)
niftyL4 = niftyClose - (((niftyHigh-niftyLow)*1.1)/2)
niftyL3 = niftyClose - (((niftyHigh-niftyLow)*1.1)/4)
niftyRow = ["Nifty",niftyHigh,niftyClose,niftyR4,niftyR3,niftyR2,niftyR1,niftyTC,niftyPivot,niftyBC,niftyS1,niftyS2,niftyS3,niftyS4,niftyH4,niftyH3,niftyL3,niftyL4]
niftyBNPivot = (niftyBNClose+niftyBNHigh+niftyBNLow)/3
niftyBNBC = (niftyBNHigh+niftyBNLow)/3
niftyBNTC = (niftyBNPivot-niftyBNTC)+niftyBNPivot
niftyBNR1 = 2*(niftyBNPivot-niftyBNLow)
niftyBNR2 = niftyBNPivot+(niftyBNHigh-niftyBNLow)
niftyBNR3 = niftyBNR1+(niftyBNHigh-niftyBNLow)
niftyBNR4 = niftyBNR3+(niftyBNR2-niftyBNR1)
niftyBNS1 = 2*(niftyBNPivot-niftyBNHigh)
niftyBNS2 = niftyBNPivot-(niftyBNHigh-niftyBNLow)
niftyBNS3 = niftyBNS1-(niftyBNHigh-niftyBNLow)
niftyBNS4 = niftyBNS3-(niftyBNS1-niftyBNS2)
niftyBNH4 = niftyBNClose + (((niftyBNHigh-niftyBNLow)*1.1)/2)
niftyBNH3 = niftyBNClose + (((niftyBNHigh-niftyBNLow)*1.1)/4)
niftyBNL4 = niftyBNClose - (((niftyBNHigh-niftyBNLow)*1.1)/2)
niftyBNL3 = niftyBNClose - (((niftyBNHigh-niftyBNLow)*1.1)/4)
niftyBNRow = [niftyBNHigh,niftyBNClose,niftyBNR4,niftyBNR3,niftyBNR2,niftyBNR1,niftyBNTC,niftyBNPivot,niftyBNBC,niftyBNS1,niftyBNS2,niftyBNS3,niftyBNS4,niftyBNH4,niftyBNH3,niftyBNL3,niftyBNL4]

for i in range(19):
    print([niftyRow[i],niftyBNRow[i]])