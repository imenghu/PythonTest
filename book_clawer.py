"""
这是一个爬取某小说网站的py程序。
网站地址:http://www.biquw.com/book/94/

# 程序设计的步骤的步骤
#   1  拿到小说章节的超链接
#   2  拿到a标签中的连接之后先去做url拼接,组成完整的小说内容，再通过requests.get() 拿到具体的内容页中的内容的所有的数据
#   3   在内容页中使用bs4 提取小说中的内容
#   4  把我们提取的数据存到文本文件中
"""
# 导入网络请求包
import requests
# 网页选择器 pip install bs4 解析html代码并且从代码中获取我们想要的数据。
from bs4 import BeautifulSoup
# lxml是一个HTML/XML的解析器，主要的功能是如何解析和提取HTML/XML数据。
import lxml

def main():

    # 获取网页上的所有的数据
    response = requests.get('http://www.biquw.com/book/94/').text

    # 所有数据的基础上筛选数据,有两个参数第一个参数是要筛选的网页，第二个值是html解析器lxml
    soup = BeautifulSoup(response, 'lxml')

    soup_list = soup.find("ul")
    # 因为在ulb标签中有许多li标签，li标签中包含了a标签在a标签中有我们想要的超链接
    for book in soup_list.find_all('a'):
        # print('{}:{}'.format(book.text,'http://www.biquw.com/book/700/' + book['href']))
        book_url = 'http://www.biquw.com/book/94/' + book['href']
        data_book = requests.get(book_url, 'lxml').text
        soup = BeautifulSoup(data_book, 'lxml')
        data = soup.find('div', {'id': 'htmlContent'}).text

        # 将文本写入txt文件中
        with open(book.text + '.txt', 'w', encoding='utf-8') as f:
            f.write(data)


if __name__ == '__main__':
    print("开始下载。。。")
    main()
    print("下载完成")
