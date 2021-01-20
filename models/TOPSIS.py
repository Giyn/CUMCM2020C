# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name  : TOPSIS
   Description:
   Author     : Giyn
   date       : 2020/9/13 18:12:39
-------------------------------------------------
   Change Activity:
                   2020/9/13 18:12:39
-------------------------------------------------
"""
__author__ = 'Giyn'

import pandas as pd

from Utils import *


def entropy_weight(features):
    """

    Entropy method

    Args:
        features: Features

    Returns:
        weight: weight coefficient

    """
    features = np.array(features)
    proportion = features / features.sum(axis=0)  # normalized
    entropy = np.nansum(-proportion * np.log(proportion) / np.log(len(features)),
                        axis=0)  # calculate entropy
    weight = (1 - entropy) / (1 - entropy).sum()

    return weight  # calculation weight coefficient


def topsis(data, weight=None):
    """

    TOPSIS algorithm

    Args:
        data: Features
        weight:

    Returns:
        Result:
        Z:
        weight:

    """
    data = data / np.sqrt((data ** 2).sum())  # normalized

    Z = pd.DataFrame([data.min(), data.max()], index=['负理想解', '正理想解'])  # best and worst solution

    weight = entropy_weight(data) if weight is None else np.array(weight)  # distance
    Result = data.copy()
    Result['正理想解'] = np.sqrt(((data - Z.loc['正理想解']) ** 2 * weight).sum(axis=1))
    Result['负理想解'] = np.sqrt(((data - Z.loc['负理想解']) ** 2 * weight).sum(axis=1))

    # composite score index
    Result['综合得分指数'] = Result['负理想解'] / (Result['负理想解'] + Result['正理想解'])
    Result['排序'] = Result.rank(ascending=False)['综合得分指数']

    return Result, Z, weight


"""123"""
df_CH = pd.read_csv('../data/credit_history_enterprise_information.csv')

df_CH = df_CH.iloc[:, [4, 5, 6, 7, 8]]

CH_list = ['E{}.csv'.format(str(codename)) for codename in range(1, 124)]

amount_list_CH = []
for each_enterprise in CH_list:
    df_CH_input = pd.read_csv(
        '../data/credit_history_enterprise_input_invoice/{}'.format(each_enterprise), index_col=0)
    df_CH_output = pd.read_csv(
        '../data/credit_history_enterprise_output_invoice/{}'.format(each_enterprise), index_col=0)
    billing_date = list(df_CH_input['开票日期'].values) + list(df_CH_output['开票日期'].values)
    amount_list_CH.append(
        (sum(df_CH_output['价税合计'].values) - sum(df_CH_input['价税合计'].values)) / count_months(
            billing_date))

features_list = []
for i in range(123):
    features_list.append(df_CH.iloc[i, :].values / amount_list_CH[i])

data = pd.DataFrame(features_list,
                    columns=['作废发票/有效发票', '购方合作密切指数', '销方合作密切指数', '月交易频率', '企业资金链稳定程度'])
raw_score = topsis(data)[0]['综合得分指数'].values.reshape(-1, 1)
for index, i in enumerate(topsis(data)[0]['综合得分指数'].values.reshape(-1, 1)):
    if i == max(topsis(data)[0]['综合得分指数'].values.reshape(-1, 1)):
        raw_score[index] = np.mean(raw_score)
    if i == min(topsis(data)[0]['综合得分指数'].values.reshape(-1, 1)):
        raw_score[index] = np.mean(raw_score)

result = pd.DataFrame(NormMinandMax(raw_score, min=0.8, max=1.2), columns=['企业信赖指数'])

result['企业代号'] = list(map(clean, CH_list))

result.to_csv('credit_hitsoty_corporate_trust_degree.csv', index=False, encoding='utf_8_sig')

"""302"""
df_NCH = pd.read_csv('../data/no_credit_history_enterprise_information.csv')

x = ['购方合作密切指数', '销方合作密切指数', '作废发票/有效发票', '月交易频率', '企业资金链稳定程度']

NCH_list = ['E{}.csv'.format(str(codename)) for codename in range(124, 426)]

amount_list = []
for each_enterprise in NCH_list:
    df_NCH_input = pd.read_csv(
        '../data/no_credit_history_enterprise_input_invoice/{}'.format(each_enterprise),
        index_col=0)
    df_NCH_output = pd.read_csv(
        '../data/no_credit_history_enterprise_output_invoice/{}'.format(each_enterprise),
        index_col=0)
    billing_date = list(df_NCH_input['开票日期'].values) + list(df_NCH_output['开票日期'].values)
    amount_list.append(
        (sum(df_NCH_output['价税合计'].values) - sum(df_NCH_input['价税合计'].values)) / count_months(
            billing_date))

features_list = []
for i in range(302):
    features_list.append(df_NCH[x].iloc[i, :].values / amount_list[i])

data = pd.DataFrame(features_list,
                    columns=['购方合作密切指数', '销方合作密切指数', '作废发票/有效发票', '月交易频率', '企业资金链稳定程度'])

raw_score = topsis(data)[0]['综合得分指数'].values.reshape(-1, 1)

for i, j in enumerate(raw_score):
    if np.isnan(j):
        raw_score[i][0] = 0.85

for index, i in enumerate(topsis(data)[0]['综合得分指数'].values.reshape(-1, 1)):
    if i == max(topsis(data)[0]['综合得分指数'].values.reshape(-1, 1)):
        raw_score[index] = np.mean(raw_score)
    if i == min(topsis(data)[0]['综合得分指数'].values.reshape(-1, 1)):
        raw_score[index] = np.mean(raw_score)

result = pd.DataFrame(NormMinandMax(raw_score, min=0.8, max=1.2), columns=['企业信赖指数'])

result['企业代号'] = list(map(clean, NCH_list))

result.to_csv('no_credit_hitsoty_corporate_trust_degree.csv', index=False, encoding='utf_8_sig')
