# 下载MP3文件到本地
import os
import requests


def DownloadFile(mp3_url, save_url, file_name):
    try:
        if mp3_url is None or save_url is None or file_name is None:
            print('参数错误')
            return None
        # 文件夹不存在，则创建文件夹
        folder = os.path.exists(save_url)
        if not folder:
            os.makedirs(save_url)
        # 读取MP3资源
        res = requests.get(mp3_url, stream=True)
        # 获取文件地址
        file_path = os.path.join(save_url, file_name)
        print('开始写入文件：', file_path)
        # 打开本地文件夹路径file_path，以二进制流方式写入，保存到本地
        with open(file_path, 'wb') as fd:
            for chunk in res.iter_content():
                fd.write(chunk)
        print(file_name + ' 成功下载！')
    except:
        print("程序错误")


if __name__ == "__main__":
    # MP3源地址url
    ##url = 'https://mp3.jiuku.9ku.com/upload/128/2017/08/03/863848.mp3'
    ##url = 'https://mp3.9ku.com/hot/2005/11-01/72064.mp3'
    ##url = 'http://antiserver.kuwo.cn/anti.s?rid=MUSIC_38913046&response=res&format=mp3|aac&type=convert_url&br=128kmp3&agent=iPhone&callback=getlink&jpcallback=getlink.mp3'
    url = 'https://www.littleducks.cn/uploads/mp3/ypylubinghuamp3.mp3'
    # MP3保存文件夹
    save_url = '/Users/hrtps/Desktop/music'
    # MP3文件名
    file_name = '鲁冰花.mp3'
    DownloadFile(url, save_url, file_name)
