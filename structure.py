# HTML/CSS/Xpath tiktok structure

################### Views Function #########################
css_verified = '#main-content-others_homepage > div > div.tiktok-1g04lal-DivShareLayoutHeader-StyledDivShareLayoutHeaderV2.enm41492 > div.tiktok-1gk89rh-DivShareInfo.ekmpd5l2 > div.tiktok-1nbnul7-DivShareTitleContainer.ekmpd5l3 > h2 > svg'

xpath_avatar_verified = '//*[@id="app"]/div[3]/div[2]/div/div[1]/div[1]/div[1]/span/img'

xpath_avatar_non_verified = '//*[@id="app"]/div[3]/div[2]/div/div[1]/div[1]/a/div/span[1]/img'

xpath_following = '//strong[contains(@data-e2e,"following-count")]'

xpath_follower = '//strong[contains(@data-e2e,"followers-count")]'

xpath_likes = '//strong[contains(@data-e2e,"likes-count")]'

xpath_click = '//*[@id="tiktok-verify-ele"]/div/div[1]/div[1]'

def xpath_view_func(i: int=0+1) :
    element = '//*[@id="main-content-others_homepage"]/div/div[2]/div[2]/div/div['+str(i+1)+']/div[1]/div/div/a/div/div[2]/strong'
    return element

def xpath_view_func_sec(i: int=0+1) :
    element = '//*[@id="main-content-others_homepage"]/div/div[2]/div[3]/div/div['+str(i+1)+']/div[1]/div/div/a/div/div[2]/strong'
    return element

def xpath_url_func(i: int=0+1) :
    element = '//*[@id="app"]/div[3]/div[2]/div/div[2]/div[2]/div/div['+str(i+1)+']/div[1]/div/div/a'
    return element

def xpath_url_func_sec(i: int=0+1) :
    element = '//*[@id="app"]/div[3]/div[2]/div/div[2]/div[3]/div/div['+str(i+1)+']/div[1]/div/div/a'
    return element

################### Detail Function #########################
xpath_like_detail = "//strong[contains(@data-e2e,'like-count')]"

xpath_comment_detail = "//strong[contains(@data-e2e,'comment-count')]"

xpath_share_detail = "//strong[contains(@data-e2e,'share-count')]"

def xpath_view_detail_func(link:str) :
    element = "//a[contains(@href,'"+ link +"')]/div/div[2]/strong"
    return element