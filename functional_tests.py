from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        # 암묵적 대기 추가
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 웹 사이트 확인
        self.browser.get('http://localhost:8000')

        # 타이틀과 헤더가 To-do를 표시하고 있는지 확인
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
