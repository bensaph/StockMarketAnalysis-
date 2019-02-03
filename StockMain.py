from urllib.request import *
from json import *


def get_json(url):
    ''' Function to get a json dictionary from a website.
        url - a string'''
    with urlopen(url) as response:
        html = response.read()
    htmlstr = html.decode("utf-8")
    return loads(htmlstr)

def main():
    company_list = ['AAC','AAN','AAOI','AAON','AAT','AAWW','AAXN','ABCB','ABEO','ABG','ABM','ABR','ABTX','ABUS','AC','ACAD','ACBI','ACCO','ACHN','ACIA','ACIW','ACLS','ACMR','ACNB','ACOR','ACRE','ACRS','ACTG','ADC','ADES','ADMA','ADMS','ADRO','ADSW','ADTN','ADUS','ADVM','AE','AEGN','AEIS','AEL','AEO','AERI','AFI','AGEN','AGFS','AGLE','AGM','AGS','AGX','AGYS','AHH','AHT','AI','AIMC','AIMT','AIN','AINC','AIR','AIT','AJRD','AJX','AKAO','AKBA','AKCA','AKR','AKRX','AKS','ALBO','ALCO','ALDR','ALDX','ALE','ALEX','ALG','ALGT','ALLK','ALNA','ALRM','ALTR','ALX','AMAG','AMAL','AMBA','AMBC','AMBR','AMC','AMED','AMEH','AMKR','AMN','AMNB','AMOT','AMPE','AMPH','AMR','AMRC','AMRS','AMRX','AMSF']
    percent_change_list = []
    index = 0
    for item in company_list:
        urlstr = 'https://api.iextrading.com/1.0/stock/' + item + '/quote'
        print(urlstr)
        dict = get_json(urlstr)
        company_name = dict['companyName']
        current_stock_price = dict['close']
        day_percent_change = dict['changePercent']
        percent_change_list.append([company_name,current_stock_price,day_percent_change])
        if dict['ytdChange'] < -0.15:
            print('OMG DISGUSTING!!!!')
        print('Company Name:',company_name,"   |    Closing Price:",current_stock_price,"   |    Day Percent Change:",day_percent_change)
        index+=1
    print(percent_change_list)
    percent_change_list.sort(key=lambda x: x[2],reverse=True)
    print(percent_change_list)
    print('THE GREATEST RETURN TODAY WAS:',percent_change_list[0][0])

if __name__ == '__main__':
    main()