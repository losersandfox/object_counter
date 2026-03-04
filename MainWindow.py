import sys
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PictureProcessWindow

class MainWin():
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QMainWindow()
        self.window.setWindowTitle("Main Window")
        self.window.setGeometry(400, 450, 800, 600)
        self.window.setStyleSheet('''
            QMainWindow {
                background-color: #9BBCFF;
            }
            QMainWindow::title {
                color: #421EFF;
                font-size: 18px;
            }''')
        self.initUI()

    def initUI(self):
        # 设置 centralWidget
        central_widget = QtWidgets.QWidget()
        self.window.setCentralWidget(central_widget)

        # 添加按钮
        button_start = QtWidgets.QPushButton("Start", self.window)
        button_start.setGeometry(300, 400, 80, 30)
        button_start.setStyleSheet('''
            QPushButton {
                background-color: #FF5733;
                color: white;
                font-size: 16px;
                font-family: "Consolas", "Courier New", monospace;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #C70039;
            }''')
        button_start.clicked.connect(self.start_process)
        button_quit = QtWidgets.QPushButton("Quit", self.window)
        button_quit.setGeometry(400, 400, 80, 30)
        button_quit.setStyleSheet('''
            QPushButton {
                background-color: #FF5733;
                color: white;
                font-size: 16px;
                font-family: "Consolas", "Courier New", monospace;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #C70039;
            }''')
        button_quit.clicked.connect(self.window.close)

        # 添加标签
        label = QtWidgets.QLabel("Connected Component Labeling", self.window)
        label.setGeometry(110, 200, 600, 50)
        label.setStyleSheet('''
            QLabel {
                color: #421EFF;
                font-size: 30px;
                font-weight: bold;
                font-family: "Consolas", "Courier New", monospace;
            }
        ''')
        label.setAlignment(QtCore.Qt.AlignCenter)

        self.window.show()
        sys.exit(self.app.exec_())

    def start_process(self):
        self.window.hide()
        self.picture_process_window = PictureProcessWindow.PictureProcessWindow()
        
if(__name__ == "__main__"):
    window = MainWin()


