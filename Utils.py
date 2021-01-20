# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name  : Utils
   Description:
   Author     : Giyn
   date       : 2020/9/13 18:07:45
-------------------------------------------------
   Change Activity:
                   2020/9/13 18:07:45
-------------------------------------------------
"""
__author__ = 'Giyn'

import datetime
import re

import numpy as np


def count_months(bill_date_list):
    count_list = []
    for bill_date in bill_date_list:
        count_list.append(re.findall(r'^\d{4}.\d{1,2}', bill_date)[0])

    return len(list(set(count_list)))


def get_log(profit):
    return np.log10(profit)


def change_date(date):
    return date.replace('/', '-')


def recover_date(date):
    return date.replace('-', '/')


def sort_date(date):
    return datetime.datetime.strptime(date, "%Y-%m").timestamp()


def split_months(date_list):
    YM_date_list = []
    for date in date_list:
        YM_date_list.append(re.findall(r'^\d{4}.\d{1,2}', date)[0])

    return YM_date_list


def NormMinandMax(npdarr, min=0, max=1):
    arr = npdarr.flatten()
    Ymax = np.max(arr)  # calculate the maximum
    Ymin = np.min(arr)  # calculate the minimum
    k = (max - min) / (Ymax - Ymin)
    last = min + k * (arr - Ymin)

    return last


def clean(string):
    return string.replace('.csv', '')
