#!/usr/bin/python
# -*- coding: cp1250  -*-
__author__ = 'Fekete András Demeter'


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class mail_:
    def email(self,username,password,to_txt,cc_txt,bcc_txt,sbj_txt,body_txt,attach):
            dcap = dict(DesiredCapabilities.PHANTOMJS)
            dcap["phantomjs.page.settings.userAgent"] = ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')
            mydriver = webdriver.PhantomJS(desired_capabilities=dcap,service_args=['--ssl-protocol=any','--ignore-ssl-errors=true'])
            mydriver.set_window_size(1024, 1500) #
            baseurl = "https:// -- your host -- /owa/?ae=Item&t=IPM.Note&a=New"
            xpaths = { 'usernameTxtBox' : ".//*[@id='username']",
                   'passwordTxtBox' : ".//*[@id='password']",
                   'submitButton' : ".//*[@id='tblMid']/tbody/tr[7]/td/table/tbody/tr[3]/td/input[1]",
                   'submitButton2' : ".//*[@id='lnkHdrnewmsg']",
                   'TxtBoxtxtto' : ".//*[@id='txtto']",
                   'TxtBoxtxtcc' : ".//*[@id='txtcc']",
                   'TxtBoxtxtbcc' : ".//*[@id='txtbcc']",
                   'TxtBoxsubject' : ".//*[@id='txtsbj']",
                   'TxtBoxbody' : ".//*[@id='frm']/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[1]/textarea",
                   'TxtBoxSOS' : ".//*[@id='lnkHdrimphigh']/img",
                   'TxtBoxsend' : ".//*[@id='lnkHdrsend']",
                   'attachment' : ".//*[@id='frm']/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[10]/td[1]/a",
                   'attachment2' : ".//*[@id='attach']",
                   'attachment2attach' : ".//*[@id='attachbtn']",
                   'attachment_done' : ".//*[@id='lnkHdrdone']"
                                    }
            mydriver.get(baseurl)

            Wait=WebDriverWait(mydriver, 60)
            Wait.until(EC.element_to_be_clickable((By.ID,'tblMid')))
            mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)
            mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)
            mydriver.find_element_by_xpath(".//*[@id='rdoPblc']").click()
            mydriver.find_element_by_xpath(".//*[@id='tblMid']/tbody/tr[7]/td/table/tbody/tr[3]/td/input[1]").click()
            mydriver.find_element_by_xpath(xpaths['TxtBoxtxtto']).send_keys(to_txt)
            mydriver.find_element_by_xpath(xpaths['TxtBoxtxtcc']).send_keys(cc_txt)
            mydriver.find_element_by_xpath(xpaths['TxtBoxtxtbcc']).send_keys(bcc_txt)
            mydriver.find_element_by_xpath(xpaths['TxtBoxsubject']).send_keys(sbj_txt)
            mydriver.find_element_by_xpath(xpaths['TxtBoxbody']).send_keys(body_txt)
            mydriver.find_element_by_xpath(xpaths['TxtBoxSOS']).click()
            if attach=='':
                pass
            else:
                mydriver.find_element_by_xpath(xpaths['attachment']).click()
                mydriver.find_element_by_xpath(xpaths['attachment2']).send_keys(attach)
                mydriver.find_element_by_xpath(xpaths['attachment2attach']).click()
                mydriver.find_element_by_xpath(xpaths['attachment_done']).click()
            mydriver.find_element_by_xpath(xpaths['TxtBoxsend']).click()
            mydriver.quit()

if __name__ == "__main__":

    username = 'domain\\username'
    password = ''
    to_txt = ''
    cc_txt = ''
    bcc_txt = ''
    sbj_txt = ''
    body_txt = ''
    attach = 'fullpath!'

send = mail_
send.email(username,password,to_txt,cc_txt,bcc_txt,sbj_txt,body_txt,attach)
