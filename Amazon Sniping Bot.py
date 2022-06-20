
from msedge.selenium_tools.options import Options
import selenium
from selenium import webdriver as wb
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from msedge.selenium_tools import Edge, EdgeOptions
from selenium import webdriver
import time



def If_Available(new_l1,new_l2,URL):
    
    mylist=[]
    from selenium import webdriver
    options = Options()
    options.use_chromium = True
    options.add_argument('--headless')
    webD1=wb.Chrome('chromedriver.exe')    
   
    webD1.get(URL)
    
    time.sleep(2)
    
    html=webD1.page_source
    
    soup=BeautifulSoup(html,"html.parser")
        
        
    availability=webD1.find_element_by_xpath('//*[@id="availability"]/span[1]')
        
    availability=availability.text
        
        
    time.sleep(4)
        
    if availability!="ã“ã®å•†å“ã¯ç¾åœ¨ãŠå–ã‚Šæ‰±ã„ã§ãã¾ã›ã‚“ã€‚":
        
        try:
            
            pri=webD1.find_element_by_xpath('//*[@id="corePrice_feature_div"]/div/span')
            
            pri=pri.text


            length=len(pri)


            price=""
        


            for j in range(0,length):
                
                if pri[j]=='ï¿¥':
                    
                    for k in range(j+1,length):
                        
                        price+=pri[k]


            newprice=""

            for index in range(0,len(price)):

                if price[index]==',':

                    continue

                else:

                    newprice+=price[index]


            temp=int(newprice)

                

            if temp>=new_l1 and  temp<=new_l2:

                print("Buying the product within the available range!")

                print("Its price: ",temp)



                mylist.append(1)

                webD1.quit()

                return(mylist)

            elif temp<new_l1:

                print("Available but with a higher price than the desired!")

            else:
                print("Expensive!")  
                
        except:
            new_list=[0]
            return new_list
        
            
                
                                    
    else:
        
        print("Currently Unavailable!")
            
        mylist.append(0)
        
        webD1.quit()
            
        return(mylist)
    
    
    webD1.quit()

    


def Purchase():
    
    URL= "https://www.amazon.co.jp/gp/product/B09GVYXWGT"
    
    l1=input("Please enter the starting range")
    
    l2=input("Please enter the ending range")
    
    
    new_l1=int(l1)
    
    new_l2=int(l2)
    
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument("user-data-dir=C:\\tmp\\Edge Data")
    options.add_argument('--profile-directory=Profile1')
    options.add_argument('--lang=en')
    

    driver = Edge(options=options)    
    
    driver.get(URL)
    
    
    flag=1
    
        
        
    while flag==1:
        
        time.sleep(1)
        
        temp_list=If_Available(new_l1,new_l2,URL)
        
        
        if temp_list[0]==1:
            
            try:
                
                driver.refresh()
                
                time.sleep(1)
                
                driver.find_element_by_xpath('//*[@id="addToCart_feature_div"]').click()
                
                driver.find_element_by_xpath('//*[@id="sc-buy-box-ptc-button"]').click()



                flag=0
        
                
            
            except:
                
                driver.quit()
                
                while flag!=0:
                    
                    try:
                        
                        
                        options = EdgeOptions()
                        options.use_chromium = True
                        options.add_argument("user-data-dir=C:\\tmp\\Edge Data")
                        options.add_argument('--profile-directory=Profile1')
                        options.add_argument('--lang=en')

                        driver = Edge(options=options)

                        driver.get(URL)
                            
                        driver.refresh()
                        
                        
                        driver.find_element_by_xpath('//*[@id="submit.buy-now"]').click()

                        flag=0
                        
                    except:
                        
                        print("Too load on the browser! Please try again!")
                        
                        flag=0
                        
                        
                            
                            

                    
                
                
    
            
        else:
            
            continue
            
        driver.find_element_by_xpath('//*[@id="submitOrderButtonId"]').click()

        driver.find_element_by_xpath('//*[@id="bottomsubtotals"]/div/div/div/div[1]/span/span').click()  
    


# In[173]:


Purchase()

