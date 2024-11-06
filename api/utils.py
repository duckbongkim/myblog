def obj_to_post(obj, flag=True):
    post = dict(vars(obj)) ## obj 로 들어오는 속성들을 딕셔너리 형태로 저장

    if obj.category: 
        post['category'] = obj.category.name
    else:
        post['category'] = 'NoCategory'

    if obj.tags:
       post['tags'] = [t.name for t in obj.tags.all()] 
    else:
        post['tags'] = []

    if obj.image:
        post['image'] = obj.image.url
    else:
        post['image'] = 'https://via.placeholder.com/900x300/'

    if obj.update_dt:
        post['update_dt'] = obj.update_dt.strftime('%Y-%m-%d %H:%M:%S')
    else:
        post['update_dt'] = '9999-12-12 00:00:00'
    

    del post['_state'],post['category_id'],post['create_dt']

    if not flag:
        del post['tags'], post['update_dt'], post['description'], post['content']

    return post

def prev_next_post(obj):
    try:
        prevObj = obj.get_previous_by_update_dt()
        prevDict = {
            'id':prevObj.id,
            'title':prevObj.title
        }
    except obj.DoesNotExist:
        prevDict={}


    try:
        nextObj = obj.get_next_by_update_dt()
        nextDict = {
            'id':nextObj.id,
            'title':nextObj.title
        }
    except obj.DoesNotExist:
        nextDict={}
    
    return prevDict, nextDict    
