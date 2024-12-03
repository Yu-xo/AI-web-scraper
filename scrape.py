import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

def scrape_web(website):
    print("launching chrome ..................")
    
    
    chrome_driver_path = "./chromedriver.exe"
    options =  webdriver.ChromeOptions()
    driver  = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
    
    try:
        driver.get(website)
        print("loaded page")
        html = driver.page_source
        time.sleep(10)
        return html
    
    finally:
        driver.quit()
        
def extract_body_con(html_content):
    soup = BeautifulSoup(html_content,"html.parser")
    body_con = soup.body
    if body_con:
        return str(body_con)
    return

def clean_body_con(body_con):
    soup  = BeautifulSoup(body_con,"html.parser")
    
    for script_or_style in soup(["script","style"]):
        script_or_style.extract()
        
        
    cleaned_con =  soup.get_text(separator="\n")
    cleaned_con = "\n".join(
        line.strip() for line in cleaned_con.splitlines() if line.strip()
    )
    
    return cleaned_con

def split_dom_contant(dom_con , max_lenght = 7000):
    return[
        dom_con[i:i+max_lenght] for i in range(0,len(dom_con),max_lenght)
    ]
    
    