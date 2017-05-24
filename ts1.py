# -*- coding:utf-8 -*-
import tushare as ts
import  csv
import pandas as pd
import numy as np
import matplotlib.pyplot as plt

class stock(object):
# print tushare.__version__
# df=ts.get_hist_data()
    def __int__(self):
        
    def basicinfo(self):
        """
        code,代码
        name,名称
        industry,所属行业
        area,地区
        pe,市盈率
        outstanding,流通股本(亿)
        totals,总股本(亿)
        totalAssets,总资产(万)
        liquidAssets,流动资产
        fixedAssets,固定资产
        reserved,公积金
        reservedPerShare,每股公积金
        esp,每股收益
        bvps,每股净资
        pb,市净率
        timeToMarket,上市日期
        undp,未分利润
        perundp, 每股未分配
        rev,收入同比(%)
        profit,利润同比(%)
        gpr,毛利率(%)
        npr,净利润率(%)
        holders,股东人数
        """
        bs = ts.get_stock_basics()
        file_name='txt.csv'
        bs.to_csv(file_name, encoding='utf_8_sig')
        # csvfile.write(codecs.BOM_UTF8)
        # print  bs
    def financeReport(self):
        """
        code,代码
        name,名称
        esp,每股收益
        eps_yoy,每股收益同比(%)
        bvps,每股净资产
        roe,净资产收益率(%)
        epcf,每股现金流量(元)
        net_profits,净利润(万元)
        profits_yoy,净利润同比(%)
        distrib,分配方案
        report_date,发布日期
        :return:
        """
        year=[2010]#,2012,2013,2014,2015,2016]
        quater=[1,2,3,4]
        for y in year:
            for q in quater:
                rs=ts.get_report_data(y,q)
                rs.to_csv(str(y)+'_'+str(q)+'.csv',encoding='utf_8_sig')
    def pic(self):
        plt.show()
        
if __name__ ==  "__main__":
    t=stock()
    t.financeReport()
    # basicinfo()
