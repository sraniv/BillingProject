import configparser

class GetConfigData:
    @staticmethod
    def get_config_data(configpath):
        my_config = configparser.ConfigParser()
        my_config.read(configpath)
        base_path = my_config['General']['base_path']
        #directory where bill should be read from
        pathdict = {}
        pathdict['bill'] = base_path + my_config['BillGenerator']['bill_target_path']
        pathdict['proc'] = base_path + my_config['BillProcessor']['proc_target_path']
        pathdict['error'] = base_path + my_config['BillProcessor']['error_target_path']
        pathdict['csv'] = base_path + my_config['BillProcessor']['csv_target_path']
        pathdict['log'] = base_path + my_config['Logging']['log_path']
        return pathdict