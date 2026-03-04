import picture_process
import sys
import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as QtCore
import SubEditWindow

class my_button(QtWidgets.QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet('''
            QPushButton {
                background-color: #FF5733;
                color: white;
                font-size: 18px;
                font-family: "Consolas", "Courier New", monospace;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #C70039;
            }''')
class SelectableButtonGroup(QtWidgets.QWidget):
    def __init__(self, texts, parent=None):
        super().__init__(parent)
        self.initUI(texts)
        
    def initUI(self, texts):
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        
        self.button_group = QtWidgets.QButtonGroup(self)
        self.button_group.setExclusive(True)  # 确保只能选中一个
        
        btn_layout = QtWidgets.QHBoxLayout()
        
        button_texts = texts
        
        # 创建按钮并添加到组中
        for i, text in enumerate(button_texts):
            btn = QtWidgets.QPushButton(text)
            btn.setCheckable(True)  # 使按钮可选中
            btn.setStyleSheet("""
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
            }
            QPushButton:checked {
                    background-color: #4CAF50;
                    color: white;
                }
            """)
            
            self.button_group.addButton(btn, i)  # 给每个按钮一个ID
            btn_layout.addWidget(btn)
        
        # 默认选中第一个按钮
        if button_texts:
            self.button_group.button(0).setChecked(True)
        
        layout.addLayout(btn_layout)
        
class PictureProcessWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Picture Process")
        self.setGeometry(200, 250, 1300, 800)
        self.setStyleSheet('''
            QMainWindow {
                background-color: #9BBCFF;
            }
            QMainWindow::title {
                color: #421EFF;
                font-size: 18px;
            }''')
        self.start()

    def start(self):
        type = [0, 0, 0]
        # 设置 centralWidget
        centeral_widget = QtWidgets.QWidget()
        self.setCentralWidget(centeral_widget)
        button_quit = my_button("Quit", self)
        button_quit.setGeometry(1200, 20, 80, 30)
        button_quit.clicked.connect(self.close)
        line_edit = QtWidgets.QLineEdit(self)
        line_edit.setGeometry(320, 150, 600, 50)
        line_edit.setPlaceholderText("Enter image path")
        line_edit.setAlignment(QtCore.Qt.AlignCenter)
        line_edit.setStyleSheet('''
            QLineEdit {
                background-color: white;
                color: #421EFF;
                font-size: 22px;
                font-family: "Consolas", "Courier New", monospace;
                border-radius: 5px;
            }''')
        

        button_img = my_button("Select Img", self)
        button_img.setGeometry(400, 300, 200, 50)
        test_binary_model = QtWidgets.QLabel("Binary Model", self)
        test_binary_model.setGeometry(320, 370, 200, 60)
        test_eq_model = QtWidgets.QLabel("If GussianBur", self)
        test_eq_model.setGeometry(320, 470, 200, 60)
        test_bw_model = QtWidgets.QLabel("If reverse", self)
        test_bw_model.setGeometry(320, 570, 200, 60)

        button_img.clicked.connect(lambda: self.find_image(line_edit))
        button_binary_type_group = SelectableButtonGroup(["Global", "Adaptive"], self)
        button_binary_type_group.setGeometry(320, 400, 600, 60)
        button_binary_type_group.button_group.buttonClicked.connect(lambda: type.__setitem__(1, button_binary_type_group.button_group.checkedId()))
        button_eq_type_group = SelectableButtonGroup(["No", "Yes"], self)
        button_eq_type_group.setGeometry(320, 500, 600, 60)
        button_eq_type_group.button_group.buttonClicked.connect(lambda: type.__setitem__(2, button_eq_type_group.button_group.checkedId()))
        button_bw_type_group = SelectableButtonGroup(["No", "Yes"], self)
        button_bw_type_group.setGeometry(320, 600, 600, 60)
        button_bw_type_group.button_group.buttonClicked.connect(lambda: type.__setitem__(0, button_bw_type_group.button_group.checkedId()))
        
        button_start = my_button("Start", self)
        button_start.setGeometry(620, 300, 200, 50)
        button_start.clicked.connect(lambda: picture_process.connected_component_labeling(line_edit.text(), type))
        self.show()
    def find_image(self, line_edit):
        file_path = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image File", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        line_edit.setText(file_path[0])

