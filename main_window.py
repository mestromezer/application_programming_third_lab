import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

import iterator, dataset_copy, dataset_copy_random, dataset_to_csv

from PyQt5.QtCore import QThread, QObject

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.folderpath = str()
        
        while self.folderpath == "":
            try:
            
                self.folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
            
                paths_to_files = dataset_to_csv.get_paths_to_files(self.folderpath)

                dataset_to_csv.write_as_csv(paths_to_files)
            except: 
                print("Датасет не найден")
                self.folderpath = ""
            
        
        self.cOne = iterator.SimpleIterator("dataset_csv_first.csv", "1")
        self.cTwo = iterator.SimpleIterator("dataset_csv_first.csv", "2")
        self.cThree = iterator.SimpleIterator("dataset_csv_first.csv", "3")
        self.cFour = iterator.SimpleIterator("dataset_csv_first.csv", "4")
        self.cFive = iterator.SimpleIterator("dataset_csv_first.csv", "5")
        
        self.initUI()

    def Set_Label(self, x: int, y: int, text: str) -> None:
        """Этот метод устанавливает Label на форму по заданным координатам"""

        reviews = QLabel(text, self)
        reviews.resize(reviews.sizeHint())
        reviews.move(x, y)

    def Set_LineEdit(self, x: int, y: int) -> QTextEdit:
        """Этот метод устанавливает TextEdit на форму по заданным координатам"""

        reviews_edit = QTextEdit(' ', self)
        reviews_edit.resize(300, 500)
        reviews_edit.setReadOnly(True)
        reviews_edit.move(x, y)
        return reviews_edit

    def Set_Button(self, x: int, y: int, text: str, function) -> None:
        """Этот метод устанавливает PushButton на форму по заданным координатам"""

        btn = QPushButton(text, self)
        btn.resize(btn.sizeHint())
        btn.move(x, y)
        btn.clicked.connect(function)
        return btn

    def Set_Widgets(self) -> None:
        """Метод установки всех виджетов на форму"""
        self.Set_Label(0, 10, 'Одна звезда')
        self.Set_Label(300, 10, 'Две звезды')
        self.Set_Label(600, 10, 'Три звезды')
        self.Set_Label(900, 10, 'Четыре звезды')
        self.Set_Label(1200, 10, 'Пять звезды?')

        self.Line_Edit_cOne = self.Set_LineEdit(0, 90)
        self.Line_Edit_cTwo = self.Set_LineEdit(300, 90)
        self.Line_Edit_cThree = self.Set_LineEdit(600, 90)
        self.Line_Edit_cFour = self.Set_LineEdit(900, 90)
        self.Line_Edit_cFive= self.Set_LineEdit(1200, 90)

        self.Set_Button(
            0, 610, 'Next', self.On_Next_cOne)

        self.Set_Button(
            300, 610, 'Next', self.On_Next_cTwo)
       
        self.Set_Button(
            600, 610, 'Next', self.On_Next_cThree)
       
        self.Set_Button(
            900, 610, 'Next', self.On_Next_cFour)
       
        self.Set_Button(
            1200, 610, 'Next', self.On_Next_cFive)
        
        self.Set_Button(
            300, 700, 'Копия датасета', self.On_Create_Copy_Dataset_Button)
        
        self.Set_Button(
            900, 700, 'Перемешать данные в датасете', self.On_Create_Dataset_Random_Button)

        #self.Set_Button(
        #    1000, 90, 'Создать аннотацию для dataset', self.On_Create_Csv_Dataset_Button)
        #self.Set_Button(
        #    1000, 140, 'Создать новый dataset и аннотацию для него', self.On_Create_Copy_Dataset_Button)
        #self.Set_Button(
        #    1000, 190, 'Создать рандомный dataset и аннотацию для него', self.On_Create_Dataset_Random_Button)

    def On_Next_cOne(self) -> None:
        """Метод для отображения следующего хорошего отзыва"""
        path = self.cOne.__next__()
        file = open(path, 'r', encoding='utf-8')
            
        self.Line_Edit_cOne.setText(file.read())
            
    def On_Next_cTwo(self) -> None:
        """Метод для отображения следующего хорошего отзыва"""
        path = self.cTwo.__next__()
        file = open(path, 'r', encoding='utf-8')
            
        self.Line_Edit_cTwo.setText(file.read())
            
    def On_Next_cThree(self) -> None:
        """Метод для отображения следующего хорошего отзыва"""
        path = self.cThree.__next__()
        file = open(path, 'r', encoding='utf-8')
            
        self.Line_Edit_cThree.setText(file.read())
            
    def On_Next_cFour(self) -> None:
        """Метод для отображения следующего хорошего отзыва"""
        path = self.cFour.__next__()
        file = open(path, 'r', encoding='utf-8')
            
        self.Line_Edit_cFour.setText(file.read())
            
    def On_Next_cFive(self) -> None:
        """Метод для отображения следующего хорошего отзыва"""
        path = self.cFive.__next__()
        file = open(path, 'r', encoding='utf-8')
            
        self.Line_Edit_cFive.setText(file.read())
        

    def On_Create_Copy_Dataset_Button(self) -> None:
        """Метод для создания нового датасета и его csv-файла"""
        paths_to_files = dataset_copy.get_paths_to_files(self.folderpath)

        new_dataset_path = dataset_copy.copy_dataset(self.folderpath)

        dataset_copy.write_as_csv(new_dataset_path, paths_to_files)
        

    def On_Create_Dataset_Random_Button(self) -> None:
        """Метод для создания рандомного датасета и его csv-файла"""
        dataset_copy_random.create_copy(self.folderpath)

        path_new_dataset = dataset_copy_random.path_n_d()
        paths_to_files = dataset_copy_random.get_paths_to_files(path_new_dataset)

        dataset_copy_random.write_as_csv(path_new_dataset, paths_to_files)
        

    def initUI(self) -> None:

        self.resize(1400, 700)
        self.center()
        self.Set_Widgets()
        self.msg = QMessageBox()
        self.setWindowTitle('Отзывы')
        self.setWindowIcon(QIcon('web.png'))

    def center(self) -> None:

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def Init_Application() -> None:
    """создание оконного приложения"""
    app = QApplication(sys.argv)
    ex = Example()
    ex.setStyleSheet("background-image: url(background.jpg)")

    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    Init_Application()
