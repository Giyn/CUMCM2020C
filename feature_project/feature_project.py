# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name  : feature_project
   Description:
   Author     : Giyn
   date       : 2020/9/13 18:05:52
-------------------------------------------------
   Change Activity:
                   2020/9/13 18:05:52
-------------------------------------------------
"""
__author__ = 'Giyn'

import pandas as pd
from sklearn import preprocessing

from Utils import *

CH_list = ['E{}.csv'.format(str(codename)) for codename in range(1, 124)]

"""企业合作稳定指数"""
stability_degree_list = []
for each_enterprise in CH_list:
    df_input = pd.read_csv(
        '../data/credit_history_enterprise_input_invoice/{}'.format(each_enterprise), index_col=0)
    stable_partner_times = list(df_input['销方单位代号'].value_counts())[0]
    billing_date = list(df_input['开票日期'].values)
    stability_degree = stable_partner_times / count_months(billing_date)
    stability_degree_list.append(round(stability_degree, 4))

min_max_scaler = preprocessing.MinMaxScaler()
stability_degree_array = min_max_scaler.fit_transform(
    np.array(stability_degree_list).reshape(-1, 1))

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['销方合作密切指数'] = stability_degree_array

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

stability_degree_list = []
for each_enterprise in CH_list:
    df_output = pd.read_csv(
        '../data/credit_history_enterprise_output_invoice/{}'.format(each_enterprise), index_col=0)
    stable_partner_times = list(df_output['购方单位代号'].value_counts())[0]
    billing_date = list(df_output['开票日期'].values)
    stability_degree = stable_partner_times / count_months(billing_date)
    stability_degree_list.append(round(stability_degree, 4))

min_max_scaler = preprocessing.MinMaxScaler()
stability_degree_array = min_max_scaler.fit_transform(
    np.array(stability_degree_list).reshape(-1, 1))

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['购方合作密切指数'] = stability_degree_array

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

"""金额"""
input_amount_list = []
for each_enterprise in CH_list:
    df_input = pd.read_csv(
        '../data/credit_history_enterprise_input_invoice/{}'.format(each_enterprise), index_col=0)
    input_amount_list.append(sum(df_input['金额'].values))

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['进项金额'] = input_amount_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

output_amount_list = []
for each_enterprise in CH_list:
    df_output = pd.read_csv(
        '../data/credit_history_enterprise_output_invoice/{}'.format(each_enterprise), index_col=0)
    output_amount_list.append(sum(df_output['金额'].values))

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['销项金额'] = output_amount_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

"""价税合计"""
input_amount_and_tax_list = []
for each_enterprise in CH_list:
    df_input = pd.read_csv(
        '../data/credit_history_enterprise_input_invoice/{}'.format(each_enterprise), index_col=0)
    input_amount_and_tax_list.append(sum(df_input['价税合计'].values))

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['进项价税合计'] = input_amount_and_tax_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

output_amount_and_tax_list = []
for each_enterprise in CH_list:
    df_output = pd.read_csv(
        '../data/credit_history_enterprise_output_invoice/{}'.format(each_enterprise), index_col=0)
    output_amount_and_tax_list.append(sum(df_output['价税合计'].values))

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['销项价税合计'] = output_amount_and_tax_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

"""平均金额"""
input_average_amount_list = []
for each_enterprise in CH_list:
    df_input = pd.read_csv(
        '../data/credit_history_enterprise_input_invoice/{}'.format(each_enterprise), index_col=0)
    input_average_amount_list.append(np.mean(df_input['金额'].values))

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['进项平均金额'] = input_average_amount_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

output_average_amount_list = []
for each_enterprise in CH_list:
    df_output = pd.read_csv(
        '../data/credit_history_enterprise_output_invoice/{}'.format(each_enterprise), index_col=0)
    output_average_amount_list.append(np.mean(df_output['金额'].values))

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['销项平均金额'] = output_average_amount_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

"""平均税额"""
input_average_tax_list = []
for each_enterprise in CH_list:
    df_input = pd.read_csv(
        '../data/credit_history_enterprise_input_invoice/{}'.format(each_enterprise), index_col=0)
    input_average_tax_list.append(np.mean(df_input['税额'].values))

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['进项平均税额'] = input_average_tax_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

output_average_tax_list = []
for each_enterprise in CH_list:
    df_output = pd.read_csv(
        '../data/credit_history_enterprise_output_invoice/{}'.format(each_enterprise), index_col=0)
    output_average_tax_list.append(np.mean(df_output['税额'].values))

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['销项平均税额'] = output_average_tax_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

"""金额中位数"""
input_median_amount_list = []
for each_enterprise in CH_list:
    df_input = pd.read_csv(
        '../data/credit_history_enterprise_input_invoice/{}'.format(each_enterprise), index_col=0)
    input_median_amount_list.append(np.median(df_input['金额'].values))

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['进项金额中位数'] = input_median_amount_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

output_median_amount_list = []
for each_enterprise in CH_list:
    df_output = pd.read_csv(
        '../data/credit_history_enterprise_output_invoice/{}'.format(each_enterprise), index_col=0)
    output_median_amount_list.append(np.median(df_output['金额'].values))

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['销项金额中位数'] = output_median_amount_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

"""税额中位数"""
input_median_tax_list = []
for each_enterprise in CH_list:
    df_input = pd.read_csv(
        '../data/credit_history_enterprise_input_invoice/{}'.format(each_enterprise), index_col=0)
    input_median_tax_list.append(np.median(df_input['税额'].values))

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['进项税额中位数'] = input_median_tax_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

output_median_tax_list = []
for each_enterprise in CH_list:
    df_output = pd.read_csv(
        '../data/credit_history_enterprise_output_invoice/{}'.format(each_enterprise), index_col=0)
    output_median_tax_list.append(np.median(df_output['税额'].values))

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['销项税额中位数'] = output_median_tax_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

"""税额"""
input_tax_list = []
for each_enterprise in CH_list:
    df_input = pd.read_csv(
        '../data/credit_history_enterprise_input_invoice/{}'.format(each_enterprise), index_col=0)
    input_tax_list.append(sum(df_input['税额'].values))

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['进项税额'] = input_tax_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

output_tax_list = []
for each_enterprise in CH_list:
    df_output = pd.read_csv(
        '../data/credit_history_enterprise_output_invoice/{}'.format(each_enterprise), index_col=0)
    output_tax_list.append(sum(df_output['税额'].values))

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['销项税额'] = output_tax_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

"""作废发票数"""
invalid_input_invoices_amount_list = []
for each_enterprise in CH_list:
    df_input = pd.read_csv(
        '../data/credit_history_enterprise_input_invoice/{}'.format(each_enterprise), index_col=0)
    invalid_input_invoices_amount_list.append(
        df_input[df_input['发票状态'].str.contains('作废发票')].shape[0])

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['作废进项发票数'] = invalid_input_invoices_amount_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

invalid_output_invoices_amount_list = []
for each_enterprise in CH_list:
    df_output = pd.read_csv(
        '../data/credit_history_enterprise_output_invoice/{}'.format(each_enterprise), index_col=0)
    invalid_output_invoices_amount_list.append(
        df_output[df_output['发票状态'].str.contains('作废发票')].shape[0])

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['作废销项发票数'] = invalid_output_invoices_amount_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

"""有效发票数"""
valid_input_invoices_amount_list = []
for each_enterprise in CH_list:
    df_input = pd.read_csv(
        '../data/credit_history_enterprise_input_invoice/{}'.format(each_enterprise), index_col=0)
    valid_input_invoices_amount_list.append(
        df_input[df_input['发票状态'].str.contains('有效发票')].shape[0])

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['有效进项发票数'] = valid_input_invoices_amount_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

valid_output_invoices_amount_list = []
for each_enterprise in CH_list:
    df_output = pd.read_csv(
        '../data/credit_history_enterprise_output_invoice/{}'.format(each_enterprise), index_col=0)
    valid_output_invoices_amount_list.append(
        df_output[df_output['发票状态'].str.contains('有效发票')].shape[0])

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['有效销项发票数'] = valid_output_invoices_amount_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

"""月交易频率"""
monthly_trading_fre_list = []
for each_enterprise in CH_list:
    df_input = pd.read_csv(
        '../data/credit_history_enterprise_input_invoice/{}'.format(each_enterprise), index_col=0)
    df_output = pd.read_csv(
        '../data/credit_history_enterprise_output_invoice/{}'.format(each_enterprise), index_col=0)
    in_valid_invoice = df_input[df_input['发票状态'].str.contains('有效发票')].shape[0]
    out_valid_invoice = df_output[df_output['发票状态'].str.contains('有效发票')].shape[0]
    billing_date_in = list(df_input['开票日期'].values)
    billing_date_out = list(df_output['开票日期'].values)
    billing_date = billing_date_in + billing_date_out
    monthly_trading_fre = round(
        ((in_valid_invoice + out_valid_invoice) / count_months(billing_date)), 4)
    monthly_trading_fre_list.append(monthly_trading_fre)

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['月交易频率'] = monthly_trading_fre_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

"""作废/有效发票比值"""
ratio_of_void_and_valid_invoice = []
for each_enterprise in CH_list:
    df_input = pd.read_csv(
        '../data/credit_history_enterprise_input_invoice/{}'.format(each_enterprise), index_col=0)
    df_output = pd.read_csv(
        '../data/credit_history_enterprise_output_invoice/{}'.format(each_enterprise), index_col=0)
    in_void_invoice = df_input[df_input['发票状态'].str.contains('作废发票')].shape[0]
    out_void_invoice = df_output[df_output['发票状态'].str.contains('作废发票')].shape[0]
    in_valid_invoice = df_input[df_input['发票状态'].str.contains('有效发票')].shape[0]
    out_valid_invoice = df_output[df_output['发票状态'].str.contains('有效发票')].shape[0]
    ratio_of_void_and_valid_invoice.append(
        round((in_void_invoice + out_void_invoice) / (in_valid_invoice + out_valid_invoice), 4))

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['作废发票/有效发票'] = ratio_of_void_and_valid_invoice

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

"""企业资金链稳定程度"""
enterprise_profit_variance = []
for each_enterprise in CH_list:
    each_enterprise_total_profit = []
    df_input = pd.read_csv(
        '../data/credit_history_enterprise_input_invoice/{}'.format(each_enterprise), index_col=0)
    df_output = pd.read_csv(
        '../data/credit_history_enterprise_output_invoice/{}'.format(each_enterprise), index_col=0)
    raw_in_date_list = list(set(df_input['开票日期'].values))
    raw_out_date_list = list(set(df_output['开票日期'].values))
    in_date_list = list(map(change_date, raw_in_date_list))
    out_date_list = list(map(change_date, raw_out_date_list))
    YM_in_date_list = split_months(in_date_list)
    YM_out_date_list = split_months(out_date_list)
    raw_in_months_list = list(set(YM_in_date_list))
    raw_out_months_list = list(set(YM_out_date_list))
    in_months_list = sorted(raw_in_months_list, key=lambda date: sort_date(date))
    out_months_list = sorted(raw_out_months_list, key=lambda date: sort_date(date))
    final_in_months_list = list(map(recover_date, in_months_list))
    final_out_months_list = list(map(recover_date, out_months_list))

    for each_month in final_in_months_list:
        if len(df_input[df_input['开票日期'].str.contains(each_month)]['价税合计'].values) < 10:
            pass
        else:
            each_enterprise_total_profit.append(
                sum(df_input[df_input['开票日期'].str.contains(each_month)]['价税合计'].values))

    for each_month in final_out_months_list:
        each_enterprise_total_profit.append(
            sum(df_output[df_output['开票日期'].str.contains(each_month)]['价税合计'].values))

    enterprise_profit_variance.append(np.var(each_enterprise_total_profit))

min_max_scaler = preprocessing.MinMaxScaler()
enterprise_profit_variance = min_max_scaler.fit_transform(
    np.array(enterprise_profit_variance).reshape(-1, 1))

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['企业资金链稳定程度'] = enterprise_profit_variance

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')

"""总发票数"""
invoices_amount_list = []
for each_enterprise in CH_list:
    df_input = pd.read_csv(
        '../data/credit_history_enterprise_input_invoice/{}'.format(each_enterprise), index_col=0)
    df_output = pd.read_csv(
        '../data/credit_history_enterprise_output_invoice/{}'.format(each_enterprise), index_col=0)
    invoices_amount_list.append(df_input['发票状态'].shape[0] + df_output['发票状态'].shape[0])

df_CH_enterprise = pd.read_csv('../data/credit_history_enterprise_information.csv')
df_CH_enterprise['总发票数'] = invoices_amount_list

df_CH_enterprise.to_csv('../data/credit_history_enterprise_information.csv', index=False,
                        encoding='utf_8_sig')
