import pymongo
import pandas as pd
import numpy as np
client = pymongo.MongoClient('localhost', 27017)
db = client['51job_test']
collection = db['zhiwei_test']
# 读取数据
data = pd.DataFrame(list(collection.find()))
# 选择需要显示的字段
data = data[['pname',"workplace","education","salary","experience"]]
# 打印输出
data1=list(data['education'])
data2=list(data['experience'])
data3=list(data['workplace'])
data4=list(data['salary'])
# data4=np.asarray(data4)
data5=[]
#data4有空值
for data_4 in data4:
    if  data_4 :
        if not (-1 != data_4.find('/')):
            data5.append(data_4)
            pass

        pass
    pass
# print(data5)
count_undergraduate=0
master=0
doctor=0
others=0
college=0
unlimited=0
unrestricted=0
graduate=0
one_year=0
almost_year=0
three_year=0
five_year=0
beijing=0
shanghai=0
guangzhou=0
shenzhen=0
dalian=0
other_city=0
S_under_5k=0
S_5K_10k=0
S_10K_15K=0
S_15K_20K=0
S_20K_25K=0
S_UP25K=0

for data1 in data1:
    if data1=="本科":
        count_undergraduate=count_undergraduate+1
    elif data1=="硕士":
        master=master+1
    elif data1=="博士":
        doctor=doctor+1
    elif data1=="大专":
          college=college+1
    elif data1=="不限":
        unlimited=unlimited+1
    else:
        pass
for data2 in data2:
    if data2=="应届毕业生" or data2=="应届"or data2=="应届生":
        graduate=graduate+1
    elif data2=="不限":
        unrestricted=unrestricted+1
    elif data2=="1年"or data2=="2年"or data2=="1-2年":
        one_year=one_year+1
    elif data2=="3年"or data2=="4年"or data2=="3-4年":
        three_year=three_year+1
    elif data2=="5年"or data2=="6年"or data2=="5-7年":
        five_year=five_year+1
    elif data2=="一年以下":
        almost_year=almost_year+1
    else:
        pass
for data3 in data3:
    if data3=="北京":
        beijing=beijing+1
    elif data3=="上海":
        shanghai=shanghai+1
    elif data3=="广州":
        guangzhou=guangzhou +1
    elif data3=="深圳":
        shenzhen=shenzhen+1
    elif data3=="大连":
        dalian=dalian+1
    else:
        other_city=other_city+1
        pass
    pass

for data5 in data5:
    if float(data5)<0.5:
        S_under_5k=S_under_5k+1
        pass
    elif 0.5<=float(data5)<1:
        S_5K_10k =S_5K_10k+1
        pass
    elif 1<=float(data5)<1.5:
        S_10K_15K=S_10K_15K+1
        pass
    elif 1.5<=float(data5)<2:
        S_15K_20K=S_15K_20K+1
        pass
    elif 2<=float(data5)<2.5:
        S_20K_25K=S_20K_25K+1
        pass
    else:
        S_UP25K=S_UP25K+1
        pass

    pass


# print(count_undergraduate,master,doctor,college,unlimited)
# print(graduate,unrestricted,one_year,three_year,five_year,almost_year)