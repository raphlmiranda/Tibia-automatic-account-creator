from tkinter import *
from tkinter import ttk
from selenium import webdriver
from tkinter import messagebox
import os
#pyinstaller --onefile GUI.py

selenium = webdriver
root = Tk()

class GUI():

    def __init__(self):
                                    ###Words List### From web scraping with bs4
        self.comboList = {
            'NonPvp': ['Belobra', 'Beneva', 'Calmera', 'Candia', 'Celesta', 'Damora', 'Descubra', 'Fidera', 'Gentebra', 'Guardia','Astera','Harmonia','Honera','Kalibra','Luminera','Magera','Menera','Nerana','Olera','Olympa','Pacera','Refugia','Secura','Tavara','Unitera','Veludera'],
            'OpenPvp': ['Amera','Antica','Estela','Ferobra','Fotera','Garnera','Honbra','Impera','Inabra','Julera','Justera','Kenora','Laudera','Noctera','Peloria','Premia','Quelibra','Quintera','Serdebra','Shivera','Silvera','Solera','Thera','Umera','Vita','Vunira','Xantera','Zanera'],
            'RetroPvp': ['Chrona','Duna','Eldera','Lutabra','Morta','Mortera','Relembra'],
            'RetroHardcore': ['Helera','Macabra','Tortura'],
            'Preview': ['Zuna','Zunera']
            #'AllWorlds': 
        }
                                    ###Selenium Variables###
        self.url = 'https://secure.tibia.com/account/?subtopic=createaccount'
        self.bool = False
                                    ###GUI Variables###
        #self.l1 = Label(root, text='Create Tibia Accounts Automatic')
        self.l2 = Label(root, text='Account')
        self.l3 = Label(root, text='Password')
        self.l4 = Label(root, text='Quantity')
        self.ent1 = Entry(root)
        self.ent2 = Entry(root)
        self.ent3 = Entry(root, width=5)
        self.btn = Button(root, text='Create Accounts', command=self.callSelenium)
        #self.txt = Text(root, width=10, height=10)
        self.l5 = Label(root, text='World')
        self.combo = ttk.Combobox(root, values=['Non Pvp', 'Open Pvp', 'Retro Pvp', 'Retro Hardcore'], width=10)

    def changeCombobox(self, event):
        current = self.combo.current()
        if current == 0:
            self.combo2 = ttk.Combobox(root, values=self.comboList['NonPvp'], width=10)
            self.wordType = 1
            self.combo2.grid(row=5, column=3)
            self.combo2.bind('<<ComboboxSelected>>', self.getWorld)
        elif current == 1:
            self.combo2 = ttk.Combobox(root, values=self.comboList['OpenPvp'], width=10)
            self.wordType = 2
            self.combo2.grid(row=5, column=3)
            self.combo2.bind('<<ComboboxSelected>>', self.getWorld)
        elif current == 2:
            self.combo2 = ttk.Combobox(root, values=self.comboList['RetroPvp'], width=10)
            self.wordType = 3
            self.combo2.grid(row=5, column=3)
            self.combo2.bind('<<ComboboxSelected>>', self.getWorld)
        elif current == 3:
            self.combo2 = ttk.Combobox(root, values=self.comboList['RetroHardcore'], width=10)
            self.wordType = 4
            self.combo2.grid(row=5, column=3)
            self.combo2.bind('<<ComboboxSelected>>', self.getWorld)

    def _show(self):
        root.title('Tibia ACC Creator')
        #self.l1.grid(row=1, column=2)
        self.l2.grid(row=2)
        self.ent1.grid(row=2, column=2)
        self.l3.grid(row=3)
        self.ent2.grid(row=3, column=2)
        self.l4.grid(row=4)
        self.ent3.grid(row=4, column=2)
        self.btn.grid(row=6, column=2)
        self.l5.grid(row=5)
        self.combo.grid(row=5, column=2)
        self.combo.bind('<<ComboboxSelected>>', self.changeCombobox)
    
    def createLog(self):
        self.user = os.getlogin()
        self.path = 'c:\\users\\%s\\tibiaAcc.txt' %self.user
        self.file = open(self.path, 'a')
        self.file.write('Account Name: ' + self.ent1.get() + ' | Password: ' + self.ent2.get() + ' | World: ' + self.combo2.get() +'\n')
    
    def getWorld(self, event):
        self.tt = self.combo2.get() 

    def checkAll(self):

        if len(self.ent1.get()) < 6 and len(self.ent2.get()) < 8:
            messagebox.showerror('Error', 'Your account need be 6 or more letters and password 8 or more letters.')
        else:
            self.bool = True
        return self.bool

    def callSelenium(self): # 
        qty = int(self.ent3.get())
        if self.checkAll() and isinstance(qty, int) and qty != 0:   
            open = selenium.Chrome()  
            self.createLog()     
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
                self.wordXpath = {
                        'Change': open.find_element_by_xpath('//*[@id="suggested_world_box"]/span[2]/small/a'),
                        'All': open.find_element_by_xpath('//*[@id="option_server_location_all"]'),
                        #'world': open.find_element_by_id('#server_%s' % self.tt)
                    }
                self.wordTypes = {
                    '1': open.find_element_by_xpath('//*[@id="option_server_pvp_type_optional_label"]/img'),
                    '2': open.find_element_by_xpath('//*[@id="option_server_pvp_type_open_label"]/img'),
                    '3': open.find_element_by_xpath('//*[@id="option_server_pvp_type_retro_label"]/img'),
                    '4': open.find_element_by_xpath('//*[@id="option_server_pvp_type_retrohardcore_label"]/img')
                    }
                                ###Selenium Actions###
                self.accountElements['account'].send_keys(self.ent1.get()+str(i))
                self.accountElements['password'].send_keys(self.ent2.get()+str(i))
                self.accountElements['password2'].send_keys(self.ent2.get()+str(i))
                self.accountElements['email'].send_keys(self.ent1.get()+str(i)+'@mozej.com')
                self.accountElements['SuggestName'].click()
                self.wordXpath['Change'].click()
                self.wordXpath['All'].click()
                for i in self.wordTypes:
                    if int(i) == self.wordType:
                        self.wordTypes[i].click()
                #self.wordXpath['world'].click()

start = GUI()
start._show()
mainloop()