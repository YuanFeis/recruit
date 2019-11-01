from flask import Flask,render_template,request,g
from datetime import datetime
app = Flask(__name__)
import read_data
from wordcloud import WordCloud
import jieba
import pandas as pd

def makewordcloud():
    data = pd.DataFrame(list(read_data.collection.find()))
    #data[['pname']] 提取df 数据
    #FutureWarning: The signature of `Series.to_csv` was aligned to that of `DataFrame.to_csv`,
    #and argument 'header' will
    #change its default value from False to True:
    #please pass an explicit value to suppress this warning.
    data_pname = data[['pname']]
    data_requirement = data[['requirement']]
    data_workplace=data[['workplace']]
    data_nature = data[['nature']]
    # pandas 保存txt去除空格
    data_pname.to_csv('static/wordcloud_pname.txt', header=None, index=False, sep=" ")
    file_pname = open('static/wordcloud_pname.txt', 'r', 1, encoding='utf8').read()
    mytext_pname = " ".join(jieba.cut(file_pname))
    wordcloud = WordCloud(font_path='static/SimSun.ttf', background_color="white",     width=1000, height=860, margin=2).generate(
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
@app.route('/',methods=["POST","GET"])
def hello_world():
    if request.method == 'POST':
        zhiweis = request.form.get("zhiwei")
        zw = read_data.collection.find({"pname": {'$regex': zhiweis}})
        # print('seratcsdasdasdasdas')
        g.zw = zw
        return render_template("search.html")
    else:
        return render_template("index.html")
@app.route('/ciyun/',methods=["POST","GET"])
def ciyun():
    if request.method == 'POST':
        zhiweis = request.form.get("zhiwei")
        zw = read_data.collection.find({"pname": {'$regex': zhiweis}})
        g.zw = zw
        return render_template("search.html")
    else:

        return render_template("ciyun.html")
@app.route('/educate/',methods=["POST","GET"])
def education():
    if request.method=='POST':
       zhiweis=request.form.get("zhiwei")
       zw=read_data.collection.find({"pname":{'$regex': zhiweis}})
       g.zw=zw
       return render_template("search.html")
    else:
        g.master=read_data.master
        g.doctor=read_data.doctor
        g.undergraduate=read_data.count_undergraduate
        g.others=read_data.others
        g.unlimited=read_data.unlimited
        g.college=read_data.college
        g.time=datetime.now()
        return render_template("education.html")
@app.route("/experience/",methods=["POST","GET"])
def work_experience():
    if request.method=='POST':
       zhiweis=request.form.get("zhiwei")
       zw=read_data.collection.find({"pname":{'$regex': zhiweis}})
       g.zw=zw
       return render_template("search.html")
    else:
        g.unrestricted=read_data.unrestricted
        g.one_year=read_data.one_year
        g.three_year=read_data.three_year
        g.five_year=read_data.five_year
        return render_template("experience.html")

@app.route("/workplace/",methods=["POST","GET"])
def work_place():
    if request.method == 'POST':
        zhiweis = request.form.get("zhiwei")
        zw = read_data.collection.find({"pname": {'$regex': zhiweis}})
        g.zw = zw
        return render_template("search.html")
    else:
        g.beijing = read_data.beijing
        g.shanghai = read_data.shanghai
        g.guangzhou = read_data.guangzhou
        g.shenzhen = read_data.shenzhen
        g.dalian = read_data.dalian
        g.other_city = read_data.other_city
        g.time = datetime.now()
        return render_template("workplace.html")

@app.route("/salary/",methods=["POST","GET"])
def work_salary():
    if request.method == 'POST':
        zhiweis = request.form.get("zhiwei")
        zw = read_data.collection.find({"pname": {'$regex': zhiweis}})
        g.zw = zw
        return render_template("search.html")
    else:
        g.S_under_5k = read_data.S_under_5k
        g.S_5K_10k = read_data.S_5K_10k
        g.S_10K_15K = read_data.S_10K_15K
        g.S_15K_20K = read_data.S_15K_20K
        g.S_20K_25K = read_data.S_20K_25K
        g.S_UP25K = read_data.S_UP25K
        g.time = datetime.now()
        return render_template("salary.html")
if __name__ == '__main__':
    # debug = True 二次启动不生成词云文件，数据量太大，
    # 生成词云的函数要 加载很多数据，导致启动太缓慢
    #如果事先没有词云图片，默认启动需要3分半
    #不生成词云要10s
    # makewordcloud()
    app.run()
