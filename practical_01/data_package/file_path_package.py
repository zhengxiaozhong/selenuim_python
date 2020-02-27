import os
class GetFilePath:
    path = os.path.realpath(__file__)
    top_path = os.path.split(os.path.split(path)[0])[0]

    def get_test_data_file_path(self):
        test_data_path=os.path.join(self.top_path,"test_data","test_data.xlsx")
        print(test_data_path)
        return test_data_path

    def get_case_config_file_path(self):
        case_config_file_path=os.path.join(self.top_path,"conf","test_case.config")
        print(case_config_file_path)
        return case_config_file_path


# if __name__ == '__main__':
#     GetFilePath().get_test_data_file_path()
#     GetFilePath().get_case_config_file_path()