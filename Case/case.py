# -*- coding: utf-8 -*-
from Excel import ReadAndWriteExcel
import os
from jinja2 import Environment, FileSystemLoader
PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)


class Case:
    def __init__(self):
        self.case_id = None
        self.response_code = None
        self.response_message = None
        self.expected = None
        self.result = None
        self.case_type = None
        self.is_run = None
        self.request_data = None
        self.interface = None
        self.sheet_name = None
        self.case_des = None
        self.case_method = None

    @property
    def case_id(self):
        return self.case_id

    @case_id.setter
    def case_id(self, case_id):
        self.case_id = case_id

    @property
    def response_code(self):
        return self.response_code

    @response_code.setter
    def response_code(self, response_code):
        self.response_code = response_code

    @property
    def response_message(self):
        return self.response_message

    @response_message.setter
    def response_message(self, response_message):
        self.response_message = response_message

    @property
    def expected(self):
        return self.expected

    @expected.setter
    def expected(self, expected):
        self.expected = expected

    @property
    def result(self):
        return self.result

    @result.setter
    def result(self, result):
        self.result = result

    @property
    def case_type(self):
        return self.case_type

    @case_type.setter
    def case_type(self, case_type):
        self.case_type = case_type

    @property
    def is_run(self):
        return self.is_run

    @is_run.setter
    def is_run(self, is_run):
        self.is_run = is_run

    @property
    def request_data(self):
        return self.request_data

    @request_data.setter
    def request_data(self, request_data):
        self.request_data = request_data

    @property
    def interface(self):
        return self.interface

    @interface.setter
    def interface(self, interface):
        self.interface = interface

    @property
    def sheet_name(self):
        return self.sheet_name

    @sheet_name.setter
    def sheet_name(self, sheet_name):
        self.sheet_name = sheet_name

    @property
    def case_des(self):
        return self.case_des

    @case_des.setter
    def case_des(self, case_des):
        self.case_des = case_des

    @property
    def case_method(self):
        return self.case_method

    @case_method.setter
    def case_method(self, case_method):
        self.case_method = case_method

case_list = []


def init_data(file_path):
    global case_list
    excel = ReadAndWriteExcel()
    excel.set_excel_path(file_path)
    sheets = excel.get_all_sheet()
    for sheet in sheets:
        case_row_nums = excel.get_rowcount_by_sheet_name(sheet)-2
        cases = []
        for row in range(case_row_nums):
            case = Case()
            case.sheet_name = sheet
            case.case_id = row + 1
            case.case_type = excel.get_cell_by_col_index_row_index(sheet, row+2, 6)
            case.expected = excel.get_cell_by_col_index_row_index(sheet, row+2, 3)
            case.interface = excel.get_cell_by_col_index_row_index(sheet, 0, 1)
            case.is_run = excel.get_cell_by_col_index_row_index(sheet, row+2, 7)
            case.request_data = excel.get_cell_by_col_index_row_index(sheet, row+2, 8).replace('\n', '').replace(' ', '')
            case.case_des = excel.get_cell_by_col_index_row_index(sheet, row+2, 5)
            case.case_method = excel.get_cell_by_col_index_row_index(sheet, row+2, 9)
            cases.append(case)
        case_list.append({'sheet': sheet, 'cases': cases})


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def generate_case():
    fname = '../paic/testsuite.txt'
    with open(fname, 'w') as f:
        case_lists = {'case_list': case_list}
        testsuite = render_template('testsuite.txt', case_lists)
        print testsuite
        f.write(testsuite.encode('utf-8'))


init_data('D:\\zhy\\auto.xls')
# print case_list[0]['cases'][0].request_data
# print case_list
generate_case()


