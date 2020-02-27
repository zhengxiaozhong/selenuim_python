import unittest
from ddt import data,ddt
from practical_01.tools.excel_process import do_excel_pandas
from practical_01.tools.excel_process import do_excel_openpyxl
from practical_01.tools.request_process.do_request import HttpRequest
from practical_01.data_package.cookie_package import LoginCookie

test_data = do_excel_pandas.ExcelProcess().read_excel()
@ddt
class MyTestCase(unittest.TestCase):

    def setUp(self) :
        pass
    @data(*test_data)
    def test_api(self,test_data):
        if (getattr(LoginCookie, "cookie") == None):
            setattr(LoginCookie, "cookie", HttpRequest().get_login_cookie())
        res = HttpRequest().request_api(test_data["method"], test_data["url"], eval(test_data["data"]),cookie=getattr(LoginCookie, "cookie"))
        try:
            result = "pass"
            self.assertEqual(test_data["expect"],res.text)
        except AssertionError as e:
            result = "faild"
            raise e
        finally:
            do_excel_openpyxl.ExcelProcess().write_back(test_data["sheet"], test_data["case_id"] + 1,test_result=res.text, result=result)

# if __name__ == '__main__':
#     unittest.main()