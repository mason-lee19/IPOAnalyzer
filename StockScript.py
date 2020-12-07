def main():
    scraper = cfscrape.create_scraper()

    # Grab recent IPO's tickers
    r = scraper.get('https://stockanalysis.com/ipos/2020-list/')

    soup = BeautifulSoup(r.text,'html.parser')
    # print(soup.text)
    results = soup.find_all('tr')
    n = 110 # amount of stocks to analyze
    for i in (results[109:n]):
        ticker = (i.find('a').text) 
        ipoDate = (i.find('td').text)
        threeMonth = MoCalc(ipoDate)
        calcHistory(scraper,ticker,threeMonth)



# Calculate 3 months after ipoDate 
def MoCalc(date):
    if 'Jan' in date:    
        threeMonth = 'Apr'
    if 'Feb' in date:    
        threeMonth = 'May'
    if 'Mar' in date:    
        threeMonth = 'Jun'
    if 'Apr' in date:    
        threeMonth = 'Jul'
    if 'May' in date:    
        threeMonth = 'Aug'
    if 'Jun' in date:    
        threeMonth = 'Sep'
    if 'Jul' in date:    
        threeMonth = 'Oct'
    if 'Aug' in date:    
        threeMonth = 'Nov'
    if 'Sep' in date:    
        threeMonth = 'Dec'
    if 'Oct' in date:    
        threeMonth = 'Jan'
    if 'Nov' in date:    
        threeMonth = 'Aug'
    if 'Dec' in date:    
        threeMonth = 'Feb'
    return threeMonth

def calcHistory(scraper,company,date):
    time.sleep(5) # Allow some time between scrapes
    link = 'https://finance.yahoo.com/quote/'+company+'/history?period1=1600992000&period2=1604620800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'
    print(link)
    r = scraper.get(link)
    soup = BeautifulSoup(r.text,'html.parser')
    results = soup.find_all('tr')
    for i in results:
        try:
            temp = i.find('span').text
            print(temp)
        except:
            temp = 1
    



if __name__ == '__main__':
    import requests
    import tkinter as tk
    from bs4 import BeautifulSoup
    import cfscrape
    import time
    import traceback

    main()


# Use company ticker to find financials and how theyve done since IPO
# Use Yahoo finance to find price's by date
# stock_cashFlow = []
# stock_totalDebt = []
# stock_industry = []
# stock_Desc = []
# stock_Name = []
# for i in ticker:
#     time.sleep(randint(3,8))
#     link = ('https://stockanalysis.com/stocks/'+i)
#     r = requests.get(link)
#     soup = BeautifulSoup(r.text,'html.parser')

#     desc = soup.find('p',attrs = {'class':'desc'})
#     stock_Desc.append(desc.contents)

#     info_all = soup.find_all('td')
#     for index, obj in enumerate(info_all):
#         if obj.text == 'Full Name':
#             stock_Name.append(info_all[index+1].text)
#         if obj.text == 'Free Cash Flow':
#             stock_cashFlow.append(info_all[index+1].text)
#         if obj.text == 'Total Debt':
#             stock_totalDebt.append(info_all[index+1].text)
#         if obj.text == 'Industry':
#             stock_industry.append(info_all[index+1].text)

