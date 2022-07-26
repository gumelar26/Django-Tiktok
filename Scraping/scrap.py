from selenium import webdriver
import time

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@csrf_exempt
def engineviews(request):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=chrome_options)
    
    driver.get(str(request.POST["link"]))
    try :
        verified = driver.find_element(By.CSS_SELECTOR, "#app > div.tiktok-ywuvyb-DivBodyContainer.e1irlpdw0 > div.tiktok-w4ewjk-DivShareLayoutV2.elmjn4l0 > div > div.tiktok-1g04lal-DivShareLayoutHeader-StyledDivShareLayoutHeaderV2.elmjn4l2 > div.tiktok-1gk89rh-DivShareInfo.ekmpd5l2 > div.tiktok-1hdrv89-DivShareTitleContainer.ekmpd5l3 > h2 > svg")
        verified = True
    except :
        verified = False
        
    avatars = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[1]/div[1]/div[1]/span/img')
    avatar = avatars.get_attribute('src')
    following = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[1]/h2[1]/div[1]/strong').text
    follower = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[1]/h2[1]/div[2]/strong').text
    likes = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[1]/h2[1]/div[3]/strong').text
    
    user_link = str(request.POST.get("link")) + '/video/'
    urls = driver.find_elements_by_xpath("//a[contains(@href,'"+ user_link +"')]")[:12]
    urls = [url.get_attribute('href') for url in urls]
    views = driver.find_elements_by_xpath("//strong[contains(@data-e2e,'video-views')]")[:12]
    views = [view.text for view in views]
    
    content = []
    for i in range(len(urls)):
        dic = {"url":urls[i],
            "view":views[i]}
        content.append(dic)
    
    respond = {
        "status" : True,
        "message": "succes",
        "is_verified" : verified,
        "avatar" : avatar,
        "following" : following,
        "follower" : follower,
        "likes" : likes,
        'content': content
    }
    
    #****************** Process Data ******************#
    
    verified = respond['is_verified']
    avatar = respond['avatar']
    following = respond['following']
    follower = respond['follower']
    likes = respond['likes']
    content = respond['content']

    data = [following, follower, likes]

    for i in range(len(data)):
        if data[i][-1:] == 'K' :
            data[i] = float(data[i][:-1]) * 1000
            data[i] = int(data[i])
        elif data[i][-1:] == 'M' :
            data[i] = float(data[i][:-1]) * 1000000
            data[i] = int(data[i])
        elif data[i][-1:] == 'B' :
            data[i] = float(data[i][:-1]) * 1000000000
            data[i] = int(data[i])
        else :
            data[i] = int(data[i])
        
    following = data[0]
    follower = data[1]
    likes = data[2]

    for k in range(len(content)) :
        if content[k]['view'][-1:] == 'K' :
            content[k]['view'] = float(content[k]['view'][:-1]) * 1000
            content[k]['view'] = int(content[k]['view'])
        elif content[k]['view'][-1:] == 'M' :
            content[k]['view'] = float(content[k]['view'][:-1]) * 1000000
            content[k]['view'] = int(content[k]['view'])
        elif content[k]['view'][-1:] == 'B' :
            content[k]['view'] = float(content[k]['view'][:-1]) * 1000000000
            content[k]['view'] = int(content[k]['view'])
        else :
            content[k]['view'] = int(content[k]['view'])
            
    respond = {
        "status" : True,
        "message": "succes",
        "is_verified" : verified,
        "avatar" : avatar,
        "following" : following,
        "follower" : follower,
        "likes" : likes,
        'content': content
    }
    driver.quit()
    time.sleep(2)
    return JsonResponse(respond, safe=False)

#################### Detail Function #####################

@csrf_exempt
def enginedetail(request):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    link = str(request.POST.get["link"])
    link_profile = str(request.POST.get["link_profile"])
    
    if link.split('/')[3] != link_profile.split('/')[3] :
        return JsonResponse('parameter link and link_profile are not match', safe=False)
    else :
        #**************** First view detail comment, like, share ****************#
        driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=chrome_options)
        driver.get(link + '/')
        like = driver.find_element_by_xpath("//strong[contains(@data-e2e,'like-count')]").text
        comment = driver.find_element_by_xpath("//strong[contains(@data-e2e,'comment-count')]").text
        share = driver.find_element_by_xpath("//strong[contains(@data-e2e,'share-count')]").text
        if share == "Share" :
            share = '0'
        else :
            share = share
        
        driver.quit()
        time.sleep(1.5)
        #**************** Second view profile for get views ********************#
        driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=chrome_options)
        driver.get(link_profile + '/')
        try :
            views = driver.find_element_by_xpath("//a[contains(@href,'"+ link +"')]/div/div[2]/strong").text
            #**************** Process Data if exists ****************#
            data = [views, like, comment, share]
            for i in range(len(data)):
                if data[i][-1:] == 'K' :
                    data[i] = float(data[i][:-1]) * 1000
                    data[i] = int(data[i])
                elif data[i][-1:] == 'M' :
                    data[i] = float(data[i][:-1]) * 1000000
                    data[i] = int(data[i])
                elif data[i][-1:] == 'B' :
                    data[i] = float(data[i][:-1]) * 1000000000
                    data[i] = int(data[i])
                else :
                    data[i] = int(data[i])
            
            views = data[0]
            like = data[1]
            comment = data[2]
            share = data[3]
            respond = {
                "status" : True,
                "message": "succes",
                "views" : views,
                "like": like,
                "comment": comment,
                "share": share
            }
        
            driver.quit()
            time.sleep(1)
            return JsonResponse(respond, safe=False)
        
        except :
            SCROLL_PAUSE_TIME = 1.5
            while True:
                last_height = driver.execute_script("return document.body.scrollHeight")
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(SCROLL_PAUSE_TIME)
                try :
                    views = driver.find_element_by_xpath("//a[contains(@href,'"+ link +"')]/div/div[2]/strong").text
                    #**************** Process Data if video in deep ****************#
                    data = [views, like, comment, share]
                    for i in range(len(data)):
                        if data[i][-1:] == 'K' :
                            data[i] = float(data[i][:-1]) * 1000
                            data[i] = int(data[i])
                        elif data[i][-1:] == 'M' :
                            data[i] = float(data[i][:-1]) * 1000000
                            data[i] = int(data[i])
                        elif data[i][-1:] == 'B' :
                            data[i] = float(data[i][:-1]) * 1000000000
                            data[i] = int(data[i])
                        else :
                            data[i] = int(data[i])
                    
                    views = data[0]
                    like = data[1]
                    comment = data[2]
                    share = data[3]
                    respond = {
                        "status" : True,
                        "message": "succes",
                        "views" : views,
                        "like": like,
                        "comment": comment,
                        "share": share
                    }
                    
                    driver.quit()
                    time.sleep(1)
                    return JsonResponse(respond, safe=False)
                
                except :
                    new_height = driver.execute_script("return document.body.scrollHeight")
                    if new_height == last_height :
                        driver.close()
                        time.sleep(1)
                        return JsonResponse('video not found', safe=False)
                    else :
                        None