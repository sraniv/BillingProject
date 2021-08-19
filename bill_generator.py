import random
import datetime
#import os
import time
import json
#import configparser
#import Faker
from getlogger import GetLoggerObj

from getconfigdata import GetConfigData

#Issues installing
"""
https://www.geeksforgeeks.org/python-convert-dictionary-object-into-string/
https://stackoverflow.com/questions/11875770/how-to-overcome-datetime-datetime-not-json-serializable
"""

class Generate:

    mylogger = None

    """
    Generate random data with and convert to string using json.dumps()
    """
    def generate_bills(self, l_target_path):

        l_store_id = random.randint(1, 5)
        now = datetime.datetime.now()
        l_bill_id = now.strftime("%Y%m%d%H%M%S")

        #Generate Random Date
        start_date = datetime.date(2000, 1, 1)
        end_date = datetime.date(2020, 1, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        l_date = start_date + datetime.timedelta(days=random_number_of_days)
        l_date_str = l_date.__str__()
        l_bill_details = {}

        #---Generate random length bill details
        for i in range(random.randint(1, 25)):
            l_prod_id = random.randint(0, 30)
            l_qty = random.randint(1, 20)
            l_bill_details[l_prod_id] = l_qty

        l_data = {"bill_id":l_bill_id
                  ,"store_id":l_store_id
                  ,"bill_date":l_date_str
                  ,"bill_details":l_bill_details}
        data_str = json.dumps(l_data)
        Generate.mylogger.info(data_str)

        jsonfname = l_target_path + l_bill_id + ".json"
        newjson_file = open(jsonfname, "w")
        newjson_file.write(data_str)
        newjson_file.close()

if __name__ == "__main__":
    #---read this path from console****************
    config_file_path = "C:\\Users\\rvish\\sudha\\BillingSystem\\config\\config_data.ini"

    #---directory where bills should be generated to
    #target_path = "C:\\Users\\rvish\\sudha\\BillingSystem\\bills\\"
    #----read tartget_path from config file using configparser ****
    mypaths = GetConfigData.get_config_data(config_file_path)

    #---use __file__ create unique log file for bill_generator
    #?---value returned by __file__ is different when run in command prompt versus pycharm*********?
    print("__file__ =" ,__file__)
    logfname = mypaths['log'] + __file__.split('.')[0]

    loggerObj = GetLoggerObj()
    #---get logger object that will rotate files at midnight
    Generate.mylogger = loggerObj.get_timerotatelogger(logfname)

    #get Generate object
    my_generator = Generate()
    while True:
        my_generator.generate_bills(mypaths['bill'])
        # break
        time.sleep(2)
