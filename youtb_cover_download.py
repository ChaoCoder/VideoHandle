#coding=utf-8
import urllib
import urllib2
import os
import argparse


def save_img(img_url,file_name,file_path=os.path.abspath(os.curdir)+'/Desktop/python'):
    #保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 book\img文件夹
    try:
        if not os.path.exists(file_path):
            print '文件夹',file_path,'不存在，重新建立'
            #os.mkdir(file_path)
            os.makedirs(file_path)
        #获得图片后缀
        file_suffix = os.path.splitext(img_url)[1]
        #拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path,os.sep,file_name,file_suffix)
       #下载图片，并保存到文件夹中
        f = urllib2.urlopen(img_url) 
        with open(filename, "wb") as code:
            code.write(f.read())

    except IOError as e:
        print 'file fail',e
    except Exception as e:
        print 'error :',e


def getArg():
	global OLD_URL
	parser = argparse.ArgumentParser(description='manual to this script')
	parser.add_argument('--url_end', type=str, default = None)
	args = parser.parse_args()
	OLD_URL = args.url_end        

if __name__ == '__main__':
	getArg()
	img_url = 'https://i.ytimg.com/vi/' + OLD_URL + '/maxresdefault.jpg'
	save_img(img_url,OLD_URL)

# url = 'https://i.ytimg.com/vi/PImiLIKjN3s/maxresdefault.jpg' 