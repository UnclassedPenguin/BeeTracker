# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(383, 481)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.datelabel = QtWidgets.QLabel(self.centralwidget)
        self.datelabel.setText("")
        self.datelabel.setObjectName("datelabel")
        self.gridLayout.addWidget(self.datelabel, 0, 0, 1, 1)
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setObjectName("quitButton")
        self.gridLayout.addWidget(self.quitButton, 2, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.maintextBrowser = QtWidgets.QTextBrowser(self.tab_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.maintextBrowser.setFont(font)
        self.maintextBrowser.setObjectName("maintextBrowser")
        self.gridLayout_5.addWidget(self.maintextBrowser, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_13 = QtWidgets.QLabel(self.tab_7)
        self.label_13.setObjectName("label_13")
        self.gridLayout_7.addWidget(self.label_13, 4, 0, 1, 1)
        self.addlocationButton = QtWidgets.QPushButton(self.tab_7)
        self.addlocationButton.setObjectName("addlocationButton")
        self.gridLayout_7.addWidget(self.addlocationButton, 6, 1, 1, 1)
        self.locationaddressEdit = QtWidgets.QLineEdit(self.tab_7)
        self.locationaddressEdit.setObjectName("locationaddressEdit")
        self.gridLayout_7.addWidget(self.locationaddressEdit, 2, 1, 1, 1)
        self.locationnameEdit = QtWidgets.QLineEdit(self.tab_7)
        self.locationnameEdit.setObjectName("locationnameEdit")
        self.gridLayout_7.addWidget(self.locationnameEdit, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_7)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_7)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_7.addWidget(self.label_12, 2, 0, 1, 1)
        self.locationnotesEdit = QtWidgets.QTextEdit(self.tab_7)
        self.locationnotesEdit.setObjectName("locationnotesEdit")
        self.gridLayout_7.addWidget(self.locationnotesEdit, 5, 0, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.tab_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_7.addWidget(self.label_15, 0, 0, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.tab_7)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_7.addWidget(self.label_16, 3, 0, 1, 1)
        self.locationtypeBox = QtWidgets.QComboBox(self.tab_7)
        self.locationtypeBox.setObjectName("locationtypeBox")
        self.gridLayout_7.addWidget(self.locationtypeBox, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_7 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 0, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 1, 0, 1, 1)
        self.locationBox = QtWidgets.QComboBox(self.tab)
        self.locationBox.setObjectName("locationBox")
        self.gridLayout_6.addWidget(self.locationBox, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 2, 0, 1, 1)
        self.hivenameEdit = QtWidgets.QLineEdit(self.tab)
        self.hivenameEdit.setObjectName("hivenameEdit")
        self.gridLayout_6.addWidget(self.hivenameEdit, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 3, 0, 1, 1)
        self.numberofsupersBox = QtWidgets.QComboBox(self.tab)
        self.numberofsupersBox.setObjectName("numberofsupersBox")
        self.gridLayout_6.addWidget(self.numberofsupersBox, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 6, 0, 1, 1)
        self.notesEdit = QtWidgets.QTextEdit(self.tab)
        self.notesEdit.setObjectName("notesEdit")
        self.gridLayout_6.addWidget(self.notesEdit, 7, 0, 4, 2)
        self.searchButton = QtWidgets.QPushButton(self.tab)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout_6.addWidget(self.searchButton, 7, 2, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.tab)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout_6.addWidget(self.saveButton, 8, 2, 1, 1)
        self.testButton = QtWidgets.QPushButton(self.tab)
        self.testButton.setObjectName("testButton")
        self.gridLayout_6.addWidget(self.testButton, 9, 2, 1, 1)
        self.test2Button = QtWidgets.QPushButton(self.tab)
        self.test2Button.setObjectName("test2Button")
        self.gridLayout_6.addWidget(self.test2Button, 10, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setObjectName("label_14")
        self.gridLayout_6.addWidget(self.label_14, 4, 0, 1, 1)
        self.hivestrengthBox = QtWidgets.QComboBox(self.tab)
        self.hivestrengthBox.setObjectName("hivestrengthBox")
        self.gridLayout_6.addWidget(self.hivestrengthBox, 4, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 1, 1, 3)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_3)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.location2Box = QtWidgets.QComboBox(self.tab_4)
        self.location2Box.setObjectName("location2Box")
        self.gridLayout_2.addWidget(self.location2Box, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.hivename2Edit = QtWidgets.QLineEdit(self.tab_4)
        self.hivename2Edit.setObjectName("hivename2Edit")
        self.gridLayout_2.addWidget(self.hivename2Edit, 1, 1, 1, 1)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)
        self.distinctcbButton = QtWidgets.QCheckBox(self.tab_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.distinctcbButton.setFont(font)
        self.distinctcbButton.setObjectName("distinctcbButton")
        self.gridLayout_3.addWidget(self.distinctcbButton, 1, 1, 1, 2)
        self.orderbyBox = QtWidgets.QComboBox(self.tab_5)
        self.orderbyBox.setObjectName("orderbyBox")
        self.gridLayout_3.addWidget(self.orderbyBox, 2, 1, 1, 2)
        self.tableBox = QtWidgets.QComboBox(self.tab_5)
        self.tableBox.setObjectName("tableBox")
        self.gridLayout_3.addWidget(self.tableBox, 0, 1, 1, 2)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.gridLayout_4.addWidget(self.tabWidget_2, 1, 1, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(61, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(62, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 2, 0, 1, 1)
        self.toggleallButton = QtWidgets.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.toggleallButton.setFont(font)
        self.toggleallButton.setObjectName("toggleallButton")
        self.gridLayout_4.addWidget(self.toggleallButton, 2, 1, 1, 1)
        self.hivenamecbButton = QtWidgets.QCheckBox(self.tab_3)
        self.hivenamecbButton.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hivenamecbButton.setFont(font)
        self.hivenamecbButton.setChecked(True)
        self.hivenamecbButton.setObjectName("hivenamecbButton")
        self.gridLayout_4.addWidget(self.hivenamecbButton, 3, 1, 1, 1)
        self.datecbButton = QtWidgets.QCheckBox(self.tab_3)
        self.datecbButton.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.datecbButton.setFont(font)
        self.datecbButton.setChecked(True)
        self.datecbButton.setObjectName("datecbButton")
        self.gridLayout_4.addWidget(self.datecbButton, 3, 2, 1, 1)
        self.locationcbButton = QtWidgets.QCheckBox(self.tab_3)
        self.locationcbButton.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.locationcbButton.setFont(font)
        self.locationcbButton.setChecked(True)
        self.locationcbButton.setObjectName("locationcbButton")
        self.gridLayout_4.addWidget(self.locationcbButton, 3, 3, 1, 1)
        self.numberofsuperscbButton = QtWidgets.QCheckBox(self.tab_3)
        self.numberofsuperscbButton.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.numberofsuperscbButton.setFont(font)
        self.numberofsuperscbButton.setChecked(True)
        self.numberofsuperscbButton.setObjectName("numberofsuperscbButton")
        self.gridLayout_4.addWidget(self.numberofsuperscbButton, 4, 1, 1, 1)
        self.notescbButton = QtWidgets.QCheckBox(self.tab_3)
        self.notescbButton.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.notescbButton.setFont(font)
        self.notescbButton.setChecked(True)
        self.notescbButton.setObjectName("notescbButton")
        self.gridLayout_4.addWidget(self.notescbButton, 4, 2, 1, 1)
        self.search2Button = QtWidgets.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.search2Button.setFont(font)
        self.search2Button.setObjectName("search2Button")
        self.gridLayout_4.addWidget(self.search2Button, 5, 2, 1, 1)
        self.clear2Button = QtWidgets.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.clear2Button.setFont(font)
        self.clear2Button.setObjectName("clear2Button")
        self.gridLayout_4.addWidget(self.clear2Button, 5, 3, 1, 1)
        self.test3Button = QtWidgets.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.test3Button.setFont(font)
        self.test3Button.setObjectName("test3Button")
        self.gridLayout_4.addWidget(self.test3Button, 6, 1, 1, 1)
        self.save2Button = QtWidgets.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.save2Button.setFont(font)
        self.save2Button.setObjectName("save2Button")
        self.gridLayout_4.addWidget(self.save2Button, 6, 2, 1, 1)
        self.quit2Button = QtWidgets.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.quit2Button.setFont(font)
        self.quit2Button.setObjectName("quit2Button")
        self.gridLayout_4.addWidget(self.quit2Button, 6, 3, 1, 1)
        self.hivestrengthcbButton = QtWidgets.QCheckBox(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.hivestrengthcbButton.setFont(font)
        self.hivestrengthcbButton.setChecked(True)
        self.hivestrengthcbButton.setObjectName("hivestrengthcbButton")
        self.gridLayout_4.addWidget(self.hivestrengthcbButton, 4, 3, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.locationnameEdit)
        MainWindow.setTabOrder(self.locationnameEdit, self.locationaddressEdit)
        MainWindow.setTabOrder(self.locationaddressEdit, self.locationtypeBox)
        MainWindow.setTabOrder(self.locationtypeBox, self.locationnotesEdit)
        MainWindow.setTabOrder(self.locationnotesEdit, self.addlocationButton)
        MainWindow.setTabOrder(self.addlocationButton, self.locationBox)
        MainWindow.setTabOrder(self.locationBox, self.hivenameEdit)
        MainWindow.setTabOrder(self.hivenameEdit, self.numberofsupersBox)
        MainWindow.setTabOrder(self.numberofsupersBox, self.hivestrengthBox)
        MainWindow.setTabOrder(self.hivestrengthBox, self.notesEdit)
        MainWindow.setTabOrder(self.notesEdit, self.searchButton)
        MainWindow.setTabOrder(self.searchButton, self.saveButton)
        MainWindow.setTabOrder(self.saveButton, self.testButton)
        MainWindow.setTabOrder(self.testButton, self.test2Button)
        MainWindow.setTabOrder(self.test2Button, self.tabWidget_2)
        MainWindow.setTabOrder(self.tabWidget_2, self.location2Box)
        MainWindow.setTabOrder(self.location2Box, self.hivename2Edit)
        MainWindow.setTabOrder(self.hivename2Edit, self.toggleallButton)
        MainWindow.setTabOrder(self.toggleallButton, self.hivenamecbButton)
        MainWindow.setTabOrder(self.hivenamecbButton, self.datecbButton)
        MainWindow.setTabOrder(self.datecbButton, self.locationcbButton)
        MainWindow.setTabOrder(self.locationcbButton, self.numberofsuperscbButton)
        MainWindow.setTabOrder(self.numberofsuperscbButton, self.notescbButton)
        MainWindow.setTabOrder(self.notescbButton, self.hivestrengthcbButton)
        MainWindow.setTabOrder(self.hivestrengthcbButton, self.search2Button)
        MainWindow.setTabOrder(self.search2Button, self.clear2Button)
        MainWindow.setTabOrder(self.clear2Button, self.test3Button)
        MainWindow.setTabOrder(self.test3Button, self.save2Button)
        MainWindow.setTabOrder(self.save2Button, self.quit2Button)
        MainWindow.setTabOrder(self.quit2Button, self.quitButton)
        MainWindow.setTabOrder(self.quitButton, self.maintextBrowser)
        MainWindow.setTabOrder(self.maintextBrowser, self.tableBox)
        MainWindow.setTabOrder(self.tableBox, self.orderbyBox)
        MainWindow.setTabOrder(self.orderbyBox, self.distinctcbButton)
        MainWindow.setTabOrder(self.distinctcbButton, self.textBrowser)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bee Tracker"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Main"))
        self.label_13.setText(_translate("MainWindow", "Notes: "))
        self.addlocationButton.setText(_translate("MainWindow", "Add Location"))
        self.label_8.setText(_translate("MainWindow", "Location Name: "))
        self.label_12.setText(_translate("MainWindow", "Address: "))
        self.label_15.setText(_translate("MainWindow", "Add A Location: "))
        self.label_16.setText(_translate("MainWindow", "Location Type: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Add Location"))
        self.label_7.setText(_translate("MainWindow", "Add A Hive:"))
        self.label_4.setText(_translate("MainWindow", "Location: "))
        self.label.setText(_translate("MainWindow", "Hive Name: "))
        self.label_2.setText(_translate("MainWindow", "# of Supers: "))
        self.label_3.setText(_translate("MainWindow", "Notes: "))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.testButton.setText(_translate("MainWindow", "Test"))
        self.test2Button.setText(_translate("MainWindow", "Test 2"))
        self.label_14.setText(_translate("MainWindow", "Hive Strength: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Add Hive"))
        self.label_5.setText(_translate("MainWindow", "Advanced Search"))
        self.label_6.setText(_translate("MainWindow", "Location:"))
        self.label_9.setText(_translate("MainWindow", "Hive Name:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Main"))
        self.label_10.setText(_translate("MainWindow", "Table:"))
        self.label_11.setText(_translate("MainWindow", "Order By:"))
        self.distinctcbButton.setText(_translate("MainWindow", "Distinct"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Options"))
        self.toggleallButton.setText(_translate("MainWindow", "Toggle All"))
        self.hivenamecbButton.setText(_translate("MainWindow", "Hive Name"))
        self.datecbButton.setText(_translate("MainWindow", "Date"))
        self.locationcbButton.setText(_translate("MainWindow", "Location"))
        self.numberofsuperscbButton.setText(_translate("MainWindow", "# of Supers"))
        self.notescbButton.setText(_translate("MainWindow", "Notes"))
        self.search2Button.setText(_translate("MainWindow", "Search"))
        self.clear2Button.setText(_translate("MainWindow", "Clear"))
        self.test3Button.setText(_translate("MainWindow", "Test 3"))
        self.save2Button.setText(_translate("MainWindow", "Save"))
        self.quit2Button.setText(_translate("MainWindow", "Close"))
        self.hivestrengthcbButton.setText(_translate("MainWindow", "Hive Strength"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "View"))

