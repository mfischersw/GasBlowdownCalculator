# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\GasBlowdownCalculator\src\gasblowdowncalculator\ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 659)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1200, 640))
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #696a6a, stop: 1 #212222);\n"
"    min-width: 1200px;\n"
"    min-height: 640px;\n"
"}\n"
"\n"
"#frameMain {\n"
"    border: 3px solid black;\n"
"    border-radius: 10px;\n"
"    background: white;\n"
"}\n"
"\n"
"#frameTopNavi {\n"
"    min-height: 50px;\n"
"   max-height: 65px;\n"
"}\n"
"\n"
"#frameBottom {\n"
"    min-height: 50px;\n"
"    max-height: 65px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frameTopNavi = QtWidgets.QFrame(self.centralwidget)
        self.frameTopNavi.setMinimumSize(QtCore.QSize(0, 52))
        self.frameTopNavi.setStyleSheet("QPushButton{\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #696a6a, stop: 1 #212222);\n"
"    font-weight: bold; \n"
"    font-size: 15px;\n"
"    color: white;\n"
"    min-width: 140px;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #03cb08, stop: 1 #015803);\n"
"}")
        self.frameTopNavi.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTopNavi.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTopNavi.setObjectName("frameTopNavi")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameTopNavi)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(329, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonGasComposition = QtWidgets.QPushButton(self.frameTopNavi)
        self.buttonGasComposition.setMinimumSize(QtCore.QSize(142, 32))
        self.buttonGasComposition.setCheckable(True)
        self.buttonGasComposition.setObjectName("buttonGasComposition")
        self.horizontalLayout.addWidget(self.buttonGasComposition)
        self.buttonScenario = QtWidgets.QPushButton(self.frameTopNavi)
        self.buttonScenario.setMinimumSize(QtCore.QSize(142, 32))
        self.buttonScenario.setCheckable(True)
        self.buttonScenario.setObjectName("buttonScenario")
        self.horizontalLayout.addWidget(self.buttonScenario)
        self.buttonResults = QtWidgets.QPushButton(self.frameTopNavi)
        self.buttonResults.setMinimumSize(QtCore.QSize(142, 32))
        self.buttonResults.setCheckable(True)
        self.buttonResults.setObjectName("buttonResults")
        self.horizontalLayout.addWidget(self.buttonResults)
        spacerItem1 = QtWidgets.QSpacerItem(329, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_16.addWidget(self.frameTopNavi)
        self.frameMain = QtWidgets.QFrame(self.centralwidget)
        self.frameMain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMain.setObjectName("frameMain")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frameMain)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.stackedWidgetMain = QtWidgets.QStackedWidget(self.frameMain)
        self.stackedWidgetMain.setObjectName("stackedWidgetMain")
        self.pageGasComposition = QtWidgets.QWidget()
        self.pageGasComposition.setObjectName("pageGasComposition")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.pageGasComposition)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_3 = QtWidgets.QFrame(self.pageGasComposition)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(876, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_12.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(self.pageGasComposition)
        self.frame.setStyleSheet("QTableView {\n"
"    border: 8px solid #f0f0f0;\n"
"    border-radius: 5px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frameGasFile = QtWidgets.QFrame(self.frame)
        self.frameGasFile.setStyleSheet("QPushButton{\n"
"    border: 1px solid black;\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #696a6a, stop: 1 #212222);\n"
"    border-radius: 5px;    \n"
"    font-weight: bold; \n"
"    font-size: 12px;\n"
"    color: white;\n"
"    min-height: 30px;\n"
"    max-height: 35px;\n"
"    min-width: 75px;\n"
"    max-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4a42ec, stop: 1 #0d04ba);\n"
"}")
        self.frameGasFile.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameGasFile.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameGasFile.setObjectName("frameGasFile")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frameGasFile)
        self.verticalLayout.setObjectName("verticalLayout")
        self.buttonNewGas = QtWidgets.QPushButton(self.frameGasFile)
        self.buttonNewGas.setMinimumSize(QtCore.QSize(77, 32))
        self.buttonNewGas.setObjectName("buttonNewGas")
        self.verticalLayout.addWidget(self.buttonNewGas)
        self.buttonLoadGas = QtWidgets.QPushButton(self.frameGasFile)
        self.buttonLoadGas.setMinimumSize(QtCore.QSize(77, 32))
        self.buttonLoadGas.setObjectName("buttonLoadGas")
        self.verticalLayout.addWidget(self.buttonLoadGas)
        self.buttonSaveGas = QtWidgets.QPushButton(self.frameGasFile)
        self.buttonSaveGas.setMinimumSize(QtCore.QSize(77, 32))
        self.buttonSaveGas.setObjectName("buttonSaveGas")
        self.verticalLayout.addWidget(self.buttonSaveGas)
        spacerItem3 = QtWidgets.QSpacerItem(20, 256, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2.addWidget(self.frameGasFile)
        self.tableViewGas = QtWidgets.QTableView(self.frame)
        self.tableViewGas.setMinimumSize(QtCore.QSize(325, 330))
        self.tableViewGas.setObjectName("tableViewGas")
        self.horizontalLayout_2.addWidget(self.tableViewGas)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsViewGas = QtWidgets.QGraphicsView(self.frame_2)
        self.graphicsViewGas.setMinimumSize(QtCore.QSize(300, 220))
        self.graphicsViewGas.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsViewGas.setObjectName("graphicsViewGas")
        self.verticalLayout_2.addWidget(self.graphicsViewGas)
        self.labelStatusMessageGas = QtWidgets.QLabel(self.frame_2)
        self.labelStatusMessageGas.setMinimumSize(QtCore.QSize(350, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelStatusMessageGas.setFont(font)
        self.labelStatusMessageGas.setObjectName("labelStatusMessageGas")
        self.verticalLayout_2.addWidget(self.labelStatusMessageGas)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_12.addWidget(self.frame)
        self.stackedWidgetMain.addWidget(self.pageGasComposition)
        self.pageScenario = QtWidgets.QWidget()
        self.pageScenario.setObjectName("pageScenario")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.pageScenario)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_6 = QtWidgets.QFrame(self.pageScenario)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(1021, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_11.addWidget(self.frame_6)
        self.frame_14 = QtWidgets.QFrame(self.pageScenario)
        self.frame_14.setStyleSheet("QGroupBox {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;    \n"
"    font-weight: bold; \n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid black;\n"
"    border-radius: 2px;        \n"
"    margin-left: 5px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"#groupBoxBlowPipe {\n"
"    border: 0px solid black;\n"
"    border-radius: 5px;    \n"
"    font-weight: bold; \n"
"    font-size: 12px;\n"
"}\n"
"\n"
"#groupBoxValve {\n"
"    border: 0px solid black;\n"
"    border-radius: 5px;    \n"
"    font-weight: bold; \n"
"    font-size: 12px;\n"
"}\n"
"\n"
"#groupBoxOrifice {\n"
"    border: 0px solid black;\n"
"    border-radius: 5px;    \n"
"    font-weight: bold; \n"
"    font-size: 12px;\n"
"}")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_5 = QtWidgets.QFrame(self.frame_14)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.groupBoxPipe = QtWidgets.QGroupBox(self.frame_5)
        self.groupBoxPipe.setObjectName("groupBoxPipe")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBoxPipe)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_8 = QtWidgets.QFrame(self.groupBoxPipe)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEditPipeLength = QtWidgets.QLineEdit(self.frame_8)
        self.lineEditPipeLength.setMinimumSize(QtCore.QSize(0, 18))
        self.lineEditPipeLength.setObjectName("lineEditPipeLength")
        self.gridLayout.addWidget(self.lineEditPipeLength, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_8)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_8)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.lineEditPipeDiameter = QtWidgets.QLineEdit(self.frame_8)
        self.lineEditPipeDiameter.setMinimumSize(QtCore.QSize(0, 18))
        self.lineEditPipeDiameter.setObjectName("lineEditPipeDiameter")
        self.gridLayout.addWidget(self.lineEditPipeDiameter, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_8)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 2, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.frame_8)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)
        self.lineEditStartPressure = QtWidgets.QLineEdit(self.frame_8)
        self.lineEditStartPressure.setMinimumSize(QtCore.QSize(0, 18))
        self.lineEditStartPressure.setObjectName("lineEditStartPressure")
        self.gridLayout.addWidget(self.lineEditStartPressure, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_8)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 3, 0, 1, 1)
        self.lineEditTemperature = QtWidgets.QLineEdit(self.frame_8)
        self.lineEditTemperature.setMinimumSize(QtCore.QSize(0, 18))
        self.lineEditTemperature.setObjectName("lineEditTemperature")
        self.gridLayout.addWidget(self.lineEditTemperature, 3, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_8)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_8)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 3, 2, 1, 1)
        self.verticalLayout_7.addWidget(self.frame_8)
        self.verticalLayout_10.addWidget(self.groupBoxPipe)
        spacerItem5 = QtWidgets.QSpacerItem(20, 232, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem5)
        self.horizontalLayout_10.addWidget(self.frame_5)
        self.frame_7 = QtWidgets.QFrame(self.frame_14)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBoxBlow = QtWidgets.QGroupBox(self.frame_7)
        self.groupBoxBlow.setObjectName("groupBoxBlow")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBoxBlow)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem6)
        self.groupBoxBlowPipe = QtWidgets.QGroupBox(self.groupBoxBlow)
        self.groupBoxBlowPipe.setMinimumSize(QtCore.QSize(0, 60))
        self.groupBoxBlowPipe.setObjectName("groupBoxBlowPipe")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBoxBlowPipe)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_16 = QtWidgets.QLabel(self.groupBoxBlowPipe)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_7.addWidget(self.label_16)
        self.lineEditBlowPipeDiameter = QtWidgets.QLineEdit(self.groupBoxBlowPipe)
        self.lineEditBlowPipeDiameter.setMinimumSize(QtCore.QSize(0, 18))
        self.lineEditBlowPipeDiameter.setObjectName("lineEditBlowPipeDiameter")
        self.horizontalLayout_7.addWidget(self.lineEditBlowPipeDiameter)
        self.label_17 = QtWidgets.QLabel(self.groupBoxBlowPipe)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_7.addWidget(self.label_17)
        self.verticalLayout_6.addWidget(self.groupBoxBlowPipe)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem7)
        self.groupBoxValve = QtWidgets.QGroupBox(self.groupBoxBlow)
        self.groupBoxValve.setMinimumSize(QtCore.QSize(0, 60))
        self.groupBoxValve.setObjectName("groupBoxValve")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBoxValve)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_18 = QtWidgets.QLabel(self.groupBoxValve)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_8.addWidget(self.label_18)
        self.lineEditValveKv = QtWidgets.QLineEdit(self.groupBoxValve)
        self.lineEditValveKv.setMinimumSize(QtCore.QSize(0, 18))
        self.lineEditValveKv.setObjectName("lineEditValveKv")
        self.horizontalLayout_8.addWidget(self.lineEditValveKv)
        self.label_19 = QtWidgets.QLabel(self.groupBoxValve)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_8.addWidget(self.label_19)
        self.verticalLayout_6.addWidget(self.groupBoxValve)
        self.frame_12 = QtWidgets.QFrame(self.groupBoxBlow)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButtonWithoutOrifice = QtWidgets.QRadioButton(self.frame_12)
        self.radioButtonWithoutOrifice.setObjectName("radioButtonWithoutOrifice")
        self.verticalLayout_3.addWidget(self.radioButtonWithoutOrifice)
        self.radioButtonWithOrifice = QtWidgets.QRadioButton(self.frame_12)
        self.radioButtonWithOrifice.setObjectName("radioButtonWithOrifice")
        self.verticalLayout_3.addWidget(self.radioButtonWithOrifice)
        self.verticalLayout_6.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.groupBoxBlow)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidgetOrifice = QtWidgets.QStackedWidget(self.frame_13)
        self.stackedWidgetOrifice.setObjectName("stackedWidgetOrifice")
        self.pageWithOrifice = QtWidgets.QWidget()
        self.pageWithOrifice.setObjectName("pageWithOrifice")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.pageWithOrifice)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBoxOrifice = QtWidgets.QGroupBox(self.pageWithOrifice)
        self.groupBoxOrifice.setObjectName("groupBoxOrifice")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBoxOrifice)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_20 = QtWidgets.QLabel(self.groupBoxOrifice)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_9.addWidget(self.label_20)
        self.lineEditOrificeDiameter = QtWidgets.QLineEdit(self.groupBoxOrifice)
        self.lineEditOrificeDiameter.setMinimumSize(QtCore.QSize(0, 18))
        self.lineEditOrificeDiameter.setObjectName("lineEditOrificeDiameter")
        self.horizontalLayout_9.addWidget(self.lineEditOrificeDiameter)
        self.label_21 = QtWidgets.QLabel(self.groupBoxOrifice)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_9.addWidget(self.label_21)
        self.verticalLayout_4.addWidget(self.groupBoxOrifice)
        self.stackedWidgetOrifice.addWidget(self.pageWithOrifice)
        self.pageWithoutOrifice = QtWidgets.QWidget()
        self.pageWithoutOrifice.setObjectName("pageWithoutOrifice")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.pageWithoutOrifice)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        spacerItem8 = QtWidgets.QSpacerItem(20, 59, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem8)
        self.stackedWidgetOrifice.addWidget(self.pageWithoutOrifice)
        self.verticalLayout_5.addWidget(self.stackedWidgetOrifice)
        self.verticalLayout_6.addWidget(self.frame_13)
        self.verticalLayout_9.addWidget(self.groupBoxBlow)
        spacerItem9 = QtWidgets.QSpacerItem(20, 11, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem9)
        self.horizontalLayout_10.addWidget(self.frame_7)
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.groupBoxSim = QtWidgets.QGroupBox(self.frame_15)
        self.groupBoxSim.setObjectName("groupBoxSim")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBoxSim)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_11 = QtWidgets.QFrame(self.groupBoxSim)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_23 = QtWidgets.QLabel(self.frame_11)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 0, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.frame_11)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 0, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.frame_11)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 1, 0, 1, 1)
        self.lineEditSimTimeInterval = QtWidgets.QLineEdit(self.frame_11)
        self.lineEditSimTimeInterval.setMinimumSize(QtCore.QSize(0, 18))
        self.lineEditSimTimeInterval.setObjectName("lineEditSimTimeInterval")
        self.gridLayout_2.addWidget(self.lineEditSimTimeInterval, 0, 1, 1, 1)
        self.lineEditSimTimestep = QtWidgets.QLineEdit(self.frame_11)
        self.lineEditSimTimestep.setMinimumSize(QtCore.QSize(0, 18))
        self.lineEditSimTimestep.setObjectName("lineEditSimTimestep")
        self.gridLayout_2.addWidget(self.lineEditSimTimestep, 1, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.frame_11)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 1, 2, 1, 2)
        self.verticalLayout_8.addWidget(self.frame_11)
        self.verticalLayout_18.addWidget(self.groupBoxSim)
        spacerItem10 = QtWidgets.QSpacerItem(20, 144, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem10)
        self.horizontalLayout_10.addWidget(self.frame_15)
        self.frame_15.raise_()
        self.frame_7.raise_()
        self.frame_5.raise_()
        self.verticalLayout_11.addWidget(self.frame_14)
        self.frame_14.raise_()
        self.frame_6.raise_()
        self.stackedWidgetMain.addWidget(self.pageScenario)
        self.pageResults = QtWidgets.QWidget()
        self.pageResults.setObjectName("pageResults")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.pageResults)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_9 = QtWidgets.QFrame(self.pageResults)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 45))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.frame_9)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        spacerItem11 = QtWidgets.QSpacerItem(1011, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem11)
        self.verticalLayout_14.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.pageResults)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.graphicsViewResultsPressure = PlotWidget(self.frame_10)
        self.graphicsViewResultsPressure.setMinimumSize(QtCore.QSize(0, 100))
        self.graphicsViewResultsPressure.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsViewResultsPressure.setObjectName("graphicsViewResultsPressure")
        self.gridLayout_3.addWidget(self.graphicsViewResultsPressure, 0, 0, 1, 1)
        self.graphicsViewResultsLinepack = PlotWidget(self.frame_10)
        self.graphicsViewResultsLinepack.setMinimumSize(QtCore.QSize(0, 100))
        self.graphicsViewResultsLinepack.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsViewResultsLinepack.setObjectName("graphicsViewResultsLinepack")
        self.gridLayout_3.addWidget(self.graphicsViewResultsLinepack, 0, 1, 1, 1)
        self.graphicsViewResultsFlow = PlotWidget(self.frame_10)
        self.graphicsViewResultsFlow.setMinimumSize(QtCore.QSize(0, 100))
        self.graphicsViewResultsFlow.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsViewResultsFlow.setObjectName("graphicsViewResultsFlow")
        self.gridLayout_3.addWidget(self.graphicsViewResultsFlow, 1, 0, 1, 1)
        self.graphicsViewResultsVelocity = PlotWidget(self.frame_10)
        self.graphicsViewResultsVelocity.setMinimumSize(QtCore.QSize(0, 100))
        self.graphicsViewResultsVelocity.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsViewResultsVelocity.setObjectName("graphicsViewResultsVelocity")
        self.gridLayout_3.addWidget(self.graphicsViewResultsVelocity, 1, 1, 1, 1)
        self.verticalLayout_14.addWidget(self.frame_10)
        self.groupBox_11 = QtWidgets.QGroupBox(self.pageResults)
        self.groupBox_11.setMinimumSize(QtCore.QSize(0, 60))
        self.groupBox_11.setStyleSheet("QGroupBox {\n"
"    border: 2px solid black;\n"
"    border-radius: 5px;    \n"
"    font-weight: bold; \n"
"    font-size: 12px;\n"
"}")
        self.groupBox_11.setObjectName("groupBox_11")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_8 = QtWidgets.QLabel(self.groupBox_11)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_12.addWidget(self.label_8)
        self.labelResCritical = QtWidgets.QLabel(self.groupBox_11)
        self.labelResCritical.setObjectName("labelResCritical")
        self.horizontalLayout_12.addWidget(self.labelResCritical)
        spacerItem12 = QtWidgets.QSpacerItem(365, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem12)
        self.label_9 = QtWidgets.QLabel(self.groupBox_11)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_12.addWidget(self.label_9)
        self.labelResSubCritical = QtWidgets.QLabel(self.groupBox_11)
        self.labelResSubCritical.setObjectName("labelResSubCritical")
        self.horizontalLayout_12.addWidget(self.labelResSubCritical)
        spacerItem13 = QtWidgets.QSpacerItem(364, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem13)
        self.label_22 = QtWidgets.QLabel(self.groupBox_11)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_12.addWidget(self.label_22)
        self.labelResTotal = QtWidgets.QLabel(self.groupBox_11)
        self.labelResTotal.setObjectName("labelResTotal")
        self.horizontalLayout_12.addWidget(self.labelResTotal)
        self.verticalLayout_14.addWidget(self.groupBox_11)
        self.stackedWidgetMain.addWidget(self.pageResults)
        self.verticalLayout_15.addWidget(self.stackedWidgetMain)
        self.verticalLayout_16.addWidget(self.frameMain)
        self.frameBottom = QtWidgets.QFrame(self.centralwidget)
        self.frameBottom.setMinimumSize(QtCore.QSize(0, 52))
        self.frameBottom.setStyleSheet("QPushButton{\n"
"    border: 1px solid black;\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #696a6a, stop: 1 #212222);\n"
"    border-radius: 5px;    \n"
"    font-weight: bold; \n"
"    font-size: 12px;\n"
"    color: white;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4a42ec, stop: 1 #0d04ba);\n"
"}\n"
"\n"
"#labelStatusMessageSim {\n"
"    min-width: 180px;\n"
"    background: white;\n"
"    font-size: 15px;\n"
"    color: blue;\n"
"}")
        self.frameBottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBottom.setObjectName("frameBottom")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frameBottom)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.frameBottom)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.buttonStartSim = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonStartSim.sizePolicy().hasHeightForWidth())
        self.buttonStartSim.setSizePolicy(sizePolicy)
        self.buttonStartSim.setMinimumSize(QtCore.QSize(142, 27))
        self.buttonStartSim.setObjectName("buttonStartSim")
        self.horizontalLayout_4.addWidget(self.buttonStartSim)
        self.labelStatusMessageSim = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelStatusMessageSim.sizePolicy().hasHeightForWidth())
        self.labelStatusMessageSim.setSizePolicy(sizePolicy)
        self.labelStatusMessageSim.setMinimumSize(QtCore.QSize(180, 25))
        self.labelStatusMessageSim.setObjectName("labelStatusMessageSim")
        self.horizontalLayout_4.addWidget(self.labelStatusMessageSim)
        self.horizontalLayout_5.addWidget(self.frame_4)
        spacerItem14 = QtWidgets.QSpacerItem(657, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        self.verticalLayout_16.addWidget(self.frameBottom)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidgetMain.setCurrentIndex(1)
        self.stackedWidgetOrifice.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.buttonGasComposition.setText(_translate("MainWindow", "   Gas composition   "))
        self.buttonScenario.setText(_translate("MainWindow", "   Scenario   "))
        self.buttonResults.setText(_translate("MainWindow", "   Results   "))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Gas composition</span></p></body></html>"))
        self.buttonNewGas.setText(_translate("MainWindow", "New"))
        self.buttonLoadGas.setText(_translate("MainWindow", "Load"))
        self.buttonSaveGas.setText(_translate("MainWindow", "Save"))
        self.labelStatusMessageGas.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">xxx StatusMessageGasComposition xxx</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Scenario</span></p></body></html>"))
        self.groupBoxPipe.setTitle(_translate("MainWindow", "Pipe"))
        self.label_5.setText(_translate("MainWindow", "Length"))
        self.label_10.setText(_translate("MainWindow", "m"))
        self.label_6.setText(_translate("MainWindow", "Diameter"))
        self.label_11.setText(_translate("MainWindow", "mm"))
        self.label_12.setText(_translate("MainWindow", "Pressure"))
        self.label_13.setText(_translate("MainWindow", "Temperature"))
        self.label_14.setText(_translate("MainWindow", "bar"))
        self.label_15.setText(_translate("MainWindow", "°C"))
        self.groupBoxBlow.setTitle(_translate("MainWindow", "Blowdown system"))
        self.groupBoxBlowPipe.setTitle(_translate("MainWindow", "Pipe"))
        self.label_16.setText(_translate("MainWindow", "Diameter"))
        self.label_17.setText(_translate("MainWindow", "mm"))
        self.groupBoxValve.setTitle(_translate("MainWindow", "Valve"))
        self.label_18.setText(_translate("MainWindow", "Kv value"))
        self.label_19.setText(_translate("MainWindow", "m³/h"))
        self.radioButtonWithoutOrifice.setText(_translate("MainWindow", "without orifice"))
        self.radioButtonWithOrifice.setText(_translate("MainWindow", "with orifice"))
        self.groupBoxOrifice.setTitle(_translate("MainWindow", "Orifice"))
        self.label_20.setText(_translate("MainWindow", "Diameter"))
        self.label_21.setText(_translate("MainWindow", "mm"))
        self.groupBoxSim.setTitle(_translate("MainWindow", "Simulation"))
        self.label_23.setText(_translate("MainWindow", "Time interval"))
        self.label_24.setText(_translate("MainWindow", "s"))
        self.label_25.setText(_translate("MainWindow", "Time step"))
        self.label_26.setText(_translate("MainWindow", "s"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Results</span></p></body></html>"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Blowdown times"))
        self.label_8.setText(_translate("MainWindow", "overcritical:"))
        self.labelResCritical.setText(_translate("MainWindow", "xxxxxxxxxx"))
        self.label_9.setText(_translate("MainWindow", "subcritical:"))
        self.labelResSubCritical.setText(_translate("MainWindow", "xxxxxxxxxx"))
        self.label_22.setText(_translate("MainWindow", "total:"))
        self.labelResTotal.setText(_translate("MainWindow", "xxxxxxxxxx"))
        self.buttonStartSim.setText(_translate("MainWindow", "Run Simulation"))
        self.labelStatusMessageSim.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">xxx StatusMessage xxx</span></p></body></html>"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

