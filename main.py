import json
from requests import get

def GetPic():
    headers = {'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
    api_url = r'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    api = get(api_url,headers=headers)
    json_data = json.loads(api.text)
    pic_url = r'https://www.bing.com{0}'.format(json_data['images'][0]['url'])
    start_date = json_data['images'][0]['startdate']
    open(r'./json/today.json', 'wb').write(api.content)
    open(r'./json/{0}.json'.format(start_date), 'wb').write(api.content)
    pic_json = dict()
    pic_json['imgurl'] = pic_url
    pic_json['copyright'] = json_data['images'][0]['copyright']
    open(r'./json/{0}-simple.json'.format(start_date), 'wb').write(json.dumps(pic_json).encode('utf-8'))
    open(r'./json/today-simple.json'.format(start_date), 'wb').write(json.dumps(pic_json).encode('utf-8'))
    print('Create Json Success!')
    pic = get(pic_url, stream=True)
    if(pic.status_code == 200):
        open(r'./pic/today.png', 'wb').write(pic.content)
        open(r'./pic/{0}.png'.format(start_date), 'wb').write(pic.content)
        print('Create Image Success!')
    else:
        print('Create Image Faild!')

if __name__ == "__main__":
    GetPic()