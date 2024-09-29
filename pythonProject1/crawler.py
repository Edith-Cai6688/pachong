import json
import re
import requests
import datetime
from bs4 import BeautifulSoup
import os

def crawl_wiki_data():
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    url = 'https://baike.baidu.com/item/乘风破浪的姐姐'

    try:
        response=requests.get(url,headers=headers)
        soup=BeautifulSoup(response.text,'lxml')

        tables=soup.find_all('div',attrs={"data-module-type":"table"})
        crawl_table_title="*（按姓氏首字母排序）"
        # return tables
        table_titles_list = []
        for table in tables:
            table_titles=table.find_previous("div")
            # table_titles_list.append(table_titles)
        # return table_titles_list
            for title in table_titles:
                if(crawl_table_title in title):
                    return table
    except Exception as e:
        print(e)

def parse_wili_data(table_html):
    # bs=BeautifulSoup(str(table_html),'lxml')
    all_trs=table_html.find_all('tr')

    stars=[]
    for tr in all_trs:
        all_tds=tr.find_all('td')

        for td in all_tds:
            star={}
            if td.find('a'):
                star["name"]=td.find('a').text
                star["link"]="https://baike.baidu.com"+td.find('a').get('href')
            stars.append(star)

    # return stars
    json_data=json.loads(str(stars).replace("\'","\""))
    # return json_data
    with open("D:/BaiduSyncdisk/Edith/Study/3(1)/AI/strong_sister_spider/pachong/pythonProject1/"+'stars.json','w',encoding='UTF-8')as f:
        json.dump(json_data,f,ensure_ascii=False)

def crawl_everyone_wiki_urls():
    with open("D:/BaiduSyncdisk/Edith/Study/3(1)/AI/strong_sister_spider/pachong/pythonProject1/" + 'stars.json', 'r',
              encoding='UTF-8') as f:
        json_array=json.loads(f.read())
        # return json_array

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        star_infos=[]
        for star in json_array:
            # return star
            star_info={}
            name=star['name']
            # return names
            link=star['link']
            star_info['name']=name
            response=requests.get(link,headers=headers)
            bs=BeautifulSoup(response.text,'lxml')
            # return bs
            base_info_div = bs.find('div', {'class': 'basicInfo_K4cst J-basic-info'})
            # return base_info_div
            dls = base_info_div.find_all('dl')
            for dl in dls:
                dts=dl.find_all('dt')
                for dt in dts:
                    if "".join(str(dt.text).split())=='民族':
                        star_info['nation']=dt.find_next('dd').text
                    if "".join(str(dt.text).split()) == '星座':
                        star_info['constellation'] = dt.find_next('dd').text
                    if "".join(str(dt.text).split()) == '血型':
                        star_info['blood_type'] = dt.find_next('dd').text
                    if "".join(str(dt.text).split()) == '身高':
                        height_str = dt.find_next('dd').text
                        star_info['height'] = height_str[0:height_str.rfind('cm')-1]
                    if "".join(str(dt.text).split()) == '体重':
                        weight_str=dt.find_next('dd').text
                        star_info['weight'] = weight_str[0:weight_str.rfind('kg')-1]
                    if "".join(str(dt.text).split()) == '出生日期':
                        birth_day_str = dt.find_next('dd').text
                        if '年' in birth_day_str:
                            star_info['birth_day'] = birth_day_str[0:birth_day_str.rfind('年')]
                # return star_info
            star_infos.append(star_info)
        json_data = json.loads(str(star_infos).replace("'", '"').replace('\\', '\\\\'))
        with open('D:/BaiduSyncdisk/Edith/Study/3(1)/AI/strong_sister_spider/pachong/pythonProject1/' + 'stars_info.json', 'w', encoding='UTF-8') as f:
            json.dump(json_data, f, ensure_ascii=False)

            # bs_pic=bs.find('a',{"class":"albumWrapper_Te1x_ layoutRight_vCQtD disable-select"})
            # pic_list_url=bs_pic.get("href")
            # pic_list_url = 'https://baike.baidu.com' + pic_list_url

            # return pic_list_url
            # pic_list=[]
            # for pic in bs_pic:
            #     pic_list_url=pic.get("href")
            #     pic_list_url = 'https://baike.baidu.com' + pic_list_url
            #     pic_list.append(pic_list_url)
            # return pic_list

            # proxies = {'http': 'http://your_proxy', 'https': 'https://your_proxy'}
            # pic_list_response = requests.get(pic_list_url, headers=headers)
            # return pic_list_response
            # bs = BeautifulSoup(pic_list_response.text, 'lxml')
            # pic_list_html = bs.find('div',{"class":"imgWraper_uvRF3"})
            # return pic_list_html
            # pic_urls = []






if __name__ == '__main__':
    # html=crawl_wiki_data()
    # parse_wili_data(html)
    crawl_everyone_wiki_urls()
 



