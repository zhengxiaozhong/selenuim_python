import configparser
from practical_01.data_package.file_path_package import GetFilePath

class ConfigProcess:
    def get_excel_path(self):
        cp=configparser.ConfigParser()
        cp.read(GetFilePath().get_case_config_file_path(),encoding="utf-8")
        excel_file=cp.get("SELECT","excel_file")
        return excel_file

    def get_case_config(self):
        cp = configparser.ConfigParser()
        cp.read(GetFilePath().get_case_config_file_path(), encoding="utf-8")
        case_select=eval(cp.get("SELECT","case_select"))
        return case_select

# if __name__ == '__main__':
#     print(ConfigProcess().get_case_config())