#!/bin/usr/env python3

'''
Copyright © 2018 UnclassedPenguin
Author: UnclassedPenguin
App: Bee Tracker
Description: keep track of your hives
'''

import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
import sys
import networkx
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QMenuBar, \
    QWidget,QScrollArea, QTableWidget, QVBoxLayout,QTableWidgetItem, QAction
from PyQt5.QtWidgets import QApplication
from datetime import datetime
import pandas as pd
import sqlite3
import xlsxwriter
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
database = config['DEFAULT']['database']
import mainwindow, tablewindow

class BeeTracker(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(BeeTracker, self).__init__()
        self.setupUi(self)
        self.dialogs = []

        self.initial_Config()
        self.button_Config()
        self.location_Config()

#####
##### INITIAL CONFIG
#####

    def initial_Config(self):
        self.create_Tables()
        self.write_Mainpage()
        self.datelabel.setText(datetime.now().strftime("%a %b %d, %Y"))
        numberofsupers = ['1','2','3','4']
        self.numberofsupersBox.addItems(numberofsupers)
        list1 = ['Good', 'Ok', 'Bad']
        self.hivestrengthBox.clear()
        self.hivestrengthBox.addItems(list1)
        list2 = ['Clean Data', 'Historical Data']
        self.tableBox.clear()
        self.tableBox.addItems(list2)
        list3 = ['Strong Hives', 'Weak Hives', 'Nukes']
        self.locationtypeBox.clear()
        self.locationtypeBox.addItems(list3)
        self.orderbygroups = ['None', 'Date Asc.', 'Date Des.', \
                              'Hive Asc.', 'Hive Des.', \
                              'Hive Strength Asc.', 'Hive Strength Des.', \
                              'Location Asc.', 'Location Des.', \
                              '# of Supers Asc.', '# of Supers Des.', \
                              'Notes Asc.', 'Notes Des.']
        self.orderbydict = {'None': 'None',\
                         'Date Asc.': 'date', 'Date Des.': 'date',\
                         'Hive Asc.':'hive', 'Hive Des.':'hive',\
                            'Hive Strength Asc.':'hivestrength', 'Hie Strength Des.':'hivestrength',\
                         'Location Asc.': 'location', 'Location Des.': 'location',\
                         '# of Supers Asc.': 'numberofsupers', '# of Supers Des.': 'numberofsupers',\
                         'Notes Asc.': 'notes', 'Notes Des.': 'notes'}
        self.orderbyBox.clear()
        self.orderbyBox.addItems(self.orderbygroups)

    def button_Config(self):
        # Main Program
        self.quitButton.clicked.connect(self.close)

        # Add Location Tab
        self.addlocationButton.clicked.connect(self.save_Location)
        self.viewlocationButton.clicked.connect(self.view_Locations)

        # Add Hive Tab
        self.testButton.clicked.connect(self.test)
        self.test2Button.clicked.connect(self.test)
        self.searchButton.clicked.connect(self.search)
        self.saveButton.clicked.connect(self.save)

        # Advanced Search Tab
        self.toggleallButton.clicked.connect(self.toggle_All)
        self.test3Button.clicked.connect(self.get_Cbvalues)
        self.search2Button.clicked.connect(self.adv_Searchtwo)

    def location_Config(self):
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        curs.execute('INSERT INTO location(location) values("All");')
        curs.execute('INSERT INTO location(location) values("Home");')
        curs.execute('SELECT location FROM location')
        dirtylist = curs.fetchall()
        self.locations = []
        self.locations = list(sum(dirtylist, ()))
        print("Clean {}".format(self.locations))
        self.locationBox.clear()
        self.location2Box.clear()
        self.locationBox.addItems(self.locations)
        self.location2Box.addItems(self.locations)
        conn.close()
        return self.locations

    def write_Mainpage(self):
        welcomemessage = '''Welcome to Bee Tracker \n
To Get started \n -Add Your first location in the "Add Location" tab \n -Then add some hives in the "Add Hives" tab \n -then search to your hearts content!'''
        self.maintextBrowser.setText(welcomemessage)

    def msg(self, messagetype, messagetitle, infotext, messagetext):
        if messagetype == 'info':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText(infotext)
            msg.setInformativeText(messagetext)
            msg.setWindowTitle(messagetitle)
            msg.exec()
        if messagetype == 'crit':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText(infotext)
            msg.setInformativeText(messagetext)
            msg.setWindowTitle(messagetitle)
            msg.exec()
        if messagetype == "":
            msg = QtWidgets.QMessageBox()
            msg.setText(infotext)
            msg.setInformativeText(messagetext)
            msg.setWindowTitle(messagetitle)
            msg.exec()

    def create_Tables(self):
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        curs.execute('''CREATE TABLE IF NOT EXISTS hives
                   (numid integer PRIMARY KEY, date, location, hive, hivestrength, numberofsupers, notes)''')
        curs.execute('''CREATE TABLE IF NOT EXISTS cleanhives
                   (numid integer PRIMARY KEY, date, location, hive, hivestrength, numberofsupers, notes)''')
        curs.execute("CREATE UNIQUE INDEX if not exists" \
                     " numidx_cleanhives_name ON cleanhives (hive);")
        curs.execute('''CREATE TABLE IF NOT EXISTS location
                   (numid integer PRIMARY KEY, location, address, type, notes)''')
        curs.execute("CREATE UNIQUE INDEX if not exists" \
                     " numidx_location_name ON location (location);")
        conn.commit()
        conn.close()

#####
##### TEST FUNCTION
#####

    def test(self):
        self.msg('','TEST BUTTON','You pushed a testButton','')

#####
##### ADD HIVE TAB
#####

    def save(self):
        date = datetime.now().strftime('%Y-%m-%d')
        location = self.locationBox.currentText()
        hive = self.hivenameEdit.text()
        hivestrength = self.hivestrengthBox.currentText()
        numberofsupers = self.numberofsupersBox.currentText()
        notes = self.notesEdit.toPlainText()
        if len(hive) > 0:
            conn = sqlite3.connect(database)
            curs = conn.cursor()

            data_to_inject = (date, location, hive, hivestrength, numberofsupers, notes)
            curs.execute('''INSERT INTO hives(date, location, hive, hivestrength, numberofsupers, notes)
                            VALUES(?,?,?,?,?,?)''', data_to_inject)
            curs.execute('''REPLACE INTO cleanhives(date, location, hive, hivestrength, numberofsupers, notes)
                            VALUES(?,?,?,?,?,?)''', data_to_inject)
            conn.commit()
            conn.close()
            self.msg('','Info','{} Saved'.format(hive),'')
        elif len(hive) == 0:
            self.msg('','Info','Please enter a Hive Name','')

    def search(self):
        hive = self.hivenameEdit.text()
        if len(hive) > 0:
            conn = sqlite3.connect(database)
            curs = conn.cursor()

            curs.execute('''SELECT * from cleanhives where hive = ? ''', (hive,))
            tempstr = curs.fetchall()
            print(tempstr)
            index = self.locationBox.findText(tempstr[0][2], \
                                               QtCore.Qt.MatchFixedString)
            self.locationBox.setCurrentIndex(index)
            index2 = self.numberofsupersBox.findText(tempstr[0][5], \
                                               QtCore.Qt.MatchFixedString)
            self.numberofsupersBox.setCurrentIndex(index2)
            index3 = self.hivestrengthBox.findText(tempstr[0][4], \
                                               QtCore.Qt.MatchFixedString)
            self.hivestrengthBox.setCurrentIndex(index3)
            self.hivenameEdit.setText(tempstr[0][3])
            self.notesEdit.setText(tempstr[0][6])

            conn.close()
        elif len(hive) == 0:
            self.msg('','Info','Please enter a Hive Name','')

    # def goto_Pagetwo(self):
        # dialog = Pagetwo(self)
        # self.dialogs.append(dialog)
        # dialog.show()

#####
##### ADD LOCATION TAB
#####

    def save_Location(self):
        conn = sqlite3.connect(database)
        curs = conn.cursor()

        name = self.locationnameEdit.text()
        address = self.locationaddressEdit.text()
        locationtype = self.locationtypeBox.currentText()
        notes = self.locationnotesEdit.toPlainText()

        print("New Location: {}".format(name))
        if len(name) > 0:
            print("Updating Groups List...")
            curs.execute("INSERT INTO location(location, address, type, notes) VALUES (?,?,?,?) ", (name, address, locationtype, notes))
            conn.commit()
        self.msg('info', 'Info', 'Added - {}'.format(name), '')
        conn.close()
        self.location_Config()

    def view_Locations(self):
        print("View Locations Button")
#####
##### SEARCH TAB
#####

    def adv_Searchone(self):
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        self.searchlist = []

        location = self.location2Box.currentText()

        self.searchlist_Append(self.datecbButton, 'date')
        self.searchlist_Append(self.locationcbButton, 'location')
        self.searchlist_Append(self.hivenamecbButton, 'hive')
        self.searchlist_Append(self.hivestrengthcbButton, 'hivestrength')
        self.searchlist_Append(self.numberofsuperscbButton, 'numberofsupers')
        self.searchlist_Append(self.notescbButton, 'notes')

        print(self.searchlist)
        self.tempstr = ', '.join(self.searchlist)
        self.searchlist2 = self.searchlist[:]
        self.orderby1 = str(self.orderbyBox.currentText())
        self.get_Cbvalues()
        print(self.orderby1)
        if self.newlist[3] == 1:
            sortby = 'numberofsupers'
        if self.newlist[4] == 1:
            sortby = 'notes'
        if self.newlist[0] == 1:
            sortby = 'hive'
        if self.newlist[1] == 1:
            sortby = 'date'
        if self.newlist[2] == 1:
            sortby = 'location'

        if len(self.hivename2Edit.text()) > 0 and self.newlist != [0, 0, 0, 0, 0, 0]:
           if self.tableBox.currentText() == 'Historical Data':
                self.sql = "SELECT " + self.tempstr + \
                    " from hives where hive IS " + "'" + \
                    self.hivename2Edit.text() + "'"
                print(self.sql)
                x = pd.read_sql_query(self.sql, conn)
           elif self.tableBox.currentText() == 'Clean Data':
                self.sql = "SELECT " + self.tempstr + \
                    " from cleanhives where hive IS " + "'" + \
                    self.hivename2Edit.text() + "'"
                print(self.sql)
                x = pd.read_sql_query(self.sql, conn)

        elif len(self.hivename2Edit.text()) == 0 and self.newlist != [0, 0, 0, 0, 0, 0]:
            if self.tableBox.currentText() == 'Historical Data':
                if location == 'All':
                    self.sql = "Select " + self.tempstr + " from hives"
                    print(self.sql)
                    y = pd.read_sql_query(self.sql, conn)
                    x = y.sort_values(by=[sortby])
                else:
                    self.sql = "SELECT " + self.tempstr + \
                        " from hives where location = " +"'" + location + "'"
                    print(self.sql)
                    x = pd.read_sql_query(self.sql, conn)
            elif self.tableBox.currentText() == 'Clean Data':
                if location == 'All':
                    self.sql = "Select " + self.tempstr + " from cleanhives"
                    print(self.sql)
                    y = pd.read_sql_query(self.sql, conn)
                    x = y.sort_values(by=[sortby])
                else:
                    self.sql = "SELECT " + self.tempstr + \
                        " from cleanhives where location = " + "'" + location + "'"
                    print(self.sql)
                    x = pd.read_sql_query(self.sql, conn)

        elif self.newlist == [0, 0, 0, 0, 0, 0]:
            self.msg('','Info','Nothing Selected to search','')
            x = None

        if self.orderby1 != 'None':
            try:
                if x is not None:
                    if self.orderby1[-4:] == 'Asc.':
                        p = x.sort_values(by=[self.orderbydict[self.orderby1]])
                        x = p
                    elif self.orderby1[-4:] == 'Des.':
                        p = x.sort_values(by=[self.orderbydict[self.orderby1]], ascending=False)
                        x = p
                elif x is None:
                    print("X is equal to None")
            except:
                self.msg('','Info',"Didn't work. Maybe you are trying to order by a value you don't have selected.",'')
        self.p = x
        print(type(self.p))
        self.searchlist.clear()
        curs.close()
        conn.close()
        return self.p

    def adv_Searchtwo(self):
        self.y = self.adv_Searchone()
        print(type(self.y))
        if isinstance(self.y, pd.core.frame.DataFrame):
            self.window = DisplayPage()
            df = self.y
            self.window.table.setColumnCount(len(df.columns))
            self.window.table.setRowCount(len(df.index))
            self.window.table.setHorizontalHeaderLabels(self.searchlist2)
            for i in range(len(df.index)):
                for j in range(len(df.columns)):
                    self.window.table.setItem(i,j,QTableWidgetItem(str(df.iloc[i, j])))
            self.window.table.setWordWrap(True)
            self.window.table.resizeRowsToContents()
            self.window.table.resizeColumnsToContents()
            self.window.show()
        elif isinstance(self.y, pd.core.frame.DataFrame) == False:
            pass

    def searchlist_Append(self, cbvar, dbvar):
        if cbvar.isChecked():
            conn = sqlite3.connect(database)
            curs = conn.cursor()
            o = dbvar
            curs.execute('SELECT ? FROM hives ', \
                             (o,))
            tempstr = curs.fetchall()
            if len(tempstr) > 0:
                self.searchlist.append(o)
            print('SEARCHLIST: {}'.format(self.searchlist))
            curs.close()
            conn.close()

    def toggle_All(self):
        x = self.get_Cbvalues()
        print(x)
        print("0: {}".format(x.count(0)))
        print("1: {}".format(x.count(1)))
        self.temp2list = [self.hivenamecbButton, self.datecbButton,
             self.locationcbButton, self.numberofsuperscbButton,
             self.notescbButton, self.hivestrengthcbButton]
        if x.count(1) <= 14 and x.count(1) > 1:
            for s in self.temp2list:
                s.setChecked(False)
        if x.count(0) <= 14 and x.count(0) > 1:
            for s in self.temp2list:
                s.setChecked(True)

    def get_Cbvalues(self):
        print("Getting CB Values")
        self.templist = {'self.hivenamecbButton': self.hivenamecbButton,
                         'self.datecbButton': self.datecbButton,
                         'self.locationcbButton': self.locationcbButton,
                         'self.numberofsuperscbButton': self.numberofsuperscbButton,
                         'self.notescbButton': self.notescbButton,
                         'self.hivestrengthcbButton': self.hivestrengthcbButton
                         }
        self.newdict = {}
        self.newlist = []
        self.newlist.clear()

        for key, value in self.templist.items():
            if value.isChecked():
                self.newdict[key] = 1
                self.newlist.append(1)
            elif value.isChecked() == False:
                self.newdict[key] = 0
                self.newlist.append(0)

        print("New list: {}".format(self.newlist))
        print("Got CB Values")
        return self.newlist

class DisplayPage(QtWidgets.QMainWindow, tablewindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(DisplayPage, self).__init__()
        self.widget = QWidget()
        self.setupUi(self)

        self.actionClose_2.triggered.connect(self.close)

def main():
    app = QApplication(sys.argv)
    main = BeeTracker()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
