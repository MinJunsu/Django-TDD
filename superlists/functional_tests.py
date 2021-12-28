import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), '작업 아이템 입력')

        input_box.send_keys('공작깃털 사기')
        input_box.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: 공작깃털 사기' for row in rows), "신규 작업이 테이블에 표시되지 않는다.")

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
