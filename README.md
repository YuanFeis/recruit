# recruit
大三软件实训项目

#      51job网站信息采集与可视化分析系统
### 职位可视化分析

1. 爬虫：
    采用Scrapy 分布式爬虫技术，使用mongodb作为数据存储，爬取的网站Demo为智联招聘-51job，
2. 数据处理：
     采用pandas对爬取的数据进行清晰和处理
3. 数据分析：
    采用flask后端获取mongodb数据，前端使用bootstrap3.echarts以及Wordcloud的词云图

### 安装所需环境 
- pymango
- scrapy
- flask
- wordcloud
- echarts
- mangodb




### 关于项目启动


1. 爬虫：
   
   1. cd 目录
   2. scrapy crawl zlzp
2. 数据可视化
   1. 第一次使用运行 python make_wordcloud.py
   2. python zlzpView.py
