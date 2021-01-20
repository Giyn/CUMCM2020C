# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name  : data_preprocessing
   Description:
   Author     : Giyn
   date       : 2020/9/10 19:01:42
-------------------------------------------------
   Change Activity:
                   2020/9/10 19:01:42
-------------------------------------------------
"""
__author__ = 'Giyn'

import pandas as pd

CHII_filepath = '../data/credit_history_input_invoice.csv'
CHOI_filepath = '../data/credit_history_output_invoice.csv'
NCHII_filepath = '../data/no_credit_history_input_invoice.csv'
NCHOI_filepath = '../data/no_credit_history_output_invoice.csv'

df_NCHOI = pd.read_csv(NCHOI_filepath)
df_NCHII = pd.read_csv(NCHII_filepath)
df_CHOI = pd.read_csv(CHOI_filepath)
df_CHII = pd.read_csv(CHII_filepath)

for codename in range(1, 124):
    df_CHII[df_CHII['企业代号'] == 'E{}'.format(str(codename))].to_csv(
        '../data/credit_history_enterprise_input_invoice/E{''}.csv'.format(str(codename)),
        encoding='utf_8_sig')

for codename in range(1, 124):
    df_CHOI[df_CHOI['企业代号'] == 'E{}'.format(str(codename))].to_csv(
        '../data/credit_history_enterprise_output_invoice/E{''}.csv'.format(str(codename)),
        encoding='utf_8_sig')

for codename in range(124, 426):
    df_NCHII[df_NCHII['企业代号'] == 'E{}'.format(str(codename))].to_csv(
        '../data/no_credit_history_enterprise_input_invoice/E{}.csv'.format(str(codename)),
        encoding='utf_8_sig')

for codename in range(124, 426):
    df_NCHOI[df_NCHOI['企业代号'] == 'E{}'.format(str(codename))].to_csv(
        '../data/no_credit_history_enterprise_output_invoice/E{}.csv'.format(str(codename)),
        encoding='utf_8_sig')
