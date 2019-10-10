# -*- coding: utf-8 -*-
__author__ = 'cdtaogang'
__date__ = '2019/10/7 9:52'
import allure

class Test_Allure():
    @allure.step(title="第一个测试用例")
    # @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.issue('http://baidu.com', name='点击我跳转百度')
    @allure.testcase("http://www.testweb.com/test_001")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_001(self):
        allure.attach('哈哈', '我是测试步骤001的描述～～～')
        assert 1

    @allure.step(title="第二个测试用例")
    def test_002(self):
        assert 0

    def test_003(self):
        assert 1
        allure.attach.file(r'E:\test_1.jpg', '我是附件截图的名字',attachment_type=allure.attachment_type.JPG)
