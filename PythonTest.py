import pandas as pd 
import time 
import datetime as dt # manupulating date

## Selenium 
from selenium import webdriver   # importing selenium webdrivers
from selenium.webdriver.common.keys import Keys  # importing webdriver keys
 
class Test:
    
    def __init__(self):
        '''
        Google form Url
        Reading Html file
        And adding Webdrivers for Chrome
        '''
        self.url = 'https://forms.gle/tNV8Ra2TN7aLfgri8'
        self.df = pd.read_html('index.html',header=0)[0]
        self.browser = webdriver.Chrome()
             
    def PreProcessing(self):
        '''
        In this method We will do PreProcessing of data Like removing
        'an' substrings, formating dates and Removing symbols from Phone columns

        return:
        This Method will Return Processed DataFrame
        '''
        df = self.df[~self.df.Name.str.contains("an")]
        df['Phone'] = df['Phone'].str.replace(r'\(|\)| ','')
        df.reset_index(inplace=True)
        df.drop('index',axis=1,inplace=True)
        df['Date']=pd.to_datetime(df["Date"]).dt.strftime("%d%m%Y")
        #df.to_excel('Data_Details.xls')
        return df
    
    def FormAuthomation(self):
        '''
        In this Method we will Automate our Manual process of fill Google Form
        Path :
        This is the list of Xpath for the Google Form Attributes
        Columns:
        This is the Name list of Google Form Attributes
        '''
        data = self.PreProcessing() ## Calling PreProcessing method  
        Path =['//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input',
               '//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input',
               '//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/input',
               '//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/div[2]/div[1]/div/div[1]/input']
        Columns = ['Name','Phone','Email','Date']
        for j in range(0,len(data)):  ## Iterate all the rows of our excel data
            self.browser.get(self.url)
            for i in range(0,len(Path)):
                Attributes = self.browser.find_element_by_xpath(Path[i])
                Attributes.send_keys(data[Columns[i]][j])
                time.sleep(2)
            Submit = self.browser.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[3]/div[1]/div/div/span/span')
            Submit.click()
            print('Submitted', i)
                     
WebAuto = Test() ## Creating Object
WebAuto.FormAuthomation() 
