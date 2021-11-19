

from PyQt5.QtCore import Qt, QSize

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
    QListWidget, QLineEdit, QMessageBox, QInputDialog, QHBoxLayout

from PyQt5.QtGui import QPixmap, QIcon, QPalette, QImage, QBrush
from PyQt5 import QtCore


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(700, 485)
        self.old_pos = None

        name_image = QImage("ThemeStandard/Background.jpg")
        size_image = name_image.scaled(QSize(700, 485))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(size_image))
        self.setPalette(palette)

        self.inputValue = QLineEdit(self)
        self.inputValue.move(340, 70)
        self.inputValue.resize(350, 35)

        self.listWidget = QListWidget(self)
        self.listWidget.move(340, 110)
        self.listWidget.resize(350, 370)

        self.setStyleSheet("""QListWidget{
                            background: rgb(61, 61, 61);
                            border: 3px solid white;
                            color: rgb(255, 255, 255);
                        }""")

        self.inputValue.setStyleSheet("""QLineEdit{
                            background: rgb(61, 61, 61);
                            border: 3px solid white;
                            color: rgb(255, 255, 255;)
                        }""")

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeStandard/CloseButton.jpg'))

        self.closeButton = QPushButton(self)
        self.closeButton.move(660, -1)
        self.closeButton.resize(41, 25)
        self.closeButton.clicked.connect(self.closeProgram)
        self.closeButton.setIcon(icon)
        self.closeButton.setIconSize(QtCore.QSize(40, 40))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeStandard/RollDownButton.jpg'))
        self.rollButton = QPushButton(self)
        self.rollButton.move(632, -1)
        self.rollButton.resize(30, 25)
        self.rollButton.clicked.connect(self.rollDownProgram)
        self.rollButton.setIcon(icon)
        self.rollButton.setIconSize(QtCore.QSize(40, 40))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeStandard/WriteButton.jpg'))
        self.writeButton = QPushButton(self)
        self.writeButton.resize(115, 40)
        self.writeButton.move(339, 27)
        self.writeButton.clicked.connect(self.write_value)
        self.writeButton.setIcon(icon)
        self.writeButton.setIconSize(QtCore.QSize(125, 50))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeStandard/EditButton.jpg'))
        self.editButton = QPushButton(self)
        self.editButton.resize(115, 40)
        self.editButton.move(457, 27)
        self.editButton.clicked.connect(self.edit_value)
        self.editButton.setIcon(icon)
        self.editButton.setIconSize(QtCore.QSize(125, 50))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeStandard/DeleteButton.jpg'))
        self.deleteButton = QPushButton(self)
        self.deleteButton.resize(115, 40)
        self.deleteButton.move(575, 27)
        self.deleteButton.clicked.connect(self.delete_value)
        self.deleteButton.setIcon(icon)
        self.deleteButton.setIconSize(QtCore.QSize(125, 50))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeStandard/HistoryButton.jpg'))
        self.historyButton = QPushButton(self)
        self.historyButton.move(170, 27)
        self.historyButton.resize(115, 40)
        self.historyButton.setIcon(icon)
        self.historyButton.setIconSize(QtCore.QSize(125, 50))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeStandard/ThemeButton.jpg'))
        self.themeButton = QPushButton(self)
        self.themeButton.move(53, 27)
        self.themeButton.resize(115, 40)
        self.themeButton.setIcon(icon)
        self.themeButton.setIconSize(QtCore.QSize(125, 50))
        self.themeButton.clicked.connect(self.themes)
        self.count = 0

        # self.tableWidget = QtWidgets.QTableView(self.LOG) БД <<<<<<<<<<<<<<<<<<< БД

        self.layout = QHBoxLayout(self)

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeStandard/Theme_1.jpg'))
        self.theme1Button = QPushButton(self)
        self.theme1Button.move(53, 77)
        self.theme1Button.resize(190, 40)
        self.theme1Button.setIcon(icon)
        self.theme1Button.setIconSize(QtCore.QSize(230, 60))
        self.theme1Button.clicked.connect(self.changeTheme_1)
        self.theme1Button.hide()

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeStandard/Theme_2.jpg'))
        self.theme2Button = QPushButton(self)
        self.theme2Button.move(53, 120)
        self.theme2Button.resize(190, 40)
        self.theme2Button.setIcon(icon)
        self.theme2Button.setIconSize(QtCore.QSize(230, 60))
        self.theme2Button.clicked.connect(self.changeTheme_2)
        self.theme2Button.hide()

    def themes(self):
        self.count += 1
        if self.count % 2 != 0:
            self.theme1Button.show()
            self.theme2Button.show()
        else:
            self.theme1Button.hide()
            self.theme2Button.hide()

    def rollDownProgram(self):
        self.showMinimized()

    def delete_value(self):
        remove_item = self.listWidget.selectedItems()
        if not remove_item:
            return
        for item in remove_item:
            self.listWidget.takeItem(self.listWidget.row(item))

    def edit_value(self):
        if self.inputValue.text():
            self.listWidget.currentItem().setText(self.inputValue.text())
            self.inputValue.clear()
        else:
            dialog = QMessageBox(QMessageBox.Critical,
                                 "Предупреждение",
                                 "Пустое поле ввода, невозможно редактировать заметку",
                                 buttons=QMessageBox.Ok,
                                 parent=self)
            dialog.exec()

    def write_value(self):
        if self.inputValue.text():
            self.listWidget.addItem(self.inputValue.text())
            self.inputValue.clear()
        else:
            dialog = QMessageBox(QMessageBox.Critical,
                                 "Предупреждение",
                                 "Пустое поле ввода, невозможно создать заметку",
                                 buttons=QMessageBox.Ok,
                                 parent=self)
            dialog.exec()
            self.inputValue.setFocus()

    def closeProgram(self):
        self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.pos()

    # вызывается при отпускании кнопки мыши
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None

    # вызывается всякий раз, когда мышь перемещается
    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)

    def changeTheme_1(self):
        name_image = QImage("ThemeStandard/Background.jpg")
        size_image = name_image.scaled(QSize(700, 485))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(size_image))
        self.setPalette(palette)

        self.listWidget.setStyleSheet("""QListWidget{
                            background: rgb(61, 61, 61);
                            border: 3px solid white;
                            color: rgb(255, 255, 255);
                        }""")

        self.inputValue.setStyleSheet("""QLineEdit{
                            background: rgb(61, 61, 61);
                            border: 3px solid white;
                            color: rgb(255, 255, 255;)
                        }""")

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeStandard/CloseButton.jpg'))
        self.closeButton.setIcon(icon)
        self.closeButton.setIconSize(QtCore.QSize(40, 40))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeStandard/RollDownButton.jpg'))
        self.rollButton.setIcon(icon)
        self.rollButton.setIconSize(QtCore.QSize(40, 40))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeStandard/WriteButton.jpg'))
        self.writeButton.setIcon(icon)
        self.writeButton.setIconSize(QtCore.QSize(125, 50))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeStandard/EditButton.jpg'))
        self.editButton.setIcon(icon)
        self.editButton.setIconSize(QtCore.QSize(125, 50))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeStandard/DeleteButton.jpg'))
        self.deleteButton.setIcon(icon)
        self.deleteButton.setIconSize(QtCore.QSize(125, 50))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeStandard/HistoryButton.jpg'))
        self.historyButton.setIcon(icon)
        self.historyButton.setIconSize(QtCore.QSize(125, 50))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeStandard/ThemeButton.jpg'))
        self.themeButton.setIcon(icon)
        self.themeButton.setIconSize(QtCore.QSize(125, 50))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeStandard/Theme_1.jpg'))
        self.theme1Button.setIcon(icon)
        self.theme1Button.setIconSize(QtCore.QSize(230, 60))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeStandard/Theme_2.jpg'))
        self.theme2Button.setIcon(icon)
        self.theme2Button.setIconSize(QtCore.QSize(230, 60))

    def changeTheme_2(self):
        name_image = QImage("ThemeForest/Background.jpg")
        size_image = name_image.scaled(QSize(700, 485))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(size_image))
        self.setPalette(palette)

        self.inputValue.setStyleSheet("""QLineEdit{
                                    background: rgb(40, 127, 127);
                                    border: 3px solid rgb(12, 93, 93);
                                    color: rgb(255, 255, 255;)
                                }""")

        self.listWidget.setStyleSheet("""QListWidget{
                                    background: rgb(40, 127, 127);
                                    border: 3px solid rgb(12, 93, 93);
                                    color: rgb(255, 255, 255;
                                    font: "ThemeForest/font/Comic_Cat";)
                                }""")

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeForest/CloseButton.jpg'))
        self.closeButton.setIcon(icon)
        self.closeButton.setIconSize(QtCore.QSize(38, 38))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeForest/RollDownButton.jpg'))
        self.rollButton.setIcon(icon)
        self.rollButton.setIconSize(QtCore.QSize(40, 40))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeForest/WriteButton.jpg'))
        self.writeButton.setIcon(icon)
        self.writeButton.setIconSize(QtCore.QSize(125, 50))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeForest/EditButton.jpg'))
        self.editButton.setIcon(icon)
        self.editButton.setIconSize(QtCore.QSize(125, 50))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeForest/DeleteButton.jpg'))
        self.deleteButton.setIcon(icon)
        self.deleteButton.setIconSize(QtCore.QSize(125, 50))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeForest/HistoryButton.jpg'))
        self.historyButton.setIcon(icon)
        self.historyButton.setIconSize(QtCore.QSize(125, 50))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeForest/ThemeButton.jpg'))
        self.themeButton.setIcon(icon)
        self.themeButton.setIconSize(QtCore.QSize(125, 50))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeForest/Theme_1.jpg'))
        self.theme1Button.setIcon(icon)
        self.theme1Button.setIconSize(QtCore.QSize(230, 60))

        icon = QIcon()
        icon.addPixmap(QPixmap('ThemeForest/Theme_2.jpg'))
        self.theme2Button.setIcon(icon)
        self.theme2Button.setIconSize(QtCore.QSize(230, 60))


if __name__ == '__main__':
    app = QApplication([])
    app.setStyleSheet("QListWidget, QLineEdit{font-size: 18pt;}")
    w = Widget()
    w.show()
    app.exec()
