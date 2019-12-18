# 导入必要的工具包
import jieba
import wordcloud

# 1 以文本的方式读取数据
with open('会议纪要.txt','rt',encoding ='utf-8') as fi:
    s2 = fi.read()
    s2 = s2.replace('\n', '').replace('。', '').replace('，', '').replace('、', '')

# 2自动分词成列表
ls = jieba.lcut(s2)

# 3将列表拼接成字串 
s2 = ' '.join(ls)

# 4 显示打印一下字符串
print(s2)

# 5 指定字体和分词的 数据源
wordcloud = wordcloud.WordCloud(font_path= 'SIMLI.TTF', background_color="white",width=1000, height=860, margin=2,max_words= 35).generate(s2)
# 6 生成图片
wordcloud.to_file('test.png')
