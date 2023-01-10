# FastAPI setup
from fastapi import FastAPI, HTTPException, status, Form, Header
from starlette.responses import JSONResponse

# Selenium setup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Another library
import time

# Your library
import structure
import procces_data

app = FastAPI()

@app.post("/api/scrapviews")
async def scrap_view(link: str = Form(...)):
    """
    Function to pull data from tiktok (raw_data)
    respond :
        status : True/False,
        message : success/failed,
        is_verified : verified,
        avatar : avatar,
        following : following,
        follower : follower,
        likes : likes,
        content : content
    """

    # Connection
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=chrome_options)

    # User
    #user = '3stripesid'
    
    # Output
    respond = {}
    
    # Engine
    try :
        driver.get(link)

        respond['status'] = True
        respond['message'] = 'Success'

        try :
            respond['following'] = driver.find_element(By.XPATH, structure.xpath_following).text
        except :
            respond['following'] = 'Unknown'
        try :
            respond['follower'] = driver.find_element(By.XPATH, structure.xpath_follower).text
        except :
            respond['follower'] = 'Unknown'
        try :
            respond['likes'] = driver.find_element(By.XPATH, structure.xpath_likes).text
        except :
            respond['likes'] = 'Unknown'

        try :
            driver.find_element(By.CSS_SELECTOR, structure.css_verified)
            respond['is_verified'] = True
        except :
            respond['is_verified'] = False
        try :
            try :
                avatar = driver.find_element(By.XPATH, structure.xpath_avatar_verified)
                respond['avatar'] = avatar.get_attribute('src')
            except :
                avatar = driver.find_element(By.XPATH, structure.xpath_avatar_non_verified)
                respond['avatar'] = avatar.get_attribute('src')
        except :
            respond['avatar'] = 'Unknown'

        urls = []
        for i in range(12) :
            try :
                url = driver.find_element(By.XPATH, structure.xpath_url_func(i)).get_attribute('href')
                if url is str('') :
                    driver.find_element(By.XPATH, structure.xpath_click).click()
                    url = driver.find_element(By.XPATH, structure.xpath_url_func(i)).get_attribute('href')
                    urls.append(url)
                else :
                    urls.append(url)
            except :
                urls.append('Unknown')

        views = []
        for i in range(12) :
            try :
                view = driver.find_element(By.XPATH, structure.xpath_view_func(i)).text
                if view is str('') :
                    driver.find_element(By.XPATH, structure.xpath_click).click()
                    view = driver.find_element(By.XPATH, structure.xpath_view_func(i)).text
                    views.append(view)
                else :
                    views.append(view)
            except :
                views.append('Unknown')

        respond['content'] = []
        for i in range(12) :
            dic = {
                "url" : urls[i],
                "view":views[i]
            }
            respond['content'].append(dic)

        driver.quit()
        time.sleep(1) 
        return JSONResponse(
            status_code=200,
            content=procces_data.procces_view(respond)
            ) 

    except:
        driver.quit()
        time.sleep(1)
        raise HTTPException(
            status_code=404,
            detail="Please make sure your link is valid or contact developer if still in trouble"
        )

@app.post("/api/scrapdetail")
async def scrap_detail(link_profile: str = Form(...), link: str = Form(...)):
    """
    Function to pull data from tiktok (detail_data)
    respond :
        status : True/False,
        message : success/failed,
        views : views,
        like : like,
        comment : comment,
        share : share
    """

    # Connection
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=chrome_options)

    # Output
    respond = {}
    
    link = link 
    link_profile = link_profile
    
    if link.split('/')[3] != link_profile.split('/')[3] :
        raise HTTPException(status_code=500,
                            detail="Parameter link and link_profile are not match")
    # Engine
    else :
        driver.get(link + '/')
        respond['status'] = True
        respond['message'] = 'Success'
        try :
            respond['like'] = driver.find_element(By.XPATH, structure.xpath_like_detail).text
            if respond['like'] is str('') :
                driver.find_element(By.XPATH, structure.xpath_click).click()
                respond['like'] = driver.find_element(By.XPATH, structure.xpath_like_detail).text
        except :
            driver.find_element(By.XPATH, structure.xpath_click).click()
            respond['like'] = driver.find_element(By.XPATH, structure.xpath_like_detail).text
        try :
            respond['comment'] = driver.find_element(By.XPATH, structure.xpath_comment_detail).text
            if respond['comment'] is str('') :
                driver.find_element(By.XPATH, structure.xpath_click).click()
                respond['comment'] = driver.find_element(By.XPATH, structure.xpath_comment_detail).text
        except :
            driver.find_element(By.XPATH, structure.xpath_click).click()
            respond['comment'] = driver.find_element(By.XPATH, structure.xpath_comment_detail).text
        try :
            respond['share'] = driver.find_element(By.XPATH, structure.xpath_share_detail).text
            if respond['share'] is str('') :
                driver.find_element(By.XPATH, structure.xpath_click).click()
                respond['share'] = driver.find_element(By.XPATH, structure.xpath_share_detail).text
            if respond['share']  == "Share" :
                respond['share'] = '0'
            else :
                respond['share']
        except :
            driver.find_element(By.XPATH, structure.xpath_click).click()
            respond['share']  = driver.find_element(By.XPATH, structure.xpath_share_detail).text
            if respond['share'] == "Share" :
                respond['share'] = '0'
            else :
                respond['share']
        
        driver.quit()
        time.sleep(1.5)

        #**************** Second view profile for get views ********************#
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=chrome_options)
        driver.get(link_profile + '/')

        try :
            respond['views'] = driver.find_element(By.XPATH, structure.xpath_view_detail_func(link)).text
            if respond['views'] is str('') :
                driver.find_element(By.XPATH, structure.xpath_click).click()
                respond['views'] = driver.find_element(By.XPATH, structure.xpath_view_detail_func(link)).text

            driver.quit()
            time.sleep(1)
            return JSONResponse(
                status_code=200,
                content=procces_data.procces_detail(respond)
                )
        
        except :
            respond['views'] = 'Unknown'

            driver.quit()
            time.sleep(1)
            return JSONResponse (
                status_code=200,
                content=procces_data.procces_detail(respond)
            )
        
