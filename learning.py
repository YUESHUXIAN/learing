import numpy as np
# a =np.array([1,2,3,4,5])
# b = np.array([10,20,30,40,50])
# print(a+b)


# np.array([1,2,3,4,5])
# np.array((1,2,3,4,5))
# d=np.array([[1,2,3],[4,5,6]])
# c=np.array(range(5))
# print(c)
# print(d)

# a=np.arange(10,20,2)
# print(a)
# b=np.linspace(1,10,5)
# # print(b)
# c=np.zeros((2,3))
# print(c)
# d=np.ones((2,3))
# print(d)

# a=np.random.rand(3,3)
# print(a)
# b=np.empty((3,3))
# print(b)


# data = np.array([[9.7, 8.8, 7.6], [6.5, 5.4, 4.3]])
# print(data.ndim)
# print(data.shape)
# print(data.size)
# print(data.dtype)

# arr = np.array([[1,2],[4,5],[5,6]])
# print(arr)
# print(arr.ndim)


# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# arr3 =np.hstack([arr1,arr2])
# print(arr3)
# arr4 = np.array([[1],[2],[3]])
# arr5 = np.array([[4],[5],[6]])
# arr6 = np.vstack([arr4,arr5])
# print(arr6)
# arr7 = np.concatenate([arr4,arr5],axis=1)
# print(arr7)
# arr8 = np.concatenate([arr4,arr5],axis=0)
# print(arr8)

# data = np.array([9.7, 8.8, 7.6, 6.5, 5.4, 4.3])
# print(data[0])
# print(data[data>8])
# print(data[(data>7)&(data<9)])
#
#
# data = np.array([6.8,9.1,9.7,8.8,7.6,6.5,5.4,4.3,4.3])
# print(np.mean(data))
# print(np.median(data))
# print(np.std(data))
# print(np.max(data))
# print(np.min(data))
# print(np.argmax(data))
# print(np.argsort(data))
# print(np.unique(data))




#
# import json
# with open('movies.json', 'r', encoding='utf-8') as f:
#     movies = json.load(f)
# ratings = np.array([m['rating']for m in movies])
#
# print(f"平均分{np.mean(ratings):2f} 最高 {np.max(ratings)}")
# print(f"标准差{np.std(ratings):2f} 中位 {np.median(ratings)}")
#
# high = ratings[ratings>= 8.0]
# top3 = np.argsort(ratings)[-3:][::-1]
# for i in top3:
#     print(movies[i]['title'],ratings[i])
#
# import string
# read_path = r"hamlet.txt"
# with open(read_path, 'r', encoding='utf-8') as text:
#     words = []
#     for raw_word in text.read().split():
#         clean_word = raw_word.strip(string.punctuation).lower()
#         if clean_word:
#             words.append(clean_word)
#
# counts = {}
# for word in words:
#     if word in counts:
#         counts[word] += 1
#     else:
#         counts[word] = 1
#
# for word in sorted(counts, key=lambda x: counts[x], reverse=True):
#     print(f'{word} -- {counts[word]} times')




# import jieba
# content_path = r"D:\cxdownload\《红楼梦》出场人物词频分析\《红楼梦》出场人物词频分析\Dream_of_the_Red_Mansion.txt"
# stop_words_path  = r"D:\cxdownload\《红楼梦》出场人物词频分析\《红楼梦》出场人物词频分析\cn_stopwords.txt"
# dictionary_path = r"D:\cxdownload\《红楼梦》出场人物词频分析\《红楼梦》出场人物词频分析\Red_Mansion_Dictionary.txt"
# jieba.load_userdict(dictionary_path)
# with open(content_path, "r", encoding='utf-8') as f:
#     content = f.read()
# with open(stop_words_path, "r", encoding='utf-8') as f:
#     stop_words_txt = f.read()
#
# with open(dictionary_path, "r", encoding='utf-8') as f:
#     dict_txt = f.read()
# stop_words = set(stop_words_txt)
# dictionary = jieba.lcut(dict_txt)
# dictionary = set(dictionary)
# words = jieba.lcut(content)
# counts = {}
# for word in words:
#     if len(word) == 1:
#         continue
#     if word in stop_words:
#         continue
#     counts[word] = counts.get(word, 0) + 1
# items = list(counts.items())
# items.sort(key=lambda x: x[1], reverse=True)
# for i in range(10):
#     word, count = items[i]
#     print(f"{word:<10}{count:>5}")


#
# import jieba
# from wordcloud import WordCloud
#
# content_path = r"D:\cxdownload\《红楼梦》出场人物词频分析\《红楼梦》出场人物词频分析\Red_Mansion_Dictionary.txt"
# f_content = open(content_path, "r", encoding="utf-8")
# content = f_content.read()
# f_content.close()
#
# words = jieba.lcut(content)
# txt_content = " ".join(words)
#
# w = WordCloud(
#     width = 1000,
#     height = 700,
#     background_color = "white",
#     font_path = r"C:\Windows\Fonts\simhei.ttf"
# )
#
# w.generate(txt_content)
# w.to_file(r"D:\cxdownload\《红楼梦》出场人物词频分析\《红楼梦》出场人物词频分析\RedMansionwordcloud.png")
# print("词云图片生成完成！")




# import sqlite3
# import json
# def get_emp_info(cur, n_limit=None):
#     emp_list = []
#     if n_limit:
#         sql = "SELECT * FROM employee LIMIT {}".format(n_limit)
#     else:
#         sql = "SELECT * FROM employee;"
#     rows = cur.execute(sql).fetchall()
#     col_names = [desc[0] for desc in cur.description]
#     for row in rows:
#         emp_dict = dict(zip(col_names, row))
#         emp_list.append(emp_dict)
#     return emp_list
# def main():
#     db_filepath = r"D:\cxdownload\company.db"
#     json_filepath = r"D:\cxdownload\employee_info.json"
#     conn = sqlite3.connect(db_filepath)
#     cursor = conn.cursor()
#     emp_data = get_emp_info(cursor, n_limit=50)
#     with open(json_filepath, 'w', encoding='utf-8') as f:
#         json.dump(emp_data, f, ensure_ascii=False, indent=2)
#     cursor.close()
#     conn.close()
#     print("数据已保存到employee_info.json")
#
# if __name__ == '__main__':
#     main()
#


#
# import requests
# from bs4 import BeautifulSoup
# import time
# from urllib.parse import urljoin
#
# if __name__ == '__main__':
#     url = 'http://hongloumeng.5000yan.com'
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
#     }
#     try:
#         req = requests.get(url, headers=headers, timeout=10)
#         req.encoding = 'utf-8'
#         soup = BeautifulSoup(req.text, features='html.parser')
#         with open("hongloumeng.txt", "w", encoding='utf-8') as f:
#             all_links = soup.find_all('a')
#             for a in all_links:
#                 href = a.get('href')
#                 if href and 'hlm' in href:
#                     title = a.get_text(strip=True)
#                     full_url = urljoin(url, href)
#                     try:
#                         page_req = requests.get(full_url, headers=headers, timeout=10)
#                         page_req.encoding = 'utf-8'
#                         page_soup = BeautifulSoup(page_req.text, features='html.parser')
#                         content_tag = page_soup.find(name='div', class_='main-content container')
#                         if content_tag is not None:
#                             content = content_tag.get_text()
#                             f.write('\n\n' + title + '\n')
#                             f.write(content)
#                             print(title, "抓取成功")
#                         else:
#                             print(title, "正文标签未找到，跳过")
#                         time.sleep(1)
#                     except Exception as e:
#                         print(f"【{title}】访问出错，错误信息：{str(e)}")
#         print("爬取完成，已保存至hongloumeng.txt")
#     except Exception as e:
#         print(f"首页访问失败：{str(e)}")







#
#
# import matplotlib.pyplot as plt
# data = [2,3,6,7,11]
# plt.figure()
# plt.plot(data)
# plt.show()

#
# import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# x =[1,2,3,4,5]
# y=[9.7,8.5,7.2,9.1,6.8]
# plt.figure()
# plt.plot(x,y,'bo-')
# plt.xlim(0,6)
# plt.ylim(0,10)
# plt.xticks([1,2,3,4,5],['A','B','C','D','E'])
# plt.xlabel('电影编号')
# plt.ylabel('评分')
# plt.title('电影评分折线图')
# plt.grid()
# plt.show()



# import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# geners = ['剧情','科幻','喜剧','动画']
# counts = [15,8,10,5]
# plt.bar(geners,counts,color=['r','b','g','y'])
# plt.title('各类型电影数量')
# plt.show()

#
# import matplotlib.pyplot as plt
# import numpy as np
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
# genres = ['剧情','科幻','喜剧','动画']
# year2024 = [15, 8, 11, 5]
# year2025 = [12, 11, 9, 7]
# x = np.arange(len(genres))
# width = 0.35
# plt.bar(x - width/2, year2024, width, label='2024年')
# plt.bar(x + width/2, year2025, width, label='2025年')
# plt.xticks(x, genres)
# plt.title('各类型电影数量')
# plt.ylabel('数量')
# plt.legend()
# plt.show()
#
#



# import os
# import time
# import json
# import re
# import matplotlib.pyplot as plt
# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from bs4 import BeautifulSoup
#
#
# URL = "https://baike.baidu.com/item/%E5%B9%B3%E5%87%A1%E7%9A%84%E8%8D%A3%E8%80%80/22358681"
#
# print("正在启动 Edge 浏览器爬取...")
# options = webdriver.EdgeOptions()
# # options.add_argument('--headless')
# options.add_argument('--disable-gpu')
#
# try:
#     driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
#     driver.get(URL)
#     print("浏览器已打开，正在等待页面完全加载（5秒）")
#     time.sleep(5)
#
#     html = driver.page_source
#     driver.quit()
#     print("Edge 浏览器获取源码成功")
#
#     if "百度安全验证" in html or "验证码" in html:
#         print("被百度拦截了，触发安全验证")
#     else:
#         print("正在解析网页内容...")
#         soup = BeautifulSoup(html, features="html.parser")
#
#         ratings = []
#         actors = []
#         plot_text = ""
#
#         summary_div = soup.find(name='div', class_='lemma-summary')
#         if summary_div:
#             plot_text = "\n".join([p.get_text(strip=True) for p in summary_div.find_all(name='div', class_='para')])
#             with open('plot.json', 'w', encoding='utf-8') as f:
#                 json.dump({"plot": plot_text}, f, ensure_ascii=False, indent=2)
#             print("成功保存剧情简介到 plot.json")
#         else:
#             print("未找到剧情简介。")
#
#         tables = soup.find_all('table')
#         print(f"共找到 {len(tables)} 个表格，开始扫描...")
#         pattern = r'\d+\.\d+'
#
#         for table in tables:
#             table_text = table.get_text()
#             if '收视' in table_text or 'CSM' in table_text:
#                 rows = table.find_all('tr')[1:]
#                 for row in rows:
#                     cols = row.find_all(['td', 'th'])
#                     if len(cols) >= 3:
#                         match = re.search(pattern, cols[2].get_text(strip=True))
#                         if match:
#                             ratings.append({
#                                 "date": cols[0].get_text(strip=True),
#                                 "episode": cols[1].get_text(strip=True),
#                                 "rating": float(match.group())
#                             })
#             elif '演员' in table_text or '角色' in table_text:
#                 rows = table.find_all('tr')[1:]
#                 for row in rows:
#                     cols = row.find_all(['td', 'th'])
#                     if len(cols) >= 2:
#                         actors.append({
#                             "name": cols[0].get_text(strip=True),
#                             "role": cols[1].get_text(strip=True)
#                         })
#
#         if ratings:
#             with open('ratings.json', 'w', encoding='utf-8') as f:
#                 json.dump(ratings, f, ensure_ascii=False, indent=2)
#             print(f"成功保存 {len(ratings)} 条收视数据到 ratings.json")
#         else:
#             print("没找到收视情况表格。")
#
#         if actors:
#             with open('actors.json', 'w', encoding='utf-8') as f:
#                 json.dump(actors, f, ensure_ascii=False, indent=2)
#             print(f"成功保存 {len(actors)} 位演员信息到 actors.json")
#         else:
#             print("没找到演员表。")
#
# except Exception as e:
#     print(f"Edge 浏览器启动失败：{e}")
#
# print("\n开始读取 JSON 并生成可视化图表...")
# plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
# plt.rcParams['axes.unicode_minus'] = False
#
# if os.path.exists('ratings.json'):
#     with open('ratings.json', 'r', encoding='utf-8') as f:
#         data = json.load(f)
#     if data:
#         display_data = data[:15]
#         x_data = [item['episode'] for item in display_data]
#         y_data = [item['rating'] for item in display_data]
#
#         plt.figure(figsize=(12, 6))
#         plt.gca().set_facecolor('#f8f9fa')
#         plt.plot(x_data, y_data, marker='o', color='y', linewidth=2.5, markersize=8, label='东方卫视收视率')
#         for i, val in enumerate(y_data):
#             plt.text(i, val + 0.005, f'{val}%', ha='center', va='bottom', fontsize=10)
#
#         plt.title('《平凡的荣耀》真实爬取收视趋势图', fontsize=18, fontweight='bold', pad=20)
#         plt.xlabel('播出集数', fontsize=12)
#         plt.ylabel('收视率（%）', fontsize=12)
#         plt.grid(axis='y', linestyle='--', alpha=0.7)
#         plt.xticks(rotation=45)
#         plt.legend(loc='upper left')
#         plt.tight_layout()
#         plt.show()
#     else:
#         print("爬取到的收视率数据为空，无法画图。")
# else:
#     print("找不到 ratings.json 文件，可视化流程跳过。")


#
# import pandas as pd
# s = pd.Series([9.7,9.6,8.5],index=['电影A','电影B','电影C'])
# print(s)
# df= pd.DataFrame({'title': ['电影A', '电影B', '电影C'], 'rating': [9.7, 9.6, 8.5],'genre':['剧情','科幻','喜剧']})
# print(df)

# import pandas as pd
# # 构建模拟的电影数据集
# data = {
#     'title': ['肖申克的救赎', '霸王别姬', '阿甘正传', '泰坦尼克号', '星际穿越', '盗梦空间'],
#     'year': [1994, 1993, 1994, 1997, 2014, 2010],
#     'rating': [9.7, 9.6, 9.5, 9.4, 9.4, 9.3],
#     'genre': ['剧情', '剧情', '剧情', '爱情', '科幻', '科幻'],
#     'box_office': [28.3, 5.2, 67.8, 218.7, 67.7, 82.9]
# }
#
# # 创建DataFrame，并自定义行索引为电影ID（方便演示loc）
# df = pd.DataFrame(data, index=['M01', 'M02', 'M03', 'M04', 'M05', 'M06'])
# print("=== 原始DataFrame ===")
# print(df)
# #loc 标签索引（基于行/列名称）
# # 1.1 获取单行数据（索引名 M03）
# # print(df.loc['M03'])
#
# # 1.2 获取单列数据（列名 'title'）
# # print(df.loc[:, 'title'])
#
# # # 1.3 获取指定行和列的交点（M03行，rating列）
# # print(df.loc['M03', 'rating'])  # 输出：9.5
#
# # # 1.4 行切片（左闭右闭：包含 M02 和 M04）
# # print(df.loc['M02':'M04'])
# #
# # # 1.5 列切片（左闭右闭：包含 title 到 rating）
# # print(df.loc[:, 'title':'rating'])
#
# # # 1.6 同时切片行和列
# # print(df.loc['M02':'M04', 'title':'rating'])
#
# #iloc 位置索引（基于行/列整数位置）
# # 2.1 获取第1行（索引位置 0）
# # print(df.iloc[0])
# #
# # # 2.2 获取第2列（索引位置 1）
# # print(df.iloc[:, 1])
#
# # # 2.3 获取第1行、第3列的交点（rating列）
# # print(df.iloc[0, 2])  # 输出：9.7
# #
# # # 2.4 行切片（左闭右开：获取位置 1、2、3 的行）
# # print(df.iloc[1:4])
#
# # # 2.5 列切片（左闭右开：获取位置 0、1、2 的列）
# # print(df.iloc[:, 0:3])
# #
# # # 2.6 同时切片行和列
# # print(df.iloc[1:4, 0:3])
#
# #4. 布尔索引（条件筛选）
# # 4.1 单条件筛选：评分大于 9.5 的电影
# print(df[df['rating'] > 9.5])
#
# # 4.2 单条件筛选：类型为科幻
# print(df[df['genre'] == '科幻'])
#
# # 4.3 多条件筛选：评分大于 9.4 且 类型为科幻
# # 注意：每个条件必须用括号括起来，条件之间用 & 连接
# print(df[(df['rating'] > 9.4) & (df['genre'] == '科幻')])
#
# # 4.4 多条件筛选：类型为剧情 或 类型为科幻
# print(df[(df['genre'] == '剧情') | (df['genre'] == '科幻')])
#
# # 4.5 取反筛选：类型不是剧情
# print(df[~(df['genre'] == '剧情')])




#创建一个“脏”数据集
import pandas as pd
import numpy as np

# 构造包含缺失值、重复值的脏数据
data = {
    'title': ['肖申克的救赎', '霸王别姬', '阿甘正传', '泰坦尼克号',
              '星际穿越', '盗梦空间', '肖申克的救赎', np.nan],
    'year': [1994, 1993, 1994, 1997, 2014, 2010, 1994, 2001],
    'rating': [9.7, 9.6, 9.5, np.nan, 9.4, 9.3, 9.7, 9.4],
    'genre': ['剧情', '剧情', '剧情', '爱情', '科幻', '科幻', '剧情', '动画'],
    'box_office': [28.3, 5.2, np.nan, 218.7, 67.7, 82.9, 28.3, 27.5]
}

df = pd.DataFrame(data)
print("=== 原始脏数据 ===")
print(df)
#1. 缺失值处理-识别缺失值
# 判断每个单元格是否为缺失值（返回布尔型DataFrame）
print("=== 缺失值分布（True表示缺失）===")
print(df.isnull())
#
# # 统计每列的缺失数量
# print("\n=== 每列缺失数量 ===")
# print(df.isnull().sum())
# #1.2 填充缺失值（fillna）
# # 方式一：用常数 0 填充票房缺失
# df['box_office'] = df['box_office'].fillna(0)
# print("=== 票房缺失值填为 0 ===")
# print(df['box_office'])
#
# # 方式二：用均值填充评分缺失
# df['rating'] = df['rating'].fillna(df['rating'].mean())
# print("\n=== 评分缺失值填为均值 ===")
# print(df['rating'])
#删除缺失值
# # 方式一：删除任何包含缺失值的行（当前数据中标题仍有缺失）
# df_drop_row = df.dropna(how='any')
# print("=== 删除任何含缺失值的行后 ===")
# print(df_drop_row)
# #方式二：只根据指定列（title）判断并删除缺失行
# df_drop_subset = df.dropna(subset=['title'])
# print("\n=== 仅删除标题缺失的行 ===")
# print(df_drop_subset)
#2. 重复值处理
# # 2.1 识别重复行（判断整行是否完全一样）
# print("=== 判断整行是否重复 ===")
# print(df.duplicated())

# # 2.2 按某一列识别重复（比如 title 相同）
# print("\n=== 判断 title 列是否重复 ===")
# print(df.duplicated(subset=['title']))
# #
# # 2.3 删除完全重复的行（保留第一次出现的）
# df_no_dup = df.drop_duplicates(keep='first')
# print("\n=== 删除完全重复后 ===")
# print(df_no_dup)

# # 2.4 根据 title 去重（保留最后一条）
# df_title_dup = df.drop_duplicates(subset=['title'], keep='last')
# print("\n=== 按 title 去重后（保留最后一条）===")
# print(df_title_dup)

#分组聚合与透视表准备工作：创建测试数据集
import pandas as pd
import numpy as np

# 构造包含类型、年份、评分、票房的电影数据集
data = {
    'title': ['肖申克的救赎', '霸王别姬', '阿甘正传', '泰坦尼克号',
              '星际穿越', '盗梦空间', '千与千寻', '你的名字', '疯狂动物城'],
    'genre': ['剧情', '剧情', '剧情', '爱情', '科幻', '科幻', '动画', '动画', '动画'],
    'year': [1994, 1993, 1994, 1997, 2014, 2010, 2001, 2016, 2016],
    'rating': [9.7, 9.6, 9.5, 9.4, 9.4, 9.3, 9.4, 9.2, 9.2],
    'box_office': [28.3, 5.2, 67.8, 218.7, 67.7, 82.9, 27.5, 27.6, 102.3]
}

df = pd.DataFrame(data)
print("=== 原始数据 ===")
print(df)
# 按类型分组后，提取单列计算平均值
print("=== 各类型电影的平均评分 ===")
print(df.groupby('genre')['rating'].mean())
print("\n=== 哪种类型的电影平均票房最高 ===")
print(df.groupby('genre')['box_office'].mean().idxmax())
# 按类型分组，一次性计算评分的均值、最大值、最小值
print("=== 各类型评分的均值/最大值/最小值 ===")
print(df.groupby('genre')['rating'].agg(['mean', 'max', 'min']))