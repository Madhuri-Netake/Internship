#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install selenium')


# ### Q1: Write a python program to scrape data for “Data Analyst” Job position in “Bangalore” location. You
# have to scrape the job-title, job-location, company_name, experience_required. You have to scrape first 10
# jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.shine.com/
# 2. Enter “Data Analyst” in “Job title, Skills” field and enter “Bangalore” in “enter the location” field.
# 3. Then click the searchbutton.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.

# In[54]:


import selenium 
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.shine.com/new/job-search")

job_role = driver.find_element(By.CLASS_NAME, "form-control")
job_role.send_keys('Data Analyst')
location = driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Bangalore')
experience = driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div/form/div/div[1]/ul/li[3]/div/input[1]")
experience.send_keys('11')

search_button = driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div/form/div/div[2]/div/button")

search_button.click()

job_title = []
job_location = []
company_name = []
experience_required = []

# scraping Job title from the given page

title_tags=driver.find_elements(By.XPATH, '//div[@class ="jobCard_jobCard__jjUmu  white-box-border jobCard" or @class="jobCard_jobCard__jjUmu active white-box-border jobCard"]/div/h2/a') 
for i in title_tags:
    title=i.text 
    job_title.append(title)
    
# scraping Job Experience from the given page
experience_tags=driver.find_elements (By.XPATH, '//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in experience_tags:
    exp=i.text 
    experience_required.append(exp)



# scraping Job Location from the given page
location_tags=driver.find_elements(By.XPATH, '//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]') 
for i in location_tags:
    location=i.text 
    job_location.append(location)

# scraping Company name from the given page
company_tags=driver.find_elements(By.XPATH, '//div[@class="jobCard_jobCard_cName__mYnow"]/span') 
for i in company_tags:
    company=i.text
    company_name.append (company)

print(len (job_title),len (job_location), len (company_name), len (experience_required))

    
df=pd.DataFrame ({'Job Title':job_title,'Location':job_location, 'Company_name' : company_name, 'Experience': experience_required})
df


# ### Q2:Write a python program to scrape data for “Data Scientist” Job position in“Bangalore” location. You
# have to scrape the job-title, job-location, company_name. You have to scrape first 10 jobs data.
# This task will be done in following steps:
# 1. First get the webpage https://www.shine.com/
# 2. Enter “Data Scientist” in “Job title, Skills” field and enter “Bangalore” in “enter thelocation” field.
# 3. Then click the search button.
# 4. Then scrape the data for the first 10 jobs results you get.
# 5. Finally create a dataframe of the scraped data.
# Note: All of the above steps have to be done in code. No step is to be done manually.

# In[55]:


import selenium 
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.shine.com/new/job-search")

job_role = driver.find_element(By.CLASS_NAME, "form-control")
job_role.send_keys('Data Scientist')
location = driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys('Bangalore')
experience = driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div/form/div/div[1]/ul/li[3]/div/input[1]")
experience.send_keys('11')

search_button = driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div/form/div/div[2]/div/button")

search_button.click()

job_title = []
job_location = []
company_name = []
experience_required = []

# scraping Job title from the given page

title_tags=driver.find_elements(By.XPATH, '//div[@class ="jobCard_jobCard__jjUmu  white-box-border jobCard" or @class="jobCard_jobCard__jjUmu active white-box-border jobCard"]/div/h2/a') 
for i in title_tags:
    title=i.text 
    job_title.append(title)
    
# scraping Job Experience from the given page
experience_tags=driver.find_elements (By.XPATH, '//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for i in experience_tags:
    exp=i.text 
    experience_required.append(exp)



# scraping Job Location from the given page
location_tags=driver.find_elements(By.XPATH, '//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]') 
for i in location_tags:
    location=i.text 
    job_location.append(location)

# scraping Company name from the given page
company_tags=driver.find_elements(By.XPATH, '//div[@class="jobCard_jobCard_cName__mYnow"]/span') 
for i in company_tags:
    company=i.text
    company_name.append (company)

print(len (job_title),len (job_location), len (company_name), len (experience_required))

    
df=pd.DataFrame ({'Job Title':job_title,'Location':job_location, 'Company_name' : company_name, 'Experience': experience_required})
df


# ### Q3: In this question you have to scrape data using the filters available on the webpage
#  You have to use the location and salary filter.
# You have to scrape data for “Data Scientist” designation for first 10 job results.
# You have to scrape the job-title, job-location, company name, experience required.
# The location filter to be used is “Delhi/NCR”. The salary filter to be used is “3-6” lakhs
# The task will be done as shown in the below steps:
# 1. first get the web page https://www.shine.com/
# 2. Enter “Data Scientist” in “Skill, Designations, and Companies” field.
# 3. Then click the search button.
# 4. Then apply the location filter and salary filter by checking the respective boxes
# 5. Then scrape the data for the first 10 jobs results you get.
# 6. Finally create a dataframe of the scrapeddata.
# Note: All of the above steps have to be done in code. No step is to be done manually.

# In[75]:


import selenium 
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.shine.com/new/job-search")

job_role = driver.find_element(By.CLASS_NAME, "form-control")
job_role.send_keys('Data Scientist')

search_button = driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div/form/div/div[2]/div/button")

search_button.click()

search_location = driver.find_element(By.CLASS_NAME,"filter_filter_lists_items__wlFfo")
search_location.click()
time.sleep(2)

search_delhi = driver.find_element(By.CLASS_NAME,"filter_filter_option_label__v_iAW")
search_delhi.click()
time.sleep(2)

#sleep.time(2)

location = driver.find_element(By.XPATH,'//li[@class="pr-20 mb-15"]/input')
location.send_keys('Delhi')
time.sleep(2)

select_location = driver.find_element(By.CLASS_NAME,"styled-checkbox")
select_location.click()


time.sleep(3)
# I am struggling to add the wait time in my program , looks like it's not able to find the location 
# input tag because till the time location filter is opening my program finished it's execution and it's getting
# ElementClickInterceptedException  on click event for seleting Delhi checkbox


# In[ ]:





# ### Q4: Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:
# To scrape the data you have to go through following steps:
# 1. Go to Flipkart webpage by url :https://www.flipkart.com/
# 2. Enter “sunglasses” in the search fieldwhere “search for products, brands and more” is written and
# click the search icon
# 3. After that you will reach to the page having a lot of sunglasses. From this page you can scrap the
# required data as usual.
# 4. After scraping data from the first page, go to the “Next” Button at the bottom other page , then
# click on it.
# 5. Now scrape data from this page as usual
# 6. Repeat this until you get data for 100sunglasses.
# Note: That all of the above steps have to be done by coding only and not manually
# 

# In[100]:


import selenium 
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time

warnings.filterwarnings('ignore')

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")    #to open the Flipkart website

search = driver.find_element(By.XPATH, '//input[@class="Pke_EE"]')  #to Insert 'sunglasses' in search bar
search.send_keys('sunglasses')
close_pop_up  = driver.find_element(By.CLASS_NAME,'_30XB9F')   #to close login popup
close_pop_up.click()
search_button = driver.find_element(By.CLASS_NAME,'_2iLD__')  #to click on search button 
search_button.click()

start = 0
end = 3
brand = []
discription = []
price = []
discount = []
for page in range(start,end):  #to scrap brand names
    brand_name = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')              
    for i in brand_name :
        brand.append(i.text)
        
    #to scarp product description     
    product_discription = driver.find_elements(By.XPATH,'//a[@class="IRpwTa _2-ICcC" or @class="IRpwTa"]')              
    for i in product_discription  :
        discription.append(i.text)
        
    #to scarp product price   
    product_price = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')              
    for i in product_price  :
        price.append(i.text)
    #to scarp product discount    
    product_discount = driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')              
    for i in product_discount  :
        discount.append(i.text)
    
    #to click on next button 
    next_button = driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(3)
    
# creating a data frame
df = pd.DataFrame ({'Brand':brand ,'Price':price,'Discription':discription,'Discount':discount})
df


# ### Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link: https://www.flipkart.com/apple-iphone-11-black-64-gb/product- reviews/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZXSHRJ&market place=FLIPKART
# As shown in the above page you have to scrape the tick marked attributes. These are:
# 1. Rating
# 2. Review summary
# 3. Full review
# 4. You have to scrape this data for first 100reviews.
# Note: All the steps required during scraping should be done through code only and not manually.
# 

# In[77]:


import selenium 
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time

warnings.filterwarnings('ignore')

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/apple-iphone-11-black-64-gb/p/itm4e5041ba101fd?pid=MOBFWQ6BXGJCEYNY&lid=LSTMOBFWQ6BXGJCEYNYZE3ENS&marketplace=FLIPKART&q=iphone%2011&sattr[]=color&sattr[]=storage&st=color") 
# above given URL was not working(page not found)so i searched for the Mentioned product manually and then copied this URL from there


start = 0
end = 10
rating = []
review = [] 
full_review = []
time.sleep(4)

all_review = driver.find_element(By.XPATH,'//div[@class="_3UAT2v _16PBlm"]')
all_review.click()

time.sleep(3)

for page in range(start,end):
    product_rating = driver.find_elements(By.XPATH,'//div[@class="_3LWZlK _1BLPMq"]') 
    for i in product_rating:
        rating.append(i.text)
    
    review_summary = driver.find_elements(By.XPATH,'//p[@class="_2-N8zT"]') 
    for i in review_summary :
        review.append(i.text) 
        
    Full_review = driver.find_elements(By.XPATH,'//div[@class="t-ZTKy"]/div[1]/div') 
    for i in  Full_review:
        full_review.append(i.text) 
   
    next_button = driver.find_element(By.XPATH,'//a[@class="_1LKTO3" and span/text()="Next"]')
    next_button.click()
    time.sleep(4)
    
# creating a data frame    
    
df = pd.DataFrame ({'rating':rating,'Product review':review,'full review ':full_review})
df
    


# ### Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com and search for “sneakers” in the search field.
# You have to scrape 3 attributes of each sneaker:
# 1. Brand
# 2. Product Description
# 3. Price
# As shown in the below image, you have to scrape the above attributes.

# In[17]:


import selenium 
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time

warnings.filterwarnings('ignore')

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")    #to open the Flipkart website

search = driver.find_element(By.XPATH, '//input[@class="Pke_EE"]')   # to scrap the search bar  
search.send_keys('sneakers')   # to type 'sneakers' in to search bar

close_pop_up  = driver.find_element(By.CLASS_NAME,'_30XB9F')    # to close login popup
close_pop_up.click()

search_button = driver.find_element(By.CLASS_NAME,'_2iLD__')   # to click on search Button 
search_button.click()

# to scrap product brand,price,discription
# to scrap the data from first 3 pages
start = 0
end = 3
price = []
discription = []  # creating empty lists to Store the brand,price,discription data
brand = []
numberofItems = 0

while start <= numberofItems:  # while loop until it breaks on 100th element 
    
    #useing relative xpath to scrap multiple price elements
    product_price = driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]') 
         
    for i in product_price  :
        if(len(price)<100): # on the single page it might have 40+ elements so check if length array reached to 100
            price.append(i.text)
            
    #useing relative xpath to scrap multiple  product discription  elements
    product_discription = driver.find_elements(By.XPATH,'//a[@class="IRpwTa _2-ICcC" or  @class="IRpwTa"]')    
    #Above element have 2 different class for descriptions element so used OR condition 
    for i in product_discription  :
        if(len(discription)<100):
            discription.append(i.text)
            
    #useing relative xpath to scrap multiple  brand names      
    brand_name = driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')  
         
    for i in brand_name :
        if(len(brand)<100):
            brand.append(i.text)
            
    # to scrap the NEXT button 
    next_button = driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')

    numberofItems = len(price)
    if(numberofItems >= 100):  # if number items more than 100 then break the loop 
        break
    else:
        next_button.click()
        time.sleep(3)

    
# creating a data frame    
    
df = pd.DataFrame ({'Price':price,'Product Description':discription,'Product Brand':brand})
df


# ### Q7: Go to webpage https://www.amazon.in/ Enter “Laptop” in the search field and then click the search icon. Then set CPU Type filter to “Intel Core i7” as shown in the below image:
# After setting the filters scrape first 10 laptops data. You have to scrape 3 attributes for each laptop:
# 1. Title
# 2. Ratings
# 3. Price

# In[91]:


import selenium 
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time

warnings.filterwarnings('ignore')

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")   

search_input = driver.find_element(By.XPATH,'//div[@class="nav-search-field "]/input')
search_input.send_keys('Laptop')
search_submit = driver.find_element(By.XPATH,'//input[@class="nav-input nav-progressive-attribute" and @type="submit"]')
search_submit.click()

title = []
price = []
rating = []

# scraping Title from the given page
title_tags=driver.find_elements (By.XPATH, '//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]')[1:11]
for i in title_tags:
    titleText=i.text 
    title.append(titleText)

# scraping Title from the given page
price_tags=driver.find_elements (By.XPATH, '//div[@class="a-section a-spacing-none a-spacing-top-micro puis-price-instructions-style"]/div/div/a/span')[1:11]
for i in price_tags:
    priceText=i.text 
    price.append(priceText)
#Could Not fetch the Rating of the product 

df = pd.DataFrame ({'Title':title,'price':price})
df


# ### Q8: Write a python program to scrape data for Top 1000 Quotes of All Time. The above task will be done in following steps:
# 1. First get the webpagehttps://www.azquotes.com/
# 2. ClickonTopQuotes

# In[110]:


import selenium 
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time

warnings.filterwarnings('ignore')

driver = webdriver.Chrome()
driver.get("https://www.azquotes.com/")  

top_qoutes = driver.find_element(By.XPATH,'//div[@class="mainmenu"]//ul/li/a[text()="Top Quotes"]')
top_qoutes.click()
time.sleep(1)

start = 0
title = []

numberofItems = 0

while start <= numberofItems:  # while loop until it breaks on 1000th element 
    
    #useing relative xpath to scrap multiple title elements
    qoute_title = driver.find_elements(By.XPATH,'//a[@class="title"]') 
         
    for i in qoute_title  :
        if(len(price)<1000): # on the single page it might have 1000+ elements so check if length array reached to 100
            title.append(i.text)
            
  
            
    # to scrap the NEXT button 
    try:
        next_button = driver.find_element(By.XPATH,'//li[@class="next"]')
    except NoSuchElementException:
        print("")


    numberofItems = len(title)
    if(numberofItems >= 900):  # Not able to skip the click event on next button and Next button not availble on last page so collecting 900 titles 
        break
    else:
        next_button.click()
        time.sleep(3)

    
# creating a data frame    
    
df = pd.DataFrame ({'Title':title})
df



# In[ ]:





# In[ ]:




