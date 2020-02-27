import ddt
import unittest
import HTMLTestRunnerNew
from practical_01.tools.my_test import my_test_case
class TestProcess:
    def do_login_test(self):

        suite=unittest.TestSuite()
        loader=unittest.TestLoader()
        suite.addTest(loader.loadTestsFromModule(my_test_case))
        with open(r"F:\workspace_02\unittest_practical\practical_01\test_result\test_report.html","wb+") as file:

            runner=HTMLTestRunnerNew.HTMLTestRunner(file,
                                                    verbosity=2,
                                                    title="接口自动化测试",
                                                    description="zhengxiaozhong第一次接口自动化测试",
                                                    tester="zhengxiaozhong")
            runner.run(suite)

if __name__ == '__main__':
     TestProcess().do_login_test()