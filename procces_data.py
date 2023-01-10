#**************** Proccess view ****************#
def procces_view(dt:dict):
    respond = {}
    
    respond['status'] = dt['status']
    respond['message'] = dt['message']
    respond['is_verified'] = dt['is_verified']
    respond['avatar'] = dt['avatar']
    following = dt['following']
    follower = dt['follower']
    likes = dt['likes']
    content = dt['content']

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
            data[i] = data[i]
    
    respond['following'] = data[0]
    respond['follower'] = data[1]
    respond['likes'] = data[2]

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
            content[k]['view'] = content[k]['view']
    
    respond['content'] = content
    return respond


#**************** Proccess detail ****************#
def procces_detail(dt:dict):
    respond = {}

    respond['status'] = dt['status']
    respond['message'] = dt['message']
    views = dt['views']
    like = dt['like']
    comment = dt['comment']
    share = dt['share']

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
            data[i] = data[i]
    
    respond['views'] = data[0]
    respond['like'] = data[1]
    respond['comment'] = data[2]
    respond['share'] = data[3]

    return respond