import PyQt5.QtWidgets as QtWidgets

class ErrorWindow(QtWidgets.QDialog):
    def __init__(self, error_message):
        super().__init__()
        self.setWindowTitle("Error")
        self.setGeometry(200, 250, 400, 200)
        self.setStyleSheet('''
            QDialog {
                background-color: #FFFFFF;
            }
            QDialog::title {
                color: #421EFF;
                font-size: 18px;
            }''')
        
        label = QtWidgets.QLabel(error_message, self)
        label.setGeometry(20, 20, 360, 100)
        label.setStyleSheet('''
            QLabel {
                color: #421EFF;
                font-size: 16px;
                font-family: "Consolas", "Courier New", monospace;
            }''')
        



