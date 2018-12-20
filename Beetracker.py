#!/bin/usr/env python3

'''
Copyright © 2018 UnclassedPenguin
Author: UnclassedPenguin
App: Bee Tracker
Description: keep track of your hives
'''

#    conn = sqlite3.connect(database)
#    curs = conn.cursor()
#    conn.close()

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
import mainwindow, tablewindow, printwindow

class BeeTracker(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(BeeTracker, self).__init__()
        self.setupUi(self)
        self.dialogs = []

        self.initial_Config()
        self.button_Config()
        self.location_Config()

##############################
####### INITIAL CONFIG #######
##############################

    def initial_Config(self):
        self.create_Tables()

        # Write the Main page message
        self.welcomemessage = '''Welcome to Bee Tracker \n
To Get started \n -Add Your first location in the "Add Location" tab\n -Then add some hives in the "Add Hives" tab\n -then search to your hearts content!'''
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
        self.testButton.clicked.connect(self.test)
        self.test2Button.clicked.connect(self.test)
        self.quitButton.clicked.connect(self.close)

        # Add Location Tab
        self.clearlocationButton.clicked.connect(self.clear_Location)
        self.search3Button.clicked.connect(self.search_Location)
        self.addlocationButton.clicked.connect(self.save_Location)
        self.viewlocationButton.clicked.connect(self.display_Locations)

        # Add Hive Tab
        self.clearhiveButton.clicked.connect(self.clear_Hive)
        self.searchButton.clicked.connect(self.search_Hive)
        self.saveButton.clicked.connect(self.save_Hive)
        self.viewhivesButton.clicked.connect(self.display_Hives)

        # Manage Hives Tab
        self.movehivesButton.clicked.connect(self.move_Hives)

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
        self.location3Box.clear()
        self.locationBox.addItems(self.locations)
        self.location2Box.addItems(self.locations)
        self.location3Box.addItems(self.locations)
        conn.close()
        return self.locations

    def write_Mainpage(self):
        self.maintextBrowser.setText(self.welcomemessage)

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

##################################
####### END INITIAL CONFIG #######
##################################

##############################
####### MISC FUNCTIONS #######
##############################

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

    def test(self):
        # self.msg('','TEST BUTTON','You pushed a testButton','')
        if self.doesit_Exist('cleanhives', 'hive', '6'):
            self.msg('','thing','itworked','')

    def doesit_Exist(self, table, column, it):
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        if table == 'cleanhives' and column == 'location':
            curs.execute('select location from cleanhives')
        elif table == 'cleanhives' and column == 'hive':
            curs.execute('select hive from cleanhives')
        elif table == 'location' and column == 'location':
            curs.execute('select location from location')
        elif table == 'location' and column == 'address':
            curs.execute('select address from location')
        tempstr = curs.fetchall()
        templist = [thing[0] for thing in tempstr]
        conn.close()
        if it in templist:
            return True
        else:
            return False

##################################
####### END MISC FUNCTIONS #######
##################################

################################
####### ADD LOCATION TAB #######
################################

    def display_Locations(self):
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        self.sql = '''select location, address, type, notes from location'''
        x = pd.read_sql_query(self.sql, conn)
        searchlist = ['location', 'address', 'type', 'notes']
        self.window = TablePage()
        df = x
        self.window.table.setColumnCount(len(df.columns))
        self.window.table.setRowCount(len(df.index))
        self.window.table.setHorizontalHeaderLabels(searchlist)
        for i in range(len(df.index)):
            for j in range(len(df.columns)):
                self.window.table.setItem(i,j,QTableWidgetItem(str(df.iloc[i, j])))
        self.window.table.setWordWrap(True)
        self.window.table.resizeRowsToContents()
        self.window.table.resizeColumnsToContents()
        self.window.show()
        curs.close()
        conn.close()

    def save_Location(self):
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        name = self.locationnameEdit.text()
        address = self.locationaddressEdit.text()
        locationtype = self.locationtypeBox.currentText()
        notes = self.locationnotesEdit.toPlainText()
        if len(name) > 0:
            print("New Location: {}".format(name))
            if len(name) > 0:
                print("Updating Groups List...")
                curs.execute("REPLACE INTO location(location, address, type, notes) VALUES (?,?,?,?) ", (name, address, locationtype, notes))
                conn.commit()
            self.msg('info', 'Info', 'Added - {}'.format(name), '')
            self.location_Config()
        conn.close()

    def search_Location(self):
        location = self.locationnameEdit.text()
        address = self.locationaddressEdit.text()
        if len(location) > 0:
            if self.doesit_Exist('location', 'location', location):
                conn = sqlite3.connect(database)
                curs = conn.cursor()
                curs.execute('''SELECT * from location where location = ? ''', (location,))
                tempstr = curs.fetchall()
                print(tempstr)
                index = self.locationtypeBox.findText(tempstr[0][3], \
                                                QtCore.Qt.MatchFixedString)
                self.locationtypeBox.setCurrentIndex(index)
                self.locationaddressEdit.setText(tempstr[0][2])
                self.locationnotesEdit.setText(tempstr[0][4])
                conn.close()
            else:
                self.msg('','Info','Name Does not exist','')
        elif len(address) > 0:
            if self.doesit_Exist('location', 'address', address):
                conn = sqlite3.connect(database)
                curs = conn.cursor()
                curs.execute('''SELECT * from location where address = ? ''', (address,))
                tempstr = curs.fetchall()
                print(tempstr)
                index = self.locationtypeBox.findText(tempstr[0][3], \
                                                QtCore.Qt.MatchFixedString)
                self.locationtypeBox.setCurrentIndex(index)
                self.locationnameEdit.setText(tempstr[0][1])
                self.locationnotesEdit.setText(tempstr[0][4])
                conn.close()
            else:
                self.msg('','Info','Address Does not exist','')
        elif len(location) == 0 and len(address) == 0:
            self.msg('','Info','Please enter at lease a Location Name','')

    def clear_Location(self):
        self.locationnameEdit.setText('')
        self.locationaddressEdit.setText('')
        self.locationtypeBox.setCurrentIndex(0)
        self.locationnotesEdit.setText('')

####################################
####### END ADD LOCATION TAB #######
####################################

############################
####### ADD HIVE TAB #######
############################

    def display_Hives(self):
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        self.sql = '''select date, location, hive, hivestrength, numberofsupers, notes from cleanhives'''
        x = pd.read_sql_query(self.sql, conn)
        p = x.sort_values(by=['hive'])
        searchlist = ['date', 'location', 'hive', 'hivestrength', 'numberofsupers', 'notes']
        self.window = TablePage()
        df = p
        self.window.table.setColumnCount(len(df.columns))
        self.window.table.setRowCount(len(df.index))
        self.window.table.setHorizontalHeaderLabels(searchlist)
        for i in range(len(df.index)):
            for j in range(len(df.columns)):
                self.window.table.setItem(i,j,QTableWidgetItem(str(df.iloc[i, j])))
        self.window.table.setWordWrap(True)
        self.window.table.resizeRowsToContents()
        self.window.table.resizeColumnsToContents()
        self.window.show()
        curs.close()
        conn.close()

    def save_Hive(self):
        date = datetime.now().strftime('%Y-%m-%d')
        location = self.locationBox.currentText()
        hive = self.hivenameEdit.text()
        hivestrength = self.hivestrengthBox.currentText()
        numberofsupers = self.numberofsupersBox.currentText()
        notes = self.hivenotesEdit.toPlainText()
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

    def search_Hive(self):
        hive = self.hivenameEdit.text()
        if len(hive) > 0:
            if self.doesit_Exist('cleanhives', 'hive', hive):
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
                self.hivenotesEdit.setText(tempstr[0][6])

                conn.close()
            else:
                self.msg('','Info','Hive "{}" does not exist'.format(hive),'')
        elif len(hive) == 0:
            self.msg('','Info','Please enter a Hive Name','')

    def clear_Hive(self):
        # self.locationBox.setCurrentIndex(0)
        self.hivenameEdit.setText('')
        self.numberofsupersBox.setCurrentIndex(0)
        self.hivestrengthBox.setCurrentIndex(0)
        self.hivenotesEdit.setText('')

# Keeping this just in case I need to add a page, this is how to open it.
    # def goto_Pagetwo(self):
        # dialog = Pagetwo(self)
        # self.dialogs.append(dialog)
        # dialog.show()

################################
####### END ADD HIVE TAB #######
################################

################################
####### MANAGE HIVES TAB #######
################################

    def move_Hives(self):
        newlocation = self.location3Box.currentText()
        if newlocation != 'All':
            hives = self.multihivesEdit.text()
            if len(hives) > 0:
                hiveslist = [hive.strip() for hive in hives.split(',')]
                date = datetime.now().strftime('%Y-%m-%d')
                hivedict = {}
                conn = sqlite3.connect(database)
                curs = conn.cursor()

                for hive in hiveslist:
                    if self.doesit_Exist('cleanhives', 'hive', hive):
                        curs.execute('''SELECT * from cleanhives where hive = ? ''', (hive,))
                        tempstr = curs.fetchall()
                        tempstrclean = tempstr[0]
                        hivedict['{}'.format(hive)] = tempstrclean
                    else:
                        self.msg('','Info','Hive {} does not exist'.format(hive),'')

                if len(hivedict) != 0:
                    for hive, values in hivedict.items():
                        hivestrength = values[4]
                        numberofsupers = values[5]
                        notes = values[6]
                        data_to_inject = (date, newlocation, hive, hivestrength, numberofsupers, notes)
                        curs.execute('''INSERT INTO hives(date, location, hive, hivestrength, numberofsupers, notes)
                                        VALUES(?,?,?,?,?,?)''', data_to_inject)
                        curs.execute('''REPLACE INTO cleanhives(date, location, hive, hivestrength, numberofsupers, notes)
                                        VALUES(?,?,?,?,?,?)''', data_to_inject)
                        conn.commit()
                    self.msg('','Info','Hive Locations Saved','')
                conn.close()
            elif len(hives) == 0:
                self.msg('','Info','Please Enter some hives first','')
        else:
            self.msg('','Info','Cannot move to location "All"','')

####################################
####### END MANAGE HIVES TAB #######
####################################

##############################
####### ADV SEARCH TAB #######
##############################

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
            if self.doesit_Exist('cleanhives', 'hive', self.hivename2Edit.text()):
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
            else:
                self.msg('','Info','Hive "{}" does not exist'.format(self.hivename2Edit.text()),'')
                x = None
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
            self.window = TablePage()
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

##################################
####### END ADV SEARCH TAB #######
##################################

class TablePage(QtWidgets.QMainWindow, tablewindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(TablePage, self).__init__()
        self.widget = QWidget()
        self.setupUi(self)
        self.closeButton.clicked.connect(self.close)

class PrintPage(QtWidgets.QMainWindow, printwindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(PrintPage, self).__init__()
        self.widget = QWidget()
        self.setupUi(self)
        self.closeButton.clicked.connect(self.close)

def main():
    app = QApplication(sys.argv)
    main = BeeTracker()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
