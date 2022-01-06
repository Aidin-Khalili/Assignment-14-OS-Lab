from functools import partial
import math
import PySide6.QtCore
import PySide6.QtWidgets 
import PySide6.QtUiTools 

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('Screencalculator.ui')
        self.ui.show()
        self.ui.zero_btn.clicked.connect(partial(self.function_NumX, 0))
        self.ui.one_btn.clicked.connect(partial(self.function_NumX, 1))
        self.ui.two_btn.clicked.connect(partial(self.function_NumX, 2))
        self.ui.three_btn.clicked.connect(partial(self.function_NumX, 3))
        self.ui.four_btn.clicked.connect(partial(self.function_NumX, 4))
        self.ui.five_btn.clicked.connect(partial(self.function_NumX, 5))
        self.ui.six_btn.clicked.connect(partial(self.function_NumX, 6))
        self.ui.seven_btn.clicked.connect(partial(self.function_NumX, 7))
        self.ui.eight_btn.clicked.connect(partial(self.function_NumX, 8))
        self.ui.nine_btn.clicked.connect(partial(self.function_NumX, 9))
        self.ui.sum_btn.clicked.connect(partial(self.get_num, '+'))
        self.ui.sub_btn.clicked.connect(partial(self.get_num, '-'))
        self.ui.mul_btn.clicked.connect(partial(self.get_num, '*'))
        self.ui.div_btn.clicked.connect(partial(self.get_num, '/'))
        self.ui.sin_btn.clicked.connect(partial(self.function_x, 'sin'))
        self.ui.cos_btn.clicked.connect(partial(self.function_x, 'cos'))
        self.ui.tan_btn.clicked.connect(partial(self.function_x, 'tan'))
        self.ui.cot_btn.clicked.connect(partial(self.function_x, 'cot'))
        self.ui.log_btn.clicked.connect(partial(self.function_x, 'log'))
        self.ui.sqrt_btn.clicked.connect(partial(self.function_x, 'sqrt'))
        self.ui.equal_btn.clicked.connect(self.equal)
        self.ui.c_btn.clicked.connect(self.reset)
        self.ui.decimal_btn.clicked.connect(self.decimal)
    def function_NumX(self, x):
        self.ui.Screen.setText(self.ui.Screen.text() + str(x))
    def get_num(self, op):
        try:
            if self.ui.Screen.text() != '':
                self.num1 = float(self.ui.Screen.text())
                self.ui.Screen.setText('')
                self.operator = op
        except:
            self.ui.Screen.setText('Error')
    def equal(self):
        try:
            if self.ui.Screen.text() != '':
                self.num2 = float(self.ui.Screen.text())
                if self.operator == '+':
                    result = self.num1 + self.num2
                elif self.operator == '-':
                    result = self.num1 - self.num2
                elif self.operator == '*':
                    result = self.num1 * self.num2
                elif self.operator == '/':
                    result = self.num1 / self.num2
                self.ui.Screen.setText(str(result))
        except:
            self.ui.Screen.setText('Error')
    def reset(self):
        self.ui.Screen.setText('')
    def decimal(self):
        if '.' not in self.ui.Screen.text() and self.ui.Screen.text() != '':
            self.ui.Screen.setText(self.ui.Screen.text() + '.')
    def function_x(self, sym):
        try:
            if self.ui.Screen.text() != '':
                text = radians(float(self.ui.Screen.text()))
                if sym == 'sin':
                    result = sin(text)
                elif sym == 'cos':
                    result = cos(text)
                elif sym == 'tan':
                    result = tan(text)
                elif sym == 'cot':
                    result = cos(text) / sin(text)
                elif sym == 'log':
                    result = log(float(self.ui.Screen.text()))
                elif sym == 'sqrt':
                    result = sqrt(float(self.ui.Screen.text()))

                result = round(result, 6)
                self.ui.Screen.setText(str(result))
        except:
            self.ui.Screen.setText('Error')

app = QApplication()
window = Calculator()
app.exec()