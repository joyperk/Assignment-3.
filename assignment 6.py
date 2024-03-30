#!/usr/bin/env python
# coding: utf-8

# In[55]:


get_ipython().system('pip install selenium')


# In[88]:


from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By


# In[67]:


driver = webdriver.Chrome()


# In[69]:


driver.get('http://www.amazon.in/')


# In[70]:


search=driver.find_element(By.ID,"twotabsearchtextbox")
search.send_keys('Watch')


# In[71]:


search=driver.find_element(By.ID,"nav-search-submit-text")
search.click()


# In[72]:


product_title=[]
brand_name=[]
price=[]
exchange=[]
expected_delivery=[]
availability=[]
url=[]


# In[73]:


product_tags=driver.find_element(By.XPATH,'//span[@class="a-size-base-plus a-color-base a-text-normal"]')
for i in product_tags:
    product=i.text
    product_title.append(product)


# In[65]:


def scrape_product_details():
    products = []
    for page_num in range(1, 4):  # Scraping first 3 pages
        if page_num > 1:
            next_page = driver.find_element(By.XPATH, f"//li[@class='a-last']/a")
            next_page.click()
            time.sleep(3) 
        product_elements = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
        for product_element in product_elements:
            product_details = {}
            try:
                product_details['Brand Name'] = product_element.find_element(By.XPATH, ".//span[@class='a-size-base-plus a-color-base a-text-normal']").text
            except:
                product_details['Brand Name'] = '-'
            try:
                product_details['Name of the Product'] = product_element.find_element(By.XPATH, ".//h2/a/span").text
            except:
                product_details['Name of the Product'] = '-'
            try:
                product_details['Price'] = product_element.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
            except:
                product_details['Price'] = '-'
            try:
                product_details['Exchange'] = product_element.find_element(By.XPATH, ".//span[@class='a-color-state a-text-bold']").text
            except:
                product_details['Exchange'] = '-'
            try:
                product_details['Expected Delivery'] = product_element.find_element(By.XPATH, ".//span[contains(text(), 'Get it by')]").text
            except:
                product_details['Expected Delivery'] = '-'
            try:
                product_details['Availability'] = product_element.find_element(By.XPATH, ".//span[@class='a-size-small a-color-success']").text
            except:
                product_details['Availability'] = '-'
            try:
                product_details['Product URL'] = product_element.find_element(By.XPATH, ".//a[@class='a-link-normal a-text-normal']").get_attribute('href')
            except:
                product_details['Product URL'] = '-'
            products.append(product_details)
    return products


# In[5]:


def scrape_product_details():
    products = []
    for page in range(start, end):  # Scraping first 3 pages
        if page_num > 1:
            next_button = driver.find_element(By.XPATH, '//li[@class="s-list-item-margin-right-adjustment"]')
            next_page.click()
            time.sleep(3)  # Wait for the next page to load
        product_elements = driver.find_elements(By.XPATH, '//span[@class="a-size-base-plus a-color-base a-text-normal"]')
        for product_element in product_elements:
            product_details = []


# In[4]:


len(product)


# In[1]:


#que 3

from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By


# In[2]:


driver = webdriver.Chrome()


# In[3]:


driver.get('https://images.google.com')


# In[4]:


search_image=driver.find_element(By.CLASS_NAME,"gLFyf")
search_image.send_keys('Fruits')


# In[5]:


search_image=driver.find_element(By.CLASS_NAME,"zgAlFc")
search_image.click()


# In[6]:


#scraping fruit image

for i in range(20):
    driver.excute_script('window.scrollBy(0,500)')
    
img_url = []'//img[@class="YQ4gaf"]'
images = driver.find_element(By.XPATH,'//img[@class="YQ4gaf"]')

for image in images:
    source= image.get_attribute('src')
    if source in not None:
        if(source[0:4] == 'http'):
            img_urls.append(source)
            
for i in range(len(image_urls)):
    if i > 10:
        breakBy.XPATH,
        
    print('Downloading {0} of {1} images'.format(i, 10))
    response= request.get(img_urls[i])
        
    file = open(r"c:Users\HP\Desktop\Fliprobo"+str(i)+".jpg","wb")
    file.write(response.content)
    


# In[10]:


for _ in range(20):
     driver.execute_script('window.scrollBy(0,500)')
        
img_url = []
images = driver.find_element(By.XPATH,'//img[@class="YQ4gaf"]')


            


# In[13]:


for i in range(len(image_urls)):
    if i > 10:
        breakBy.XPATH,
    print('Downloading {0} of {1} images'.format(i, 10))
    response= request.get(img_urls[i])
        


# In[14]:


for image in images:
    source= image.get_attribute('src')
    if source in not None:
        if(source[0:4] == 'http'):
            img_urls.append(source)


# In[35]:


driver.close()


# In[6]:


from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By


# In[18]:


driver = webdriver.Chrome()


# In[19]:


driver.get('http://www.flipkart.com/')


# In[20]:


search=driver.find_element(By.CLASS_NAME,"Pke_EE")
search.send_keys('ONEPLUS NORD')


# In[21]:


search=driver.find_element(By.CLASS_NAME,"_2iLD__")
search.click()


# In[34]:


for i in urls:
    try:
        driver.get(i)
        
         try:
            brand_names=driver.find_element(By.XPATH,'//a[@class="_1fQZEK"]')
            brand_namess.append(oneplus_nord.text)
        except NoSuchElementException:
            brand_namess.append('-')
        except TimeoutException:
            brand_namess.append('-')
                    
                    


# In[ ]:





# In[74]:


driver = webdriver.Chrome()


# In[75]:


driver.get("https://www.google.com/maps")


# In[ ]:


search=driver.find_element(By.ID,"searchboxinput")
search.send_keys('Nagpur')


# In[ ]:


search=driver.find_element(By.ID,"searchbox-searchbutton")
search.click()


# In[76]:


try:
    url_string = driver.current_url()
    print('URL Extracted: ',url_string)
    
    lat_ing = re.findall(r'@(.*)data',url_string) 


# In[10]:


#que 7 
driver = webdriver.Chrome()


# In[6]:


driver.get("https://www.forbes.com/billionaires/")


# In[7]:


search=driver.find_element(By.CLASS_NAME,"q89hEMla")
search.send_keys('billionaires')


# In[8]:


search=driver.find_element(By.CLASS_NAME,"GxTuGQKY")
search.click()


# In[ ]:





# In[ ]:




