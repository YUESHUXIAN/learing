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




