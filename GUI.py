from tkinter import *
from tkinter import ttk
import pyautogui as pag
from selenium import webdriver

selenium = webdriver
root = Tk()

class GUI():

    def __init__(self):
                                    ###Words List### From web scraping with bs4
        self.comboList = {
            'NonPvp': ['Belobra', 'Beneva', 'Calmera', 'Candia', 'Celesta', 'Damora', 'Descubra', 'Fidera', 'Gentebra', 'Guardia','Astera','Harmonia','Honera','Kalibra',
            'Luminera','Magera','Menera','Nerana','Olera','Olympa','Pacera','Refugia','Secura','Tavara','Unitera','Veludera'],
            'OpenPvp': ['Amera','Antica','Estela','Ferobra','Fotera','Garnera',
            'Honbra','Impera','Inabra','Julera','Justera','Kenora','Laudera','Noctera','Peloria','Premia','Quelibra','Quintera','Serdebra','Shivera','Silvera','Solera','Thera',
            'Umera','Vita','Vunira','Xantera','Zanera'],
            'RetroPvp': ['Chrona','Duna','Eldera','Lutabra','Morta','Mortera','Relembra','Helera','Macabra','Tortura'],
            'Preview': ['Zuna','Zunera']
        }
        self.comboList['NonPvp'].sort()
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
        #self.combo = ttk.Combobox(root, values=['Non Pvp', 'Open Pvp', 'Retro Pvp', 'Preview'], width=6)
        self.combo2 = ttk.Combobox(root, values=self.comboList['NonPvp'], width=10)
            
        
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
        #self.combo.grid(row=5, column=2)
        self.combo2.grid(row=5, column=3)
        
    '''
    def comboCall(self):
        if self.combo.get() == 'NonPvp':
            self.combo2 = ttk.Combobox(root, values=self.comboList['NonPvp'], width=10)
        elif self.combo.get() == 'OpenPvp':
            self.combo2 = ttk.Combobox(root, values=self.comboList['OpenPvp'], width=10)
        elif self.combo.get() == 'RetroPvp':
            self.combo2 = ttk.Combobox(root, values=self.comboList['RetroPvp'], width=10)
        elif self.combo.get() == 'Preview':
            self.combo2 = ttk.Combobox(root, values=self.comboList['Preview'], width=10)
    '''
        
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