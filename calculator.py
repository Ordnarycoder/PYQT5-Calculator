import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 350, 400)  

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.screen = QLineEdit()
        self.screen.setAlignment(Qt.AlignRight)  
        self.screen.setReadOnly(True)  
        self.screen.setFixedHeight(50) 
        self.screen.setStyleSheet("""
            QLineEdit {
                background-color: #E0E0E0;
                font-size: 24px;
                border: 2px solid #A0A0A0;
                border-radius: 10px;
                padding: 5px;
            }
        """)
        self.layout.addWidget(self.screen)

        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        buttons = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
            '0': (3, 0), 'C': (3, 1), '=': (3, 2), '+': (3, 3),
        }

        for btn_text, pos in buttons.items():
            button = QPushButton(btn_text)
            button.setFixedSize(70, 70)  
            button.setStyleSheet("""
                QPushButton {
                    font-size: 20px;
                    border: 2px solid #A0A0A0;
                    border-radius: 10px;
                    background-color: #F0F0F0;
                }
                QPushButton:pressed {
                    background-color: #D0D0D0;
                }
            """)
            button.clicked.connect(self.button_clicked)
            self.grid_layout.addWidget(button, pos[0], pos[1])

    def button_clicked(self):
        button = self.sender()
        text = button.text()

        if text == 'C':
            self.screen.clear()
        elif text == '=':
            try:
                expression = self.screen.text()
                result = eval(expression)
                self.screen.setText(str(result))
            except Exception as e:
                self.screen.setText("Hata")
        else:
            self.screen.setText(self.screen.text() + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()

    app.setStyleSheet("""
        QWidget {
            font-family: Arial, sans-serif;
            background-color: #FFFFFF;
        }
    """)

    calculator.show()
    sys.exit(app.exec_())
