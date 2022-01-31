import sys

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(StaticLiveServerTestCase):
    DEBUG = False

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        # 암묵적 대기 추가
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    @classmethod
    def setUpClass(cls):
        if not cls.DEBUG:
            cls.server_url = 'http://sunsuking.kro.kr/'
            return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 웹 사이트 확인
        self.browser.get(self.server_url)

        # 타이틀과 헤더가 To-do를 표시하고 있는지 확인
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('작업 목록', header_text)

        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), '작업 아이템 입력')

        input_box.send_keys('공작깃털 사기')
        input_box.send_keys(Keys.ENTER)

        import time
        time.sleep(1)

        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/')

        self.check_for_row_in_list_table('1: 공작깃털 사기')

        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('공작깃털을 이용해서 그물 만들기')
        input_box.send_keys(Keys.ENTER)

        import time
        time.sleep(1)

        self.check_for_row_in_list_table('2: 공작깃털을 이용해서 그물 만들기')
        self.check_for_row_in_list_table('1: 공작깃털 사기')

        self.browser.quit()
        self.browser = webdriver.Firefox()

        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('공작깃털 사기', page_text)
        self.assertNotIn('그물 만들기', page_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('우유 사기')
        inputbox.send_keys(Keys.ENTER)

        import time
        time.sleep(1)

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/')
        self.assertNotEqual(francis_list_url, edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('공작깃털 사기', page_text)
        self.assertIn('우유 사기', page_text)

    def test_layout_and_styling(self):
        # 에디스는 메인 페이지를 방문한다.
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # 그녀는 입력 상자가 가운데 배치된 것을 본다
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        # 그녀는 새로운 리스트를 시작하고 입력상자가 가운데 배치된 것을 확인한다.
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )
