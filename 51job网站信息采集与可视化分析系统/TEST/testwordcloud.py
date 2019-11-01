from wordcloud import WordCloud
import jieba

f = open('test.txt','r',1,encoding='utf8').read()
mytext = " ".join(jieba.cut(f))
wordcloud = WordCloud(font_path='SimSun.ttf',background_color="white",width=1000, height=860, margin=2).generate(mytext)
wordcloud.to_file('test.png')


