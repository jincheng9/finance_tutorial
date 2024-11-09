import requests
from bs4 import BeautifulSoup
import pandas as pd

url_prefix = "http://www.pbc.gov.cn/diaochatongjisi/116219/116225/11871/"

def get_stat_date(page_index):
    pub_date_list = []
    url_page = url_prefix + "index"+str(page_index)+".html"
    response = requests.get(url_page)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    for font_tag in soup.find_all('font', class_="newslist_style"):
        a_tag = font_tag.find('a', href=True, title=True)
        if a_tag and "金融统计数据报告" in a_tag['title']:
            # 问题在于，<span>标签不是<font>标签的直接子元素
            # 所以我们从<font>的父级开始寻找下一个<span>标签
            next_span = font_tag.find_next_sibling('span')
            if next_span:
                pub_date_list.append(next_span.text)
            else:
                print(f"{a_tag['title']}: 没有找到对应的日期")
    return pub_date_list    

if __name__ == "__main__":
    total_page_size = 35
    date_list = []
    for i in range(1, total_page_size+1):
        pub_date_list = get_stat_date(page_index=i)
        if len(pub_date_list) > 0:
            date_list = date_list + pub_date_list
    print(date_list)
    df = pd.DataFrame()
    df['pub_date'] = date_list
    df.to_csv("./pub_date.csv", index=False)