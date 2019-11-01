from wordcloud import WordCloud
import jieba
import pandas as pd
import read_data

if __name__ == '__main__':
    data = pd.DataFrame(list(read_data.collection.find()))
    # data[['pname']] 提取df 数据
    # FutureWarning: The signature of `Series.to_csv` was aligned to that of `DataFrame.to_csv`,
    # and argument 'header' will
    # change its default value from False to True:
    # please pass an explicit value to suppress this warning.
    data_pname = data[['pname']]
    data_requirement = data[['requirement']]
    data_workplace = data[['workplace']]
    data_nature = data[['nature']]

    # pandas 保存txt去除空格
    data_pname.to_csv('static/wordcloud_pname.txt', header=None, index=False, sep=" ")
    file_pname = open('static/wordcloud_pname.txt', 'r', 1, encoding='utf8').read()
    mytext_pname = " ".join(jieba.cut(file_pname))
    wordcloud = WordCloud(font_path='static/SimSun.ttf', background_color="white", width=1000, height=860,
                          margin=2).generate(
        mytext_pname)
    wordcloud.to_file('static/img/wordcloud_pname.png')

    # pandas 保存txt去除空格
    data_requirement.to_csv('static/wordcloud_requirement.txt', header=None, index=False, sep=" ")
    file_requirement = open('static/wordcloud_requirement.txt', 'r', 1, encoding='utf8').read()
    mytext_requirement = " ".join(jieba.cut(file_requirement))
    wordcloud = WordCloud(font_path='static/SimSun.ttf', background_color="white", width=1000, height=860,
                          margin=2).generate(mytext_requirement)
    wordcloud.to_file('static/img/wordcloud_requirement.png')

    # pandas 保存txt去除空格
    data_workplace.to_csv('static/wordcloud_workplace.txt', header=None, index=False, sep=" ")
    file_workplace = open('static/wordcloud_workplace.txt', 'r', 1, encoding='utf8').read()
    mytext_workplace = " ".join(jieba.cut(file_workplace))
    wordcloud = WordCloud(font_path='static/SimSun.ttf', background_color="white", width=1000, height=860,
                          margin=2).generate(mytext_workplace)
    wordcloud.to_file('static/img/wordcloud_workplace.png')

    # pandas 保存txt去除空格
    data_nature.to_csv('static/wordcloud_nature.txt', header=None, index=False, sep=" ")
    file_nature = open('static/wordcloud_nature.txt', 'r', 1, encoding='utf8').read()
    mytext_nature = " ".join(jieba.cut(file_nature))
    wordcloud = WordCloud(font_path='static/SimSun.ttf', background_color="white", width=1000, height=860,
                          margin=2).generate(mytext_nature)
    wordcloud.to_file('static/img/wordcloud_nature.png')
    pass

