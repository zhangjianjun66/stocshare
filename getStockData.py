# -*-*coding:utf-8 -*-
import tushare as ts 
import csv,os
import pandas as pd 
import numpy as np
import matplotlib.pylab as plt  
from pandas.tools.plotting import scatter_matrix

class getStockData(object):

	def __int__(self,testInstance):
		self.enable=True
		self.dataBasic={}

	def stockBasic(self,date,fileName):
		t=ts.get_stock_basics(date=date)
		t.to_csv(fileName,encoding='utf_8_sig')
		return t

	def saveCsv(self,result,filename='data.csv'):

		# filename = 'c:/day/bigfile.csv'
		# for code in ['000875', '600848', '000981']:
		# 	df = ts.get_hist_data(code)
		# 	if os.path.exists(filename):
		# 		df.to_csv(filename, mode='a', header=None)
		# 	else:
		# 		df.to_csv(filename)
		if os.path.exists(filename):
			result.to_csv(filename=filename,columns=['open','high','low','close'],mode='a',header=None,encoding='utf_8_sig')
		else:
			result.to_csv(filename=filename, coluluns=['open', 'high', 'low', 'close'],encoding='utf_8_sig')
		return filename

	def query(self,opCode,year=2016,quarter=4):
		queryCmdsByOpCode = {
			'股票列表': ('get_stock_basics', ()),
			'业绩报表':		('get_report_data',(year, quarter)),
			'盈利能力': ('get_profit_data', (year, quarter)),
			'运营能力': ('get_operation_data', (year, quarter)),
			'成长能力': ('get_growth_data', (year, quarter)),
			'偿债能力': ('get_debtpaying_data', (year, quarter)),
			'现金流量': ('get_cashflow_data', (year, quarter)),
		}
		try:
			queryCmds,args = queryCmdsByOpCode[opCode]
			self.result= getattr(ts,queryCmds)(*args)
			# self.dataBasic[opCode]=self.result

			return self.result
		except KeyError:
			print 'cmd fail'

if __name__ =='__main__':
	t=getStockData()
	result=t.query(opCode='业绩报表')
	t.saveCsv(result=result,filename='data.csv')
