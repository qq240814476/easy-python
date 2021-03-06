# encoding: utf-8
'''
用于发送链接的类
'''
from config import config
from time import sleep
from splinter.browser import Browser
# traceback模块被用来跟踪异常返回信息
import traceback

config = config()

bwr=Browser(driver_name="chrome")

def clickElement(ele):
    try:
        bwr.element_class.scroll_to(ele)
        ele.click()
    except e:
        print(e)

class api:
    # 设置用户名密码
    def setUserInfo(self):
      self.username = str(input("用户名:"))
      self.passwd = str(input("密码:"))
      print(self.username)
      print(self.passwd)
    
    # 测试browser
    def test(self): 
        bwr.visit(config.sh['whgc']['list'])
        # 时间
        friday = bwr.find_by_xpath('//li[@i_event_id="86249"]')
        satday = bwr.find_by_xpath('//li[@i_event_id="86268"]')
        sunday = bwr.find_by_xpath('//li[@i_event_id="86270"]')

        day = str(input('你想看哪场的：周五、周六、周日（时间自己查）：'))
        if day == '周六':
            day = satday
        # div = bwr.find_by_xpath('//a[@id="unlogin_div"]')
        bwr.element_class.scroll_to(day)
        day.click()
        # 一年阻塞sleep
        sleep(100)
    
    # 测试聚橙
    def testjc(self):
        bwr=Browser(driver_name="chrome")
        bwr.visit(config.jc)
        searchbox = bwr.find_by_id('search_keywords')
        keyWord = str(input('请输入你想搜索的演出（按回车键搜索）：'))
        searchbox.fill(keyWord)
        # 点击搜索
        searchBtn = bwr.find_by_xpath('//div[@class="search-btn icon-search-header"]').first
        clickElement(searchBtn)
        # 爬虫展示list
        
        # sleep
        sleep(1000)
    # 发送登录连接
    def login(self):
      '''
      # 点击当前页面的"登录"
      bwr.find_by_text(u"登录").click()
      sleep(3)
      # fill填充搜索框的内容，username。name=loginUserDTO.user_name的元素。
      bwr.fill("loginUserDTO.user_name", username)
      sleep(1)
      bwr.fill("userDTO.password", passwd)
      sleep(1)
      print(u"等待验证码，自行输入...")
      # 登录手动输入验证码，并登录系统
      while True:
        # 判断当前的url是否已经进入系统
        if bwr.url != initmy_url:
            sleep(1)
        else:
          break
      '''
      print('登录完毕')

    # 购票
    def getTickt(self):
      '''
      global bwr
      # 使用splinter打开chrome浏览器
      bwr=Browser(driver_name="chrome")
      # splinter打开浏览器（返回购票页面）
      bwr.visit(ticket_url)
      while bwr.is_text_present(u"登录"):
          sleep(1)
          login()
          #判断是否已经进入系统
          if bwr.url == initmy_url:
              break
      try:
          print(u"购票页面...")
          # splinter打开浏览器（跳回购票页面）
          bwr.visit(ticket_url)
          # 加载查询信息
          bwr.cookies.add({"_jc_save_fromStation": from_station})
          bwr.cookies.add({"_jc_save_toStation": to_station})
          bwr.cookies.add({"_jc_save_fromDate": from_date})
          bwr.reload()
          sleep(2)
          count=0
          # 循环点击预订
          if order != 0:
              while bwr.url == ticket_url:
                  bwr.find_by_text(u"查询").click()
                  count += 1
                  print(u"循环点击查询... 第 %s 次" % count)
                  sleep(1)
                  try:
                      bwr.find_by_text(u"预订")[order - 1].click()
                  except:
                      print(u"还没开始预订")
                      continue
          else:
              while bwr.url == ticket_url:
                  bwr.find_by_text(u"查询").click()
                  count += 1
                  print(u"循环点击查询... 第 %s 次" % count)
                  sleep(1)
                  try:
                      for i in bwr.find_by_text(u"预订"):
                          i.click()
                          sleep(1)
                  except:
                      print(u"还没开始预订")
                      continue
          sleep(1)
          # 可以通过修改sleep的参数来调整延时, 但延时不要太低, 防止被12306网站认为是刷票屏蔽掉.
          bwr.find_by_text(ticketer)[0].click()
          sleep(1)
          bwr.find_by_text(u"提交订单").click()
          sleep(1)
          #bwr.find_by_id(u"qr_submit_id").click()
          print(u"成功抢到一张宝贵的票")
      except Exception as e:
          print(traceback.print_exc())
      '''
      print('抢票成功')