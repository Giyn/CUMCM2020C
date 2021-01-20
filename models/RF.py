import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

data1 = pd.read_csv('credit_history_enterprise_information.csv')
data2 = pd.read_csv('credit_history_input_invoice.csv')
data3 = pd.read_csv('credit_history_output_invoice.csv')

data1['信誉评级'].replace(['A', 'B', 'C', 'D'], [4.0, 3.0, 2.0, 1.0], inplace=True)
data1['是否违约'].replace(['是', '否'], [1, 0], inplace=True)
data2['parse_time'] = pd.to_datetime(data2['开票日期'], format='%Y/%m/%d')
data3['parse_time'] = pd.to_datetime(data3['开票日期'], format='%Y/%m/%d')

suming = data2.groupby(['企业代号']).sum()['金额']
suming = data3.groupby(['企业代号']).sum()['金额']

data2['year'] = data2['parse_time'].dt.year
data2.groupby(['企业代号', 'year']).mean()
data3['year'] = data3['parse_time'].dt.year
data3.groupby(['企业代号']).count().sort_values(by='year', ascending=False)

enterprise_interest = []

for i in data1['企业代号'].unique():
    temp = [i]
    enterprise_data2 = data2[data2['企业代号'] == i]
    enterprise_data3 = data3[data3['企业代号'] == i]
    normalization = enterprise_data2['金额'].sum() - enterprise_data3['金额'].sum()

    for j in [2016, 2017, 2018, 2019, 2020]:
        mths = len(enterprise_data2[enterprise_data2['year'] == j]['parse_time'].dt.month.unique())
        meaning = enterprise_data2[enterprise_data2['year'] == j]['金额'].sum() - \
                  enterprise_data3[enterprise_data3['year'] == j]['金额'].sum()

        if mths: meaning /= mths

        meaning = 0 if meaning is np.nan else meaning
        temp.append(meaning)

    scale = np.mean(np.abs(np.array(temp[1:]))[np.array(temp[1:]) != 0.0])

    temp.append(np.log10(np.mean(scale)))
    temp.append(data1[data1['企业代号'] == i]['购方合作密切指数'].sum() / normalization)
    temp.append(data1[data1['企业代号'] == i]['销方合作密切指数'].sum() / normalization)
    temp.append(data1[data1['企业代号'] == i]['作废发票/有效发票'].sum())
    temp.append(data1[data1['企业代号'] == i]['月交易频率'].sum() / normalization)
    temp.append(data1[data1['企业代号'] == i]['企业资金链稳定程度'].sum())
    temp.append(data1[data1['企业代号'] == i]['进项金额'].sum() / normalization)
    temp.append(data1[data1['企业代号'] == i]['销项金额'].sum() / normalization)
    temp.append(data1[data1['企业代号'] == i]['进项税额'].sum() / normalization)
    temp.append(data1[data1['企业代号'] == i]['销项税额'].sum() / normalization)
    temp.append(data1[data1['企业代号'] == i]['进项价税合计'].sum() / normalization)
    temp.append(data1[data1['企业代号'] == i]['有效进项发票数'].sum() / normalization)
    temp.append(data1[data1['企业代号'] == i]['有效销项发票数'].sum() / normalization)
    temp.append(data1[data1['企业代号'] == i]['作废进项发票数'].sum() / normalization)

    enterprise_interest.append(np.array(temp))

enterprise_interest_gain = []

for i in enterprise_interest:
    temp = []

    for j in range(2, 6):
        if float(i[j - 1]) == 0:
            temp.append(0.0)
            continue
        temp.append(float(i[j]) / float(i[j - 1]))

    for k in range(6, len(i)):
        temp.append(float(i[k]))

    enterprise_interest_gain.append(temp)

enterprise_interest_gain = np.array(enterprise_interest_gain)

for i in range(0, len(enterprise_interest_gain[0])):
    enterprise_interest_gain[:, i][enterprise_interest_gain[:, i] == 0.0] = np.median(
        enterprise_interest_gain[:, i][enterprise_interest_gain[:, i] != 0.0])

train_feat = []

feat_name = ['2017-Gain', '2018-Gain', '2019-Gain', '2020-Gain', 'Scale',
             'Corporation Index(Input)',
             'Corporation Index(Output)', 'Invoice Index',
             'Trade Frequency(per month)', 'Corporateion Financial Stability', 'Input', 'Output',
             'Tax rate(Input)',
             'Tax rate(Output)', 'Tax(Input)', 'Vaild invoice(Input)', 'Vaild invoice(Output)',
             'Invaild invoice']

for i in range(0, len(np.array(enterprise_interest)[:, 0])):
    temp = np.zeros(shape=len(feat_name) + 1)

    temp[:len(feat_name)] = enterprise_interest_gain[i]

    temp[-1] = data1[data1['企业代号'] == np.array(enterprise_interest)[i, 0]]['信誉评级'].iloc[0]

    train_feat.append(np.array(temp))

train_feat = np.array(train_feat)

cart = RandomForestRegressor(min_samples_leaf=5)

cart.fit(train_feat[0:-1], train_feat[:, -1].astype(np.float32))

data1['信誉等级-回归'] = cart.predict(train_feat[0:-1])

data1.to_csv('credit_history_enterprise_information_regression.csv', index=False, encoding='gbk')
