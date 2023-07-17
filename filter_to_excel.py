#!/usr/bin/python3.6

import os
import re
import json
import xlwt
from xlwt import Workbook
from dotenv import load_dotenv

load_dotenv()

# Workbook is created
wb = Workbook()

# library modules
from jira import JIRA

# Authentication and Variables
user = os.getenv("SCRIPT_USER")
apikey = os.getenv("SCRIPT_PASS")
server = os.getenv("SCRIPT_SRVR")

jira_filter = os.getenv("FILTER")
excel_path = os.getenv("EXCEL_PATH")
excel_file = os.getenv("EXCEL_FILE")

# example pic.fields.customfield_99999
custom_field = os.getenv("ustomfield_13204")


options = {
    'server': server
}

jira = JIRA(options, basic_auth=(user,apikey) )

sheet = wb.add_sheet('Jira')

count = 0
for i in jira.search_issues('filter='+jira_filter):
    result = []
    epic = jira.issue(i)
    description = epic.fields.description

    ## Testing
    # fields_dict = epic.raw['fields']
    # for field_name, field_value in fields_dict.items():
    #     print(f'{field_name}: {field_value}')


    booking_date = custom_field
    ## Testing
    # print(epic.fields.summary)
    # print("Booking Date: "+booking_date)


    result = [epic, booking_date]

    jql_query = f'parentEpic="{epic.key}"'

    child_issues = jira.search_issues(jql_query)

    # for issue in child_issues:
    #     if (issue.key != epic.key):
            # result[i] = issue.fields.summary
            # print(" - "+issue.fields.summary)

    sheet.write(0, 0, 'test')

wb.save(excel_path+'/'excel_file)


