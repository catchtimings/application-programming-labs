import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from iterator import ImageIterator


class Ui_MainWindow(object):
    def setupUi(self, MainWindow) -> None:
        """
        Configuring the user interface of the main window
        """

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(888, 650)
        MainWindow.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(460, 520, 411, 71))
        self.next_button.setStyleSheet("background-color: rgb(149, 149, 149);\n"
"color: rgb(255, 255, 255);")
        self.next_button.setObjectName("next_button")
        self.openfile_button = QtWidgets.QPushButton(self.centralwidget)
        self.openfile_button.setEnabled(True)
        self.openfile_button.setGeometry(QtCore.QRect(20, 520, 411, 71))
        self.openfile_button.setStyleSheet("background-color: rgb(149, 149, 149);\n"
"color: white;")
        self.openfile_button.setObjectName("openfile_button")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(20, 10, 851, 491))
        self.image.setText("")
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 888, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.next_button, self.openfile_button)

        self.iterator = None
        self.csv_file = None

        self.next_button.clicked.connect(self.next_image)
        self.openfile_button.clicked.connect(self.open_file)

    def retranslateUi(self, MainWindow):
        """
        Setting the text on the controls in the interface
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Images"))
        self.next_button.setText(_translate("MainWindow", "NEXT"))
        self.openfile_button.setText(_translate("MainWindow", "OPEN FILE"))

    def open_file(self):
        """
        Open annotation file with path to images
        """
        try:
            file, _ = QFileDialog.getOpenFileName(
                parent=QtWidgets.QApplication.activeWindow(),
                caption="Select Annotation CSV File",
                directory="C:/Users/ct/Desktop",
                filter="CSV Files (*.csv)"
            )
            if file:
                self.csv_file = file
                if not QtCore.QFile.exists(file):
                    self.show_message_critical("File not found")
                self.iterator = ImageIterator(self.csv_file)
                self.next_image()
            else:
                self.show_message_critical("Please select a valid CSV file")
        except Exception:
            self.show_message_critical("An error occurred while opening the file")

    def next_image(self):
        """
        Display next image in main window
        """
        if not self.iterator:
            self.show_message_critical("Please load a CSV file first")
            return
        try:
            image_dir = next(self.iterator)
            pixmap = QPixmap(image_dir)
            if pixmap.isNull():
                self.show_message_warning("Image not found")
            else:
                self.image.setPixmap(pixmap)
        except StopIteration:
            self.show_message_warning("You've reached the end of the images. No more images to display.")
        except Exception:
            self.show_message_critical("Something went wrong...")

    def show_message_warning(self, text: str):
        """
        Warning window
        """
        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)
        msg.exec()

    def show_message_critical(self, text: str):
        """
        Critical window
        """
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        msg.exec()


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f'Something went wrong: {e}')