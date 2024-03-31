import requests
from lxml import etree
import xlwt
from collections import defaultdict
import matplotlib.pyplot as plt
headers={
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0"
}
data_total=[]

def get_dangdang_info(i,url):
    html=requests.get(url,headers=headers)
    html.encoding = html.apparent_encoding  # 将乱码进行编码
    selector=etree.HTML(html.text)
    datas=selector.xpath('//div[@class="bang_list_box"]')

    for data in datas:
        Ranks = data.xpath('ul/li/div[1]/text()')
        names = data.xpath('ul/li/div[3]/a/text()')
        pingluns = data.xpath('ul/li/div[4]/a/text()')
        authors = data.xpath('ul/li/div[5]/a/text()')
        chubans = data.xpath('ul/li/div[6]/span/text()')
        jiages = data.xpath('ul/li/div[7]/p[1]/span[1]/text()')
        yuanjias = data.xpath('ul/li/div[7]/p[1]/span[2]/text()')
        discounts = data.xpath('ul/li/div[7]/p[1]/span[3]/text()')
    # urls = data.xpath('ul/li/div[3]/a/@href')
    for Rank,name,pinglun,author,chuban,jiage,yuanjia,discount in zip(Ranks,names,pingluns,authors,chubans,jiages,yuanjias,discounts):
     # print(Rank,name,pinglun,author,chuban,jiage,yuanjia,discount)
            dflist = []
            dflist.append(i)
            dflist.append(Rank)
            dflist.append(name)
            dflist.append(pinglun)
            dflist.append(author)
            dflist.append(chuban)
            dflist.append(jiage)
            dflist.append(yuanjia)
            dflist.append(discount)
            data_total.append(dflist)

def list_save():
    head = ['year','Rank','name', 'pinglun','author','chuban','jiage','yuanjia','discount']  # 定义表头
    book = xlwt.Workbook(encoding='utf-8')  # 创建工作簿
    sheet_name = book.add_sheet('当当网畅销榜TOP500书籍信息')  # 创建工作表
    # 写入表头数据
    for h in range(len(head)):
        sheet_name.write(0, h, head[h])
    row = 1
    data_len = len(data_total)
    for i in range(data_len):
        for j in range(len(head)):
            sheet_name.write(row, j, data_total[i][j])
        row += 1
    book.save('当当网畅销榜TOP500书籍信息.xls')
def filter_books_by_author(data, author_name):
    """
    筛选特定作者的书籍信息
    :param data: 所有书籍信息的列表
    :param author_name: 想要筛选的作者名
    :return: 筛选后的书籍信息列表
    """
    filtered_data = [record for record in data if author_name in record[4]]
    return filtered_data

def prepare_plot_data(filtered_data):
    """
    准备绘图数据
    :param filtered_data: 筛选后的书籍信息列表
    :return: 用于绘图的数据结构
    """
    plot_data = defaultdict(list)
    for record in filtered_data:
        year, title = record[0], record[2]
        try:
            rank = int(record[1])
        except ValueError:
            rank = int(float(record[1]))
        plot_data[title].append((year, rank))
    for title in plot_data:
        plot_data[title].sort(key=lambda x: x[0])
    return plot_data

def plot_book_rankings(plot_data):
    """
    根据准备好的数据绘制图表
    :param plot_data: 用于绘图的数据结构
    """
    plt.figure(figsize=(10, 6))
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 例如使用微软雅黑
    plt.rcParams['axes.unicode_minus'] = False
    for title, year_rank_pairs in plot_data.items():
        years, ranks = zip(*year_rank_pairs)
        plt.plot(years, ranks, marker='o', label=title)
    years = range(2020, 2023)
    plt.xticks(years, [str(year) for year in years])
    plt.title('Rankings Over Years for Selected Author')
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.gca().invert_yaxis()  # 排名越低越好
    plt.legend()
    plt.show()

if __name__=='__main__':
    for i in range(2020,2023):
        for j in range(1,25):
            url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-{ii}-0-1-{jj}'.format(ii=i,jj=j)
            get_dangdang_info(i,url)
    list_save()
    author_name = "罗伯特·戴博德"
    filtered_data = filter_books_by_author(data_total, author_name)
    plot_data = prepare_plot_data(filtered_data)
    plot_book_rankings(plot_data)
    print("程序运行结束")