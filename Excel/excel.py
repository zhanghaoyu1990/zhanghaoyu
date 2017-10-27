# -*- coding: utf8 -*-

from os.path import join
from xlrd import open_workbook
from xlutils.copy import copy
import os, sys
import json


class ReadAndWriteExcel:
    def __init__(self):
        self.file_path = None
        self.sheetName = None
        self.rb = None

    def set_excel_path(self, file_path):
        self.file_path = file_path
        self.rb = open_workbook(self.file_path, 'r+b')

    # 写数据
    def write_excel(self, sheet_name, row_index, line_index, content):
        rbook = open_workbook(self.file_path, 'w')
        wb = copy(rbook)
        sheet_index = rbook.sheet_names().index(sheet_name)
        wb.get_sheet(int(sheet_index)).write(int(row_index), int(line_index), content)
        wb.save(self.file_path)
        print 'write file ok'

    # 获取所有的sheet
    def get_all_sheet(self):
        return [x.name for x in self.rb.sheets()]

    # 获取某一行数据
    def get_row_index_data_by_sheet_name(self, sheet_name, row_index):
        return self.rb.sheet_by_name(sheet_name).row_values(int(row_index))

    # 获取某一列数据
    def get_col_index_data_by_sheet_name(self, sheet_name, col_index):
        return self.rb.sheet_by_name(sheet_name).col_values(int(col_index))

    # 获取总行数
    def get_rowcount_by_sheet_name(self, sheet_name):
        return int(self.rb.sheet_by_name(sheet_name).nrows)

    # 获取总列数
    def get_col_umn_count_by_sheet_name(self, sheet_name):
        return int(self.rb.sheet_by_name(sheet_name).ncols)

    # 获取某个单元格的值
    def get_cell_by_col_index_row_index(self, sheet_name, row_index, col_index):
        return self.rb.sheet_by_name(sheet_name).cell_value(int(row_index), int(col_index))


def test():
    excel = ReadAndWriteExcel()
    excel.set_excel_path('D:\\zhy\\auto.xls')
    # a = excel.get_cell_by_col_index_row_index(u'订单受理', 3, 8)
    sheets = excel.get_all_sheet()
    for sheet in sheets:
        print sheet
    print type(sheets)

test()
