from tkinter import *
import pyautogui as pag
from selenium import webdriver
from tkinter import ttk

selenium = webdriver
root = Tk()

class GUI():

    def __init__(self):
        self.l1 = Label(root, text='Create Tibia Accounts Automatic')
        self.l2 = Label(root, text='Account')
        self.l3 = Label(root, text='Password')
        self.l4 = Label(root, text='Quantity')
        self.ent1 = Entry(root)
        self.ent2 = Entry(root)
        self.ent3 = Entry(root, width=5)
        self.btn = Button(root, text='Create Accounts', command=self.callSelenium)
        #self.txt = Text(root, width=10, height=10)
        self.l5 = Label(root, text='World')
        self.combo = ttk.Combobox(root, values=['teste1', 'teste2'])
        
    """
        Variables Config
    """

    def _show(self):
        self.l1.grid(row=1, column=2)
        self.l2.grid(row=2)
        self.ent1.grid(row=2, column=2)
        self.l3.grid(row=3)
        self.ent2.grid(row=3, column=2)
        self.l4.grid(row=4)
        self.ent3.grid(row=4, column=2)
        self.btn.grid(row=6, column=2)
        self.l5.grid(row=5)
        self.combo.grid(row=5, column=2)

        
    def callSelenium(self): #
        open = selenium.Chrome()
        qty = int(self.ent3.get())
                                ###Selenium Variables###
        self.url = 'https://secure.tibia.com/account/?subtopic=createaccount'
                                
        if isinstance(qty, int) and qty != 0:
            for i in range(qty):
                open.get(self.url)
                                ###Selenium Variables###
                self.accountElements = {
                    'account':open.find_element_by_xpath('//*[@id="accountname"]'),
                    'password':open.find_element_by_xpath('//*[@id="password1"]'),
                    'email':open.find_element_by_xpath('//*[@id="email"]'),
                    'password2':open.find_element_by_xpath('//*[@id="password2"]'),
                    'SuggestName':open.find_element_by_xpath('//*[@id="CreateAccountAndCharacterForm"]/div/table/tbody/tr/td/div/table/tbody/tr[2]/td/div[2]/div/table/tbody/tr[1]/td[2]/small/a')
                }
                                ###Selenium Actions###
                self.accountElements['account'].send_keys(self.ent1.get()+str(i))
                self.accountElements['password'].send_keys(self.ent2.get()+str(i))
                self.accountElements['password2'].send_keys(self.ent2.get()+str(i))
                self.accountElements['email'].send_keys(self.ent1.get()+str(i)+'@mozej.com')
                self.accountElements['SuggestName'].click()

start = GUI()
start._show()
mainloop()