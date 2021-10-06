from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Annogram(object):
    def setupUi(self, Annogram):
        Annogram.setObjectName("Annogram")
        Annogram.resize(440, 400)
        Annogram.setStyleSheet("background-color: rgb(246, 255, 253);")
        self.centralwidget = QtWidgets.QWidget(Annogram)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 70, 100, 50))
        self.pushButton.setStyleSheet("background-color: rgb(188, 188, 188);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 70, 100, 50))
        self.pushButton_2.setStyleSheet("background-color: rgb(188, 188, 188);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 70, 100, 50))
        self.pushButton_3.setStyleSheet("background-color: rgb(150, 188, 188);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 400, 50))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 130, 400, 250))
        self.textBrowser.setObjectName("textBrowser")
        Annogram.setCentralWidget(self.centralwidget)

        self.retranslateUi(Annogram)
        QtCore.QMetaObject.connectSlotsByName(Annogram)

        self.add_functions()  # создадим функцию для обработки кнопок

    def retranslateUi(self, Annogram):
        _translate = QtCore.QCoreApplication.translate
        Annogram.setWindowTitle(_translate("Annogram", "Annograma"))
        self.pushButton.setText(_translate("Annogram", "Enter"))
        self.pushButton_2.setText(_translate("Annogram", "Clear"))
        self.pushButton_3.setText(_translate("Annogram", "Exit"))

    def add_functions(self):
        self.pushButton.clicked.connect(self.write_anogram)  # присваиваем кнопке Enter функцию write_anogram
        self.pushButton_2.clicked.connect(self.clear_anogram)  # присваиваем кнопке Clear функцию clear_anogram
        self.pushButton_3.clicked.connect(sys.exit)  # закрываем приложение при нажатии кнопки Exit

    def clear_anogram(self):
        self.textBrowser.clear()  # отчищаем поле вывода информации
        self.textEdit.clear()  # отчищаем поле ввода информации

    def write_anogram(self):
        with open('word_rus.txt', 'r', encoding='utf-8') as f:  # открываем на чтение txt файл со словарем
            self.list_word = f.read()
            self.list_word = list(self.list_word.split('\n'))  # переводим его в список и склеиваем через запятую

            try:  # обработка исключений на пустой ввод или ввод на английской раскладке
                self.anogram = self.textEdit.toPlainText()  # считываем анограму
                if ' ' in self.anogram:  # условие на разделение анограмы пробелами
                    self.textBrowser.append('Ошибка ввода данных, уберите пробел')
                else:
                    self.result = []
                    self.word = ''
                    for i in range(len(self.list_word)):
                        self.new_list = self.anogram
                        for self.item in self.list_word[i]:
                            if self.item in self.new_list:
                                self.word = self.word + self.item
                                self.new_list = self.new_list.replace(self.item, '', 1)
                        if len(self.word) == (len(self.list_word[i])):
                            self.result.append(self.word)
                        self.word = ''

                    self.max_length = len(max(self.result, key=len))

                    while self.max_length != 0:
                        self.fool_list = []
                        for i in range(len(self.result)):
                            if len(self.result[i]) == self.max_length:
                                self.fool_list.append(self.result[i])
                        if self.fool_list:
                            self.fool_list = str(self.fool_list)
                            self.textBrowser.append(f'{self.max_length} букв(ы)')
                            self.textBrowser.append(self.fool_list)
                            self.textBrowser.append('\n')
                        self.max_length -= 1
            except ValueError:
                self.textBrowser.append('Некоректный ввод, нажмите Clear и повторите попытку')
                self.textBrowser.append('Возможно пустой ввод или ввод на другой раскладке')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Annogram()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())