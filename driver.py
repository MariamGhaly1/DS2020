from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Trie import *
import os

MainUI,_ = loadUiType('DS_Searching_Engine.ui')

T = Trie()

class Main(QMainWindow , MainUI):
    main_path = ''

    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.tabWidget.tabBar().setVisible(False)
        self.progressBar.setVisible(False)
        self.label_2.setVisible(False)
        self.tabWidget.setCurrentIndex(0)
        self.progressBar.setValue(0)
        self.progressBar.setFormat('')
        self.pushButton.clicked.connect(self.upload)
        self.pushButton_2.clicked.connect(self.output)

    def upload(self):
        try:
            self.label_2.setVisible(True)
            names = QFileDialog.getOpenFileNames()
            self.main_path = "/".join(names[0][0].split('/')[:-1])
            n = len(names[0])
            self.progressBar.setMaximum(n)
            self.progressBar.setVisible(True)
            for i in range(n):
                with open(names[0][i], mode='r', encoding='utf-8') as f:
                    content = f.read()
                    name = os.path.basename(f.name)
                for word in content.split():
                    T.insert(word, name)
                self.progressBar.setValue(i+1)
            self.tabWidget.setCurrentIndex(1)
        except:
            QMessageBox.information(self, "Warning", "Something went wrong please try again !")

    def output(self):
        self.textEdit.clear()
        word = self.lineEdit.text()
        if word != '':
            try:
                files = T.find(word)
                if len(files) == 0:
                    self.textEdit.insertPlainText('This word does not exist !')
                    return
                for i in range(len(files)):
                    self.textEdit.insertPlainText(files[i])
                    self.textEdit.insertPlainText('\n')
                    path = os.path.join(self.main_path, files[i])
                    with open(path, mode='r', encoding='utf-8') as f:
                        x = f.read()
                    self.textEdit.insertPlainText(x)
                    self.textEdit.insertPlainText('\n_____________________________________________________\n\n')
            except:
                QMessageBox.information(self, "Warning", "Something went wrong please try again !")
        else:
            QMessageBox.information(self, "Warning", "Please enter a word to start search !")




def main():
    app=QApplication(sys.argv)
    window = Main()
    window.setWindowTitle('Search Engine')
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
