#import configparser
import os
import json
import datetime

from prodmastdata import Products
import csv
import shutil
import time as tm
from getconfigdata import GetConfigData
from getlogger import GetLoggerObj
from myexceptions import InvalidProdIDException
from myexceptions import InvalidStoreIDException

#https://realpython.com/working-with-files-in-python/
#https://realpython.com/iterate-through-dictionary-python/

class ProcessBills:

    firsttime = True
    mylogger = None
    mypaths = {}

    def read_files(self, frompath):
        from os.path import isfile, join
        onlyfiles = [f for f in os.listdir(frompath) if isfile(join(frompath, f))]
        #print(type(onlyfiles))
        #print(onlyfiles)
        return onlyfiles

    """
    def move_files(self, procfiles, frompath, topath):
        for file_name in procfiles:
            shutil.move(os.path.join(frompath, file_name), topath)
    """

    def process_bill_details(self,bill_details):
        #print(type(bill_details))
        bill_total = 0

        #myproducts = Products.product_data --- locally defined product data
        #---from db
        myproducts = Products().getproductdatafromdb()
        #---calculate line total for each prod id, build bill_details dictionary with line totals
        for key,qty in bill_details.items():
            #print(type(key),key,"->",type(qty),qty)
            #---lookup item from products
            try:
                item = myproducts[int(key)]
                #print(type(item))
                price = item['price']
                #print(key, "->", price, "qty=", qty)
                line_total = qty * price
                #update bill_details with line total
                bill_details[key] = {'prod_id':key, 'qty':qty, 'line_total':line_total}
                bill_total = bill_total + line_total
            except KeyError:
                raise InvalidProdIDException(key)

        return bill_total

    def write_bill_details(self,bill_id, bill_details, csvpath,ctime):
        ProcessBills.mylogger.info(bill_details)
        #add date timestamp to filename**********
        #now = datetime.datetime.now()
        billdetailfname = csvpath + 'bill_details' + ctime.strftime("%Y%m%d%H%M%S") + '.csv'

        try:
            with open(billdetailfname, 'a', newline='') as csvfile:
                fields = ['bill_id', 'prod_id', 'qty', 'line_total']
                detcsvwriter = csv.DictWriter(csvfile, fieldnames=fields)

                if ProcessBills.firsttime is True:
                    #---write header info only if first time writing to file
                    ProcessBills.mylogger.info("Writing to csv file:" + csvfile.__str__())
                    detcsvwriter.writeheader()
                    ProcessBills.firsttime = False

                #---concat bill_id with product detail info and write to detail csv file
                bid = {'bill_id':bill_id}
                for detail in bill_details.values():
                    bid.update(detail)
                    detcsvwriter.writerow(bid)
        except FileNotFoundError as fnf_error:
            ProcessBills.mylogger.error(fnf_error)

    def process_bill_data(self,filelist, ctime):
        #increment file counter
        #add date timestamp to filename*************
        billpath = self.mypaths['bill']
        csvpath = self.mypaths['csv']
        procpath = self.mypaths['proc']
        errpath = self.mypaths['error']
        billdatafname = csvpath +'bill_data'+ ctime.strftime("%Y%m%d%H%M%S") + '.csv'

        try:
            with open(billdatafname, 'w', newline='') as csvfile:
                ProcessBills.firsttime = True
                for fn in filelist:
                    try:
                        full_path = os.path.join(billpath, fn)
                        curfile = open(full_path, 'r')
                        # returns JSON object as
                        # a dictionary
                        bill_data = json.load(curfile)
                        ProcessBills.mylogger.info(bill_data)
                        storeid = bill_data['store_id']
                        if (storeid not in  Products.valid_stores):
                            raise InvalidStoreIDException(storeid)

                        bill_details = bill_data['bill_details']
                        bill_total = self.process_bill_details(bill_details)

                        if ProcessBills.firsttime:#write header fields
                            ProcessBills.mylogger.info("Writing to csv file:" + csvfile.__str__())
                            fields = ['bill_id', 'store_id', 'bill_date', 'bill_total']
                            billcsvwriter = csv.DictWriter(csvfile, fieldnames=fields)
                            billcsvwriter.writeheader()

                        #---write bill data to bill_data csv file
                        bdata = {'bill_id': bill_data['bill_id'], 'store_id': storeid,
                                 'bill_date': bill_data['bill_date'], 'bill_total': bill_total}
                        ProcessBills.mylogger.info(bdata)
                        billcsvwriter.writerow(bdata)
                        # after modified, ie. with results
                        #---write bill details to bill_details csv files
                        self.write_bill_details(bill_data['bill_id'], bill_details, csvpath, ctime)
                        #---close file and move to processed directory
                        curfile.close()
                        shutil.move(full_path, procpath)
                    except InvalidProdIDException as pe:
                        #---close file and move to error directory
                        ProcessBills.mylogger.error(pe.prodId + ":" + pe.message)
                        curfile.close()
                        shutil.move(full_path, errpath)
                    except InvalidStoreIDException as se:
                        #---close file and move to error directory
                        ProcessBills.mylogger.error(str(se.storeId) + ":" + se.message)
                        curfile.close()
                        shutil.move(full_path, errpath)
                    except FileNotFoundError as fnf_error:
                        ProcessBills.mylogger.error(fnf_error)
        except FileNotFoundError as fnf_error:
            ProcessBills.mylogger.error(fnf_error)

if __name__ == "__main__":
    # eventually read this path from console*****
    config_file_path = "C:\\Users\\rvish\\sudha\\BillingSystem\\config\\config_data.ini"
    loggerObj = None
    ProcessBills.mypaths = GetConfigData.get_config_data(config_file_path)
    #exception - if not json file*******

    # use __file__ create unique log file for bill_processor
    logfname = ProcessBills.mypaths['log'] + __file__.split('.')[0]

    my_processor = ProcessBills()
    while True:
        files_to_proc_list = my_processor.read_files(ProcessBills.mypaths['bill'])

        if files_to_proc_list:#---if there are files to process, ie. list exists
            # ---get create new log file each time we read list of files from directory
            now = datetime.datetime.now()
            #---each time through loop, get new logger
            if loggerObj:
                del loggerObj

            loggerObj = GetLoggerObj()
            ProcessBills.mylogger = loggerObj.get_logger(logfname, now)
            ProcessBills.mylogger.info("Process following files:" + str(files_to_proc_list))
            #my_processor.process_bill_data(files_to_proc_list, mypaths['bill'], mypaths['csv'],now,ProcessBills.mylogger)
            #my_processor.process_bill_data(files_to_proc_list, mypaths['bill'], mypaths['csv'], now)
            my_processor.process_bill_data(files_to_proc_list, now)
        else:
            tm.sleep(20)