import sys
from PyQt5.QtWidgets import *
import math

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QGridLayout()
        self.line_edit = QLineEdit("")
        
        self.line_edit2 = QLineEdit("")

        main_layout.addWidget(self.line_edit, 0, 0, 1, 5)
        main_layout.addWidget(self.line_edit2, 1, 0, 1, 5)

        buttons = [
            {'name': 'CE', 'row': 2, 'col': 0, 'func': self.button_clear_entry_clicked},
            {'name': 'C', 'row': 2, 'col': 1, 'func': self.button_clear_clicked},
            {'name': '%', 'row': 2, 'col': 2, 'func': self.button_percent_clicked},
            {'name': '/', 'row': 2, 'col': 3, 'func': self.button_operation_clicked},
            {'name': '7', 'row': 3, 'col': 0, 'func': self.number_button_clicked},
            {'name': '8', 'row': 3, 'col': 1, 'func': self.number_button_clicked},
            {'name': '9', 'row': 3, 'col': 2, 'func': self.number_button_clicked},
            {'name': '*', 'row': 3, 'col': 3, 'func': self.button_operation_clicked},
            {'name': '4', 'row': 4, 'col': 0, 'func': self.number_button_clicked},
            {'name': '5', 'row': 4, 'col': 1, 'func': self.number_button_clicked},
            {'name': '6', 'row': 4, 'col': 2, 'func': self.number_button_clicked},
            {'name': '-', 'row': 4, 'col': 3, 'func': self.button_operation_clicked},
            {'name': '1', 'row': 5, 'col': 0, 'func': self.number_button_clicked},
            {'name': '2', 'row': 5, 'col': 1, 'func': self.number_button_clicked},
            {'name': '3', 'row': 5, 'col': 2, 'func': self.number_button_clicked},
            {'name': '+', 'row': 5, 'col': 3, 'func': self.button_operation_clicked},
            {'name': '0', 'row': 6, 'col': 0, 'func': self.number_button_clicked},
            {'name': '.', 'row': 6, 'col': 1, 'func': self.number_button_clicked},
            {'name': '=', 'row': 6, 'col': 2, 'func': self.button_equal_clicked},
            {'name': '1/x', 'row': 6, 'col': 3, 'func': self.button_reciprocal_clicked},
            {'name': 'x^2', 'row': 7, 'col': 0, 'func': self.button_square_clicked},
            {'name': '2√x', 'row': 7, 'col': 1, 'func': self.button_sqrt_clicked},
            {'name': 'Backspace', 'row': 7, 'col': 2, 'func': self.button_backspace_clicked}
        ]

        for button in buttons:
            btn = QPushButton(button['name'])
            btn.clicked.connect(lambda state, x=button['name'], func=button['func']: func(x))
            main_layout.addWidget(btn, button['row'], button['col'])

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.line_edit.text()
        equation += str(num)
        self.line_edit.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.line_edit.text()
        equation += operation
        self.line_edit.setText(equation)

    def button_equal_clicked(self,temp):
        equation = self.line_edit.text()
        equation = list(equation)
        print(equation)
        solution = float(equation[0])
        
        for i in range(1, len(equation), 2):
            operator = equation[i]
            number = float(equation[i+1])
            
            if operator == '+':
                solution += number
            elif operator == '-':
                solution -= number
            elif operator == '*':
                solution *= number
            elif operator == '/':
                solution /= number
            elif operator == '^':
                solution = math.pow(solution, number)
            elif operator == '√':
                solution = math.sqrt(solution)
            elif operator == '%':
                solution = solution % number
        
        self.line_edit2.setText(str(solution))

    def button_clear_clicked(self,temp):
        self.line_edit.setText("")

    def button_clear_entry_clicked(self, button):
        self.line_edit.setText("")

    def button_percent_clicked(self, button):
        equation = self.line_edit.text()
        equation += '%'
        self.line_edit.setText(equation)

    def button_reciprocal_clicked(self, button):
        equation = self.line_edit.text()
        if equation:
            try:
                solution = 1/float(equation)
                self.line_edit2.setText(str(solution))
            except Exception as e:
                self.line_edit2.setText("Error")
    def button_square_clicked(self, button):
        equation = self.line_edit.text()
        if equation:
            try:
                solution = float(equation) ** 2
                self.line_edit2.setText(str(solution))
            except Exception as e:
                self.line_edit2.setText("Error")
    
    def button_sqrt_clicked(self, button):
        equation = self.line_edit.text()
        if equation:
            try:
                solution = math.sqrt(float(equation))
                self.line_edit2.setText(str(solution))
            except Exception as e:
                self.line_edit2.setText("Error")
    
    def button_backspace_clicked(self,button):
        equation = self.line_edit.text()
        equation = equation[:-1]
        self.line_edit.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())