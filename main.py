from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QMessageBox, QLabel, QWidget, QLineEdit, QApplication, QMainWindow, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import QSize, QPoint, Qt, Signal
from PySide6.QtGui import QIcon
from variables import FILES_DIR
from styles import qss, setupTheme
from utils import isEmpty, isNumoDot, isNum, isValid
from math import pow, sqrt
import _text

class Botton(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        #self.setStyleSheet('font-size: 30px;')
        
class MainWindow(QMainWindow):
    upperPressed = Signal()
    downPressed = Signal()
    def __init__(self, layout_1, layout_2:QGridLayout, display:QLineEdit, label:QLabel) -> None:
        super().__init__()

        self.mais = -5
        self.i = -1
        self.pointIndex = 5
        self.otherIndex = 3
        self.labelIndex = -2
        self.labelList = []
        self.aI = 0
        self.resultsList = []
        self.eqList = []
        
        self.testList = [*range(15)]
        self.last = self.testList[-1]
        self.metade = int(len(self.testList) / 2)
        self.center = QWidget()
        self.addonsLayout = QHBoxLayout()
        self.labelLayout = QGridLayout()
        self.layout_ = QHBoxLayout()
        self.layoutPricipal = QVBoxLayout()
        self.display = display
        self.leftLayout = layout_1
        self.rightLayout = layout_2
        self.setConfig()

        self.upperPressed.connect(self.back_)
        self.downPressed.connect(self.next_)

        self.label_1 = self.makeLabel("-")
        self.label_2 = self.makeLabel("-")
        self.label_3 = self.makeLabel("-")
        self.label_4 = self.makeLabel("-")
        self.label_5 = self.makeLabel("-")

        self.b1 = Botton('🕒')
        self.b1.clicked.connect(self.isVis)
        self.b1.setFixedSize(35 ,35)
        self.b1.setStyleSheet('font-size: 20px;')
        self.b1.setProperty('cssClass', 'HButton')
        self.labelLayout.addWidget(label, 0, 0)

        self.layoutPricipal.addWidget(self.b1)
        self.layoutPricipal.addLayout(self.labelLayout)
        self.addToPrincipalLayout(self.display)
        self.layoutPricipal.addLayout(self.layout_)
        self.layout_.addLayout(self.leftLayout)
        self.layout_.addLayout(self.rightLayout)
        self.center.setLayout(self.layoutPricipal)
        self.setCentralWidget(self.center)

        self.addToLayout(self.leftLayout)
        self.addToLayout(self.rightLayout)

    def showEvent(self, event):
        super().showEvent(event)
        self.display.setFocus()
    
    def keyPressEvent(self, event: QKeyEvent) -> None:
        texto = event.text().strip()
        key = event.key()

        isUpper = key == 16777235
        isDown = key == 16777237

        if isUpper:
            self.upperPressed.emit()
            return event.ignore()
        
        if isDown:
            self.downPressed.emit()
            return event.ignore()
    
    def print_labels(self):
        # Obtendo todos os QLabel filhos da janela
        labels = self.findChildren(QLabel)

        print("Labels encontrados:")
        for label in labels:
            print(label.text())

    def makeLabel(self, text):
        label = QLabel(text)      
        
        if len(self.labelList) == 4:
            label.setStyleSheet("""
    QLabel {
        border: 2px solid #006400;  /* Contorno verde escuro */
        border-radius: 5px;        /* Bordas arredondadas */
        padding: 5px;              /* Espaço interno */
        color: #32CD32;;              /* Cor do texto */
        font-size: 19px;           /* Tamanho da fonte */
        font-weight: bold;         /* Negrito no texto */
    }
""")
            self.rightLayout.addWidget(label)
            label.hide()
            label.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.labelList.append(label)
            label.setFixedSize(335, 50)
            return

        self.rightLayout.addWidget(label)
        label.hide()
        label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.labelList.append(label)
        label.setFixedSize(335, 50)
        label.setStyleSheet('font-size: 15px;')

    def addToLayout(self, layout):
        self.layout_.addLayout(layout)
    
    def next_(self):

        for x, y in enumerate(window.resultsList):
            if window.resultsList[x] == None:
                window.resultsList.remove(y)

        if not self.labelList[0].isVisible():
            for l in self.labelList:
                l.show()
            self.resize(700, 450)
            self.setFixedSize(700, 450)
            self.display.setFocus()
            #self.leftLayout.frist_n = self.labelList[self.i]

        self.otherIndex = 3
        self.labelIndex = -2
        self.pointIndex = 5
        self.aI = 0
        self.i = -1
        
        for x, y in enumerate(self.labelList):
            if x == 4:
                y.setStyleSheet("""
    QLabel {
        border: 2px solid #006400;  /* Contorno verde escuro */
        border-radius: 5px;        /* Bordas arredondadas */
        padding: 5px;              /* Espaço interno */
        color: #32CD32;;              /* Cor do texto */
        font-size: 19px;           /* Tamanho da fonte */
        font-weight: bold;         /* Negrito no texto */
    }
""")
            else:
                y.setStyleSheet('font-size: 15px;')

    def back_(self):

        for x, y in enumerate(window.resultsList):
            if window.resultsList[x] == None:
                window.resultsList.remove(y)

        if not self.labelList[0].isVisible():
            
            for l in self.labelList:
                l.show()
            
            self.resize(700, 450)
            self.setFixedSize(700, 450)
            self.display.setFocus()
            #print(self.leftLayout.frist_n)
        
        try:
            self.leftLayout.frist_n = self.resultsList[self.i-1]
            print(self.leftLayout.frist_n)
            self.i -= 1
            self.labelList[-5].setText(f'{self.eqList[self.i-4]} = {self.resultsList[self.i-4]}')
            self.labelList[-4].setText(f'{self.eqList[self.i-3]} = {self.resultsList[self.i-3]}')
            self.labelList[-3].setText(f'{self.eqList[self.i-2]} = {self.resultsList[self.i-2]}')
            self.labelList[-2].setText(f'{self.eqList[self.i-1]} = {self.resultsList[self.i-1]}')
            self.labelList[-1].setText(f'{self.eqList[self.i]} = {self.resultsList[self.i]}')
            ...

        except IndexError:
            
            if self.labelIndex == -5:
                self.leftLayout.frist_n = self.resultsList[0]
                self.labelList[1].setStyleSheet("font-size: 15px")
                self.labelList[0].setStyleSheet("""
    QLabel {
        border: 2px solid #006400;  /* Contorno verde escuro */
        border-radius: 5px;        /* Bordas arredondadas */
        padding: 5px;              /* Espaço interno */
        color: #32CD32;;              /* Cor do texto */
        font-size: 19px;           /* Tamanho da fonte */
        font-weight: bold;         /* Negrito no texto */
    }
""")
                return

            if not len(self.resultsList) > 0:
                return
            
            #print('frist_n:', self.leftLayout.frist_n, 'resultado na lista:', self.resultsList[self.otherIndex], 'índice:', self.otherIndex, 'resultados:', self.resultsList, 'índice da marcação:', self.pointIndex)

            self.styleS()
            self.pointIndex -= 1
            self.leftLayout.frist_n = self.resultsList[self.i]
            if self.pointIndex == 0:
                i = 1

                self.labelList[-1].setStyleSheet("""
    QLabel {
        border: 2px solid #006400;  /* Contorno verde escuro */
        border-radius: 5px;        /* Bordas arredondadas */
        padding: 5px;              /* Espaço interno */
        color: #32CD32;;              /* Cor do texto */
        font-size: 19px;           /* Tamanho da fonte */
        font-weight: bold;         /* Negrito no texto */
    }
""")
            
                self.labelList[0].setStyleSheet("""
    QLabel {
        font-size: 15px;
    }
""")
                self.pointIndex = 5
                self.i = -1
                self.labelIndex = -2

    def setConfig(self):
        self.setWindowTitle('Calculadora')
        self.setMinimumSize(350, 450)
        self.setMaximumSize(350, 450)

    def addToPrincipalLayout(self, widget):
        self.layoutPricipal.addWidget(widget)
    
    def styleS(self):
        
        self.labelList[self.labelIndex + 1].setStyleSheet("""
    QLabel {
        font-size: 15px
    }
""")

        self.labelList[self.labelIndex].setStyleSheet("""
    QLabel {
        border: 2px solid #006400;  /* Contorno verde escuro */
        border-radius: 5px;        /* Bordas arredondadas */
        padding: 5px;              /* Espaço interno */
        color: #32CD32;;              /* Cor do texto */
        font-size: 19px;           /* Tamanho da fonte */
        font-weight: bold;         /* Negrito no texto */
    }
""")
        
        #self.i = -1 if self.labelIndex > -5 else self.i
        #self.labelList[-5].setText(f'{self.eqList[self.i-4]} = {self.resultsList[self.i-4]}') if self.labelIndex > -5 else ...
        #self.labelList[-4].setText(f'{self.eqList[self.i-3]} = {self.resultsList[self.i-3]}') if self.labelIndex > -5 else ...
        #self.labelList[-3].setText(f'{self.eqList[self.i-2]} = {self.resultsList[self.i-2]}') if self.labelIndex > -5 else ...
        #self.labelList[-2].setText(f'{self.eqList[self.i-1]} = {self.resultsList[self.i-1]}') if self.labelIndex > -5 else ...
        #self.labelList[-1].setText(f'{self.eqList[self.i]} = {self.resultsList[self.i]}') if self.labelIndex > -5 else ...
        print('label index:', self.labelIndex, 'índice i:', self.i)

        self.labelIndex -= 1 if self.labelIndex > -5 else -5
        

    def isVis(self):
        
        if not self.labelList[0].isVisible():
            for l in self.labelList:
                l.show()
            self.resize(700, 450)
            self.setFixedSize(700, 450)
            self.display.setFocus()
            return

        for l in self.labelList:
            l.hide()
        self.resize(350, 450)
        self.setFixedSize(350, 450)
        self.display.setFocus()
    
    def makeMsgBox(self):
        return QMessageBox(self)

class HoverButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

        self.state = False
        icon_path = "C:/Users/Thalita/Desktop/Alessandro/Projeto_calculadora/Projeto_calculadora/sobre.png"
        self.setIcon(QIcon(icon_path))
        self.setIconSize(QSize(60, 35))

        # Janela "quadrada" sem barra de título
        self.msg_box = QWidget(self)
        self.label = QLabel(_text.texto, self.msg_box)
        self.label.setStyleSheet('font-size: 14px')
        self.msg_box.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.msg_box.setStyleSheet("background-color: lightgray; border: 2px solid black;")
        self.msg_box.setFixedSize(300, 400)  # Define o tamanho do quadrado
        self.msg_box.setStyleSheet("""
            background-color: #1b2b34;  /* Cor de fundo escura */
        """)

    def show_position(self):
        # Posição relativa ao widget pai
        local_pos = self.pos()
        # Posição global na tela
        global_pos = self.mapToGlobal(QPoint(0, 0)).y()
        
        #print(f"Posição Local (relativa ao widget pai): {local_pos}")
        #print(f"Posição Global (na tela): {global_pos}")

    def enterEvent(self, event):
        if not self.state:
            
            if self.mapToGlobal(QPoint(0, 0)).y() <= 432:
                self.msg_box.move(QPoint(self.mapToGlobal(QPoint(0, 0)).x()-300, self.mapToGlobal(QPoint(0, 0)).y()-20))
            
            if self.mapToGlobal(QPoint(0, 0)).y() > 432:
                self.msg_box.move(QPoint(self.mapToGlobal(QPoint(0, 0)).x()-300, self.mapToGlobal(QPoint(0, 0)).y()-400))

            if self.mapToGlobal(QPoint(0, 0)).x() <= 301:
                self.msg_box.move(QPoint(self.mapToGlobal(QPoint(0, 0)).x()+75, self.mapToGlobal(QPoint(0, 0)).y()-400))
            
            # Mostra a janela no centro do botão
            self.msg_box.show()
            self.show_position()
            self.state = True
        super().enterEvent(event)

    def leaveEvent(self, event):
        if self.state:
            self.msg_box.hide()
            self.state = False
        super().leaveEvent(event)

class LeftLayout(QGridLayout):
    def __init__(self, display: QLineEdit, info) -> None:
        super().__init__()

        self.gridMask_ = [
            ['C', '⌫', '𝑥ˣ', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '3', '2', '+'],
            ['±', '0', '.', '='],
            ['ˣ√𝑥', '', ' ']
        ]

        self.display = display
        self.info = info
        self.signal = None
        self.frist_n = None
        self.second_n = None
        self.initEquation = ""
        self._equation = None
        self.equation = self.initEquation
        self.i = []
        self.makeGrid()
        self.state = False
        
    def information(self, text):
        self.makeDialog(text)

    def makeGrid(self):

        self.display.enterPressed.connect(self.eq)
        self.display.backPressed.connect(self.display.backspace)
        self.display.escPressed.connect(self.clear_)
        self.display.inputPress.connect(lambda x: self.insertButtonToDisplay(Botton(x)))
        self.display.operatorPressed.connect(lambda x: self.signal_(Botton(x)))
        self.display.negativePress.connect(self.invertNumber)
        self.display.rPressed.connect(lambda x: self.signal_(Botton(x)))

        for i, line in enumerate(self.gridMask_):
            for j, colum in enumerate(line):
                botton = Botton(colum)
                botton.setFixedSize(75, 40)
                botton.setStyleSheet('font-size: 20px; font-weight: bold;')
                
                if not isNumoDot(colum) and not isEmpty(colum) and colum != '=' and not colum == ' ':
                    botton.setProperty('cssClass', 'numberButton')
                
                if colum == '=':
                    botton.setFixedSize(75, 85)
                    botton.setProperty('cssClass', 'OButton')
                
                if colum == '':
                    HoverButton(botton)
                    
    
                self.addWidget(botton, i, j)
                self.connectButtonClicked(botton, self.display.setFocus)
                slot = self.makeSlot(self.insertButtonToDisplay, botton)
                self.connectButtonClicked(botton, slot)            
                self.configSpecialButton(botton)

    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, label):
        self._equation = label
        self.info.setText(label)

    def connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)
    
    def connectButtonHovered(self, button, slot):
        button.hovered.connect(slot)

    def configSpecialButton(self, button: QPushButton):
        texto = button.text()

        if texto == 'C':
            button.clicked.connect(self.clear_)

        if texto == '⌫':
            button.clicked.connect(self.display.backspace)
        
        if texto == '±':
            button.clicked.connect(self.invertNumber)
        
        if texto in '/*-+^𝑥ˣˣ√𝑥':
            button.clicked.connect(self.makeSlot(self.signal_, button))

        if texto == '=':
            button.clicked.connect(self.eq)

    def insertButtonToDisplay(self, button):
        texto = button.text()
        textoTotal = self.display.text() + texto
        
        if not isValid(textoTotal):
            return
        
        self.display.setText(textoTotal)

    def makeSlot(self, func, *args, **kwargs):
        def slot():
            return func(*args, **kwargs)
        return slot
    
    def clear_(self):
        self.frist_n = None
        self.signal = None
        self.second_n = None
        self.info.setText(self.initEquation)
        self.display.clear()
        self.display.setFocus()
        self.i.clear()
        window.otherIndex = 3
        window.labelIndex = -2
        window.pointIndex = 5
        window.aI = 0
        window.eqList.clear()
        window.resultsList.clear()
        window.i = -1

        for i, l in enumerate(window.labelList):
        
            l.setStyleSheet('font-size: 15px')
        
            if i == 4:
                l.setStyleSheet("""
    QLabel {
        border: 2px solid #006400;  /* Contorno verde escuro */
        border-radius: 5px;        /* Bordas arredondadas */
        padding: 5px;              /* Espaço interno */
        color: #32CD32;;              /* Cor do texto */
        font-size: 19px;           /* Tamanho da fonte */
        font-weight: bold;         /* Negrito no texto */
    }
""")
            l.setText('-')
    
    def invertNumber(self):
        texto = self.display.text()
        
        if not len(texto) > 0:
            return
        
        value = float(texto) if not float(texto).is_integer() else int(texto)
        value *= -1
        self.display.setText(str(value))
    
    def signal_(self, button):
        buttonText = button.text()
        texto = self.display.text()
        self.display.clear()

        if isValid(texto) and self.frist_n is not None:
            self.frist_n = float(texto) if not float(texto).is_integer() else int(texto)

        if self.frist_n is None and not isValid(texto):
            self._showInfo('Type-error', 'O primeiro número é inválido')
            return
        
        if self.frist_n is None:
            self.frist_n = float(texto) if not float(texto).is_integer() else int(texto)

        self.signal = buttonText
        self.equation = f'{self.frist_n} {self.signal}'
        self.display.setFocus()
    
    def eq(self):
        displayText = self.display.text()
        print('Sinal:', self.signal, 'segundo dígito:', self.second_n)

        if not isValid(displayText) or self.signal is None:
            self._showInfo('Type-error', 'O segundo número é inválido!')
            return

        result = None
        self.second_n = float(displayText)
        self.equation = f'{self.frist_n} {self.signal} {self.second_n}'
        
        if self.signal == '/' and (self.second_n == None or self.second_n == 0):
            self.frist_n = None
            self.signal = None
            self.clear_()
            self.execution = 'Division by zero error'
            self._showError('Dividiu por zero', 'Não é possível dividir por zero!')
            return
        
        if self.frist_n.is_integer():
            int(self.frist_n)
        
        if self.second_n.is_integer():
            int(self.second_n)

        
        try:

            if 'ˣ√𝑥' in self.equation:
                result = round(self.frist_n ** (1/self.second_n),5)
                
                self.info.setText(str(result))
                self.frist_n = result
                self.display.clear()
                self.second_n = 0.0
                self.signal = None

                if result == None:
                    self.frist_n = None

                self.i.append(result)
                window.resultsList.append(result)
                window.eqList.append(self.equation)
                print('Resultados:', window.resultsList)
                print('Equações:', window.eqList)

                if len(self.i) == 1:
                    primeira = f'{window.eqList[-1]}' + f' = {window.resultsList[-1]}'
                    window.labelList[-1].setText(primeira)

                if len(self.i) == 2:
                    primeira = f'{window.eqList[-2]}' + f' = {window.resultsList[-2]}'
                    segunda = f'{window.eqList[-1]}' + f' = {window.resultsList[-1]}'
                    window.labelList[-2].setText(primeira)
                    window.labelList[-1].setText(segunda)
        
                if len(self.i) == 3:
                    primeira = f'{window.eqList[-3]}' + f' = {window.resultsList[-3]}'
                    segunda = f'{window.eqList[-2]}' + f' = {window.resultsList[-2]}'
                    terceira = f'{window.eqList[-1]}' + f' = {window.resultsList[-1]}'
                    window.labelList[-3].setText(primeira)
                    window.labelList[-2].setText(segunda)
                    window.labelList[-1].setText(terceira)
        
                if len(self.i) == 4:
                    primeira = f'{window.eqList[-4]}' + f' = {window.resultsList[-4]}'
                    segunda = f'{window.eqList[-3]}' + f' = {window.resultsList[-3]}'
                    terceira = f'{window.eqList[-2]}' + f' = {window.resultsList[-2]}'
                    quarta = f'{window.eqList[-1]}' + f' = {window.resultsList[-1]}'
                    window.labelList[-4].setText(primeira)
                    window.labelList[-3].setText(segunda)
                    window.labelList[-2].setText(terceira)
                    window.labelList[-1].setText(quarta)
    
                if len(self.i) == 5:
                    primeira = f'{window.eqList[-5]}' + f' = {window.resultsList[-5]}'
                    segunda = f'{window.eqList[-4]}' + f' = {window.resultsList[-4]}'
                    terceira = f'{window.eqList[-3]}' + f' = {window.resultsList[-3]}'
                    quarta = f'{window.eqList[-2]}' + f' = {window.resultsList[-2]}'
                    quinta = f'{window.eqList[-1]}' + f' = {window.resultsList[-1]}'
                    window.labelList[-5].setText(primeira)
                    window.labelList[-4].setText(segunda)
                    window.labelList[-3].setText(terceira)
                    window.labelList[-2].setText(quarta)
                    window.labelList[-1].setText(quinta)
                return
            
            if '𝑥ˣ' in self.equation:
                result = round(float(self.frist_n ** self.second_n), 5) if not float(self.frist_n ** self.second_n).is_integer() else int(self.frist_n ** self.second_n)
                result = round(result,5)
                self.info.setText(str(result))
                self.frist_n = result
                self.display.clear()
                self.second_n = 0.0
                self.signal = None

                if result == None:
                    self.frist_n = None
                self.i.append(result)
                window.resultsList.append(result)
                window.eqList.append(self.equation)
                print('Resultados:', window.resultsList)
                print('Equações:', window.eqList)
                
                if len(self.i) == 1:
                    primeira = f'{window.eqList[-1]}' + f' = {window.resultsList[-1]}'
                    window.labelList[-1].setText(primeira)

                if len(self.i) == 2:
                    primeira = f'{window.eqList[-2]}' + f' = {window.resultsList[-2]}'
                    segunda = f'{window.eqList[-1]}' + f' = {window.resultsList[-1]}'
                    window.labelList[-2].setText(primeira)
                    window.labelList[-1].setText(segunda)
        
                if len(self.i) == 3:
                    primeira = f'{window.eqList[-3]}' + f' = {window.resultsList[-3]}'
                    segunda = f'{window.eqList[-2]}' + f' = {window.resultsList[-2]}'
                    terceira = f'{window.eqList[-1]}' + f' = {window.resultsList[-1]}'
                    window.labelList[-3].setText(primeira)
                    window.labelList[-2].setText(segunda)
                    window.labelList[-1].setText(terceira)
        
                if len(self.i) == 4:
                    primeira = f'{window.eqList[-4]}' + f' = {window.resultsList[-4]}'
                    segunda = f'{window.eqList[-3]}' + f' = {window.resultsList[-3]}'
                    terceira = f'{window.eqList[-2]}' + f' = {window.resultsList[-2]}'
                    quarta = f'{window.eqList[-1]}' + f' = {window.resultsList[-1]}'
                    window.labelList[-4].setText(primeira)
                    window.labelList[-3].setText(segunda)
                    window.labelList[-2].setText(terceira)
                    window.labelList[-1].setText(quarta)
    
                if len(self.i) == 5:
                    primeira = f'{window.eqList[-5]}' + f' = {window.resultsList[-5]}'
                    segunda = f'{window.eqList[-4]}' + f' = {window.resultsList[-4]}'
                    terceira = f'{window.eqList[-3]}' + f' = {window.resultsList[-3]}'
                    quarta = f'{window.eqList[-2]}' + f' = {window.resultsList[-2]}'
                    quinta = f'{window.eqList[-1]}' + f' = {window.resultsList[-1]}'
                    window.labelList[-5].setText(primeira)
                    window.labelList[-4].setText(segunda)
                    window.labelList[-3].setText(terceira)
                    window.labelList[-2].setText(quarta)
                    window.labelList[-1].setText(quinta)
                return
            
            if '^' in self.equation:
                result = round(pow(self.frist_n, self.second_n),7)
                self.display.setFocus()
        
            else:
                result = float(eval(self.equation)) if not float(eval(self.equation)).is_integer() else int(eval(self.equation))
                self.display.setFocus()
        
        except ZeroDivisionError:
            self.execution = 'Division by zero error'
            self._showError('Dividiu por zero', 'Não é possível dividir por zero!')
            self.clear_()
        
        except OverflowError:
            self.execution = 'Over flow error'
            self._showError('Conta exuberante demais', 'Contas em escalas muito grandes são incompatíveis!')
            
        self.info.setText(str(result))
        self.frist_n = result
        self.display.clear()
        self.second_n = 0.0
        self.signal = None

        if result == None:
            self.frist_n = None
        
        self.i.append(result)
        window.resultsList.append(result)
        window.eqList.append(self.equation)
        print('Resultados:', window.resultsList)
        print('Equações:', window.eqList)

        if len(self.i) == 1:
            primeira = f'{window.eqList[-1]}' + f' = {window.resultsList[-1]}'
            window.labelList[-1].setText(primeira)

        if len(self.i) == 2:
            primeira = f'{window.eqList[-2]}' + f' = {window.resultsList[-2]}'
            segunda = f'{window.eqList[-1]}' + f' = {window.resultsList[-1]}'
            window.labelList[-2].setText(primeira)
            window.labelList[-1].setText(segunda)
        
        if len(self.i) == 3:
            primeira = f'{window.eqList[-3]}' + f' = {window.resultsList[-3]}'
            segunda = f'{window.eqList[-2]}' + f' = {window.resultsList[-2]}'
            terceira = f'{window.eqList[-1]}' + f' = {window.resultsList[-1]}'
            window.labelList[-3].setText(primeira)
            window.labelList[-2].setText(segunda)
            window.labelList[-1].setText(terceira)
        
        if len(self.i) == 4:
            primeira = f'{window.eqList[-4]}' + f' = {window.resultsList[-4]}'
            segunda = f'{window.eqList[-3]}' + f' = {window.resultsList[-3]}'
            terceira = f'{window.eqList[-2]}' + f' = {window.resultsList[-2]}'
            quarta = f'{window.eqList[-1]}' + f' = {window.resultsList[-1]}'
            window.labelList[-4].setText(primeira)
            window.labelList[-3].setText(segunda)
            window.labelList[-2].setText(terceira)
            window.labelList[-1].setText(quarta)
    
        if len(self.i) == 5:
            primeira = f'{window.eqList[-5]}' + f' = {window.resultsList[-5]}'
            segunda = f'{window.eqList[-4]}' + f' = {window.resultsList[-4]}'
            terceira = f'{window.eqList[-3]}' + f' = {window.resultsList[-3]}'
            quarta = f'{window.eqList[-2]}' + f' = {window.resultsList[-2]}'
            quinta = f'{window.eqList[-1]}' + f' = {window.resultsList[-1]}'
            window.labelList[-5].setText(primeira)
            window.labelList[-4].setText(segunda)
            window.labelList[-3].setText(terceira)
            window.labelList[-2].setText(quarta)
            window.labelList[-1].setText(quinta)

        if None in window.resultsList:
            window.resultsList.clear()
            self.clear_()

    def makeMsgBox(self):
        return QMessageBox()
        
    def makeDialog(self, text):
        msgbox = self.makeMsgBox()
        msgbox.setText(text)
        return msgbox
    
    def _showError(self, text, msg):
        msgbox = self.makeDialog(text)
        msgbox.setIcon(msgbox.Icon.Critical)
        msgbox.setStandardButtons(msgbox.StandardButton.Ok)# | msgbox.StandardButton.Cancel)
        msgbox.button(msgbox.StandardButton.Ok).setText('Ok')                
        msgbox.setInformativeText(msg)
        msgbox.setWindowTitle('Error')
        msgbox.exec()
    
    def _showInfo(self, text, msg):
        msgbox = self.makeDialog(text)
        msgbox.setIcon(msgbox.Icon.Information)
        msgbox.setStandardButtons(msgbox.StandardButton.Ok)# | msgbox.StandardButton.Cancel)
        msgbox.button(msgbox.StandardButton.Ok).setText('Ok')                
        msgbox.setInformativeText(msg)
        msgbox.setWindowTitle('Attention')
        msgbox.exec()

class RightLayout(QGridLayout):
    def __init__(self) -> None:
        super().__init__()

class Display(QLineEdit):

    enterPressed = Signal(str)
    escPressed = Signal(str)
    backPressed = Signal(str)
    operatorPressed = Signal(str)
    negativePress = Signal()
    inputPress = Signal(str)
    rPressed = Signal(str)

    def __init__(self) -> None:
        super().__init__()

        self.setFixedSize(330, 90)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(15, 15, 15, 15)
        self.setStyleSheet('font-weight: bold; font-size: 40px')
    

    def keyPressEvent(self, event: QKeyEvent) -> None:
        texto = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        isBack = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isOperator = key in [KEYS.Key_Plus, KEYS.Key_Slash, KEYS.Key_Asterisk, KEYS.Key_Minus, KEYS.Key_P]
        isNegative = key in  [KEYS.Key_N]
        isR = key in [KEYS.Key_R]
        isUpper = key == 16777235
        isDown = key == 16777237

        if isEnter:
            self.enterPressed.emit('=')
            return event.ignore()
        
        if isEsc:
            self.escPressed.emit('escape')
            return event.ignore()
        
        if isBack:
            self.backPressed.emit('delete')
            return event.ignore()
        
        if isEmpty(texto):
            return event.ignore()
        
        if isNumoDot(texto):
            self.inputPress.emit(texto)
            return event.ignore()
        
        if isR:
            self.rPressed.emit('ˣ√𝑥')
            return event.ignore()
        
        if isOperator:
            if texto.lower() == 'p':
                texto = '^'
            
            elif texto == '~':
                texto = '*'

            self.operatorPressed.emit(texto)
            return event.ignore()
        
        if isNegative:
            self.negativePress.emit()
            return event.ignore()

class Info(QLabel):
    def __init__(self) -> None:
        super().__init__()
        self.setText('')
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setStyleSheet('font-size: 14px; font-weight: bold;')


app = QApplication()
setupTheme(app)
display = Display()
info = Info()
icon = QIcon(str(FILES_DIR))
lay_1 = LeftLayout(display, info)
lay_2 = RightLayout()
window = MainWindow(lay_1, lay_2, display, info)
window.setWindowIcon(icon)
app.setWindowIcon(icon)
window.show()
app.exec()