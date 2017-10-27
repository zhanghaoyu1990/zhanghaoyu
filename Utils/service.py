# -*- coding: utf-8 -*-
from Excel import ReadAndWriteExcel
import json


class Services:
    def __init__(self):
        self.file_path = None
        self.sheet_name = None
        self.replace_params = None
        self.inject_data = None

    @property
    def file_path(self):
        return self.file_path

    @file_path.setter
    def file_path(self, file_path):
        self.file_path = file_path

    @property
    def sheet_name(self):
        return self.sheet_name

    @sheet_name.setter
    def sheet_name(self, sheet_name):
        self.sheet_name = sheet_name

    @property
    def replace_params(self):
        return self.replace_param

    @replace_params.setter
    def replace_params(self, replace_params):
        self.replace_params = replace_params

    def replace_param(self, file_path, sheet_name, replace_params, inject_data):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.replace_params = replace_params
        self.inject_data = inject_data
        excel = ReadAndWriteExcel()
        excel.set_excel_path(self.file_path)
        replace_data = excel.get_cell_by_col_index_row_index(self.sheet_name, 3, 8)
        replace_data = json.loads(replace_data)
        param_list = replace_params.split('|')
        for param in param_list:
            replace_data['requestData'][param] = inject_data['responseData'][param]
        return replace_data

inject_data = """
{
  "responseCode": "000000",
  "responseMessage": "成功",
  "responseData": {
    "actualPayAmount": "1000.00",
    "orderAmount": 1000,
    "orderCreateTime": "2017-04-14 13:54:35",
    "orderNo": "20170414020708961",
    "orderStatus": "1",
    "payOrderNo": "2017041401994496"
  }
}
"""

inject_data = json.loads(inject_data)

print inject_data
services = Services()
print services.replace_param('D:\\zhy\\auto.xls', u'订单详情', 'orderNo', inject_data)