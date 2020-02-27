import pandas as pd
from practical_01.data_package.file_path_package import GetFilePath
from practical_01.tools.config_process.do_config import ConfigProcess

class ExcelProcess:
    def read_excel(self):
        case_config=ConfigProcess().get_case_config()
        data = []
        for item in case_config:
            df = pd.read_excel(GetFilePath().get_test_data_file_path(), item)
            indexs = df.index.values
            for i in indexs:
                res = df.ix[i].to_dict()
                if(case_config[item]=="all"):
                    data.append(res)
                elif(res["case_id"] in case_config[item]):
                    data.append(res)
        return data
    #
    # def write_back(self,file,sheet):
    #     df = pd.DataFrame([1,2,3,4])
    #
    #     writer=pd.ExcelWriter(file)
    #     df.to_excel(writer,sheet_name=sheet)
    #     writer.save()



# if __name__ == '__main__':
#     data=ExcelProcess().read_excel()
#     print(len(data))