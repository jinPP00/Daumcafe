from selenium import webdriver
import time
import chromedriver_autoinstaller # 터미널 창에 pip install chromedriver_autoinstaller 입력하여 모듈 설치!

# chromedriver_autoinstaller 를 사용하여 코드를 아래처럼 작성하면,
# 굳이 chromedriver 파일을 별도로 다운로드 받지 않아도 됩니다.
# browser = webdriver.Chrome("./chromedriver") # 삭제
chrome_path = chromedriver_autoinstaller.install() # 추가
browser = webdriver.Chrome(chrome_path) # 추가
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F")
id = browser.find_element_by_css_selector("#id")
id.send_keys("talingpython")
pw = browser.find_element_by_css_selector("#inputPwd")
pw.send_keys("q1w2e3!@#")
browser.find_element_by_css_selector("#loginBtn").click()
time.sleep(3)
browser.get("http://cafe.daum.net/talingpython")
time.sleep(3)
# 가입인사 게시판 클릭
browser.switch_to.frame(browser.find_element_by_css_selector("#down")) # 프레임 전환
browser.find_element_by_css_selector("#fldlink_lF1R_309").click()
time.sleep(3)
# 글쓰기 버튼 클릭
browser.find_element_by_css_selector("#article-write-btn").click()
time.sleep(5)
# 제목 작성
subject = browser.find_element_by_css_selector(".title__input")
subject.send_keys("안녕하세요!")
# 본문 작성
browser.switch_to.frame(browser.find_element_by_css_selector("#keditorContainer_ifr")) # 프레임 전환
content = browser.find_element_by_css_selector("#tinymce")
content.send_keys("반갑습니다.")
# 발행 버튼 클릭
browser.switch_to.default_content() # 제일 바깥으로 빠져나옴.
browser.switch_to.frame(browser.find_element_by_css_selector("#down")) # 프레임 전환
browser.find_element_by_css_selector("button.btn_g.full_type1").click()
time.sleep(3)
browser.close()
