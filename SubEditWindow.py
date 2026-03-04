import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtGui as QtGui

class SubEditWindow(QtWidgets.QDialog):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setGeometry(200, 250, 400, 200)
        self.setStyleSheet('''
            QDialog {
                background-color: #FFFFFF;
            }
            QDialog::title {
                color: #421EFF;
                font-size: 18px;
            }''')
        layout = QtWidgets.QVBoxLayout()
        
        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setPlaceholderText("请输入正奇数(如3,5,7...)")
        self.line_edit.setValidator(QtGui.QIntValidator(1, 999))  # 限制只能输入1-99的整数
        
        button = QtWidgets.QPushButton("确定")
        button.setStyleSheet('''
            QPushButton {
                background-color: #D54DFF;
                color: white;
                font-size: 18px;
                font-family: "Consolas", "Courier New", monospace;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #C70039;
            }''')
        button.clicked.connect(self.accept)        
        layout.addWidget(self.line_edit)
        layout.addWidget(button)
        self.setLayout(layout)
    
    def getText(self):
        # 返回整数并确保是奇数
        if self.line_edit.text() == "":
            return 0
        value = int(self.line_edit.text())
        return value
