from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QGridLayout ,QLineEdit, QLabel, QPushButton, QWidget
from PySide6.QtCore import Qt, Slot, Signal
from main_window import Window
from variables import MEDIUM_FONT, DARKEST_PRIMARY_, PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR
from styles import qss
import math
from utils import isNumoDot, isEmpty, isValid, isNum

class Display(QLineEdit):

    eqTrigger = Signal(str)
    eqdelete = Signal(str)
    eqesc = Signal(str)
    inputPress = Signal(str)
    operatorPress = Signal(str)
    nPress = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def setConfig(self):
        self.setFixedSize(300, 80)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setStyleSheet('font-weight: bold; font-size: 26px;')
        self.setTextMargins(15, 15, 15, 15)
    
    def keyPressEvent(self, event: QKeyEvent) -> None:
        texto = event.text().strip()
        key = event.key()
        KEYS = Qt.Key
        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        isBack = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isoperator = key in [KEYS.Key_Plus, KEYS.Key_Slash, KEYS.Key_Asterisk, KEYS.Key_Minus, KEYS.Key_P]
        isNegative = key in [KEYS.Key_N]
        
        if isEnter:
            self.eqTrigger.emit('=')
            return event.ignore()
        
        if isEsc:
            self.eqesc.emit('escape')
            return event.ignore()
        
        if isBack:
            self.eqdelete.emit('delete')
            return event.ignore()
        
        if isEmpty(texto):
            return event.ignore()
        
        if isNumoDot(texto):
            self.inputPress.emit(texto)
            return event.ignore()
        
        if isoperator:
            if texto.lower() == 'p':
                texto = '^'

            elif texto =='~':
                texto = '*'
            
            self.operatorPress.emit(texto)
            return event.ignore()
        #return super().keyPressEvent(event)

        if isNegative:
            self.nPress.emit()
            return event.ignore()

class Info(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setConfig(self):
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setStyleSheet('font-weight: bold; font-size: 13px;')

class Botton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setButon()
    
    def setButon(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT)
        font.setItalic(False)
        self.setFont(font)
        self.setCheckable(False)
        #self.setProperty()

class BunttonsGrid(QGridLayout):
    def __init__(self, display:Display, info: Info, window: Window, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '⌫', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '3', '2', '+'],
            ['N', '0', '.', '='],
        ]

        self.display=display
        self.window=window
        self.make_grid()
        self.info = info
        self._execution = ''
        self.execution = ''
        self.executionInit = ''
        self.frist_n = None
        self.second_n = None
        self.signal = None
        self.execution = self.executionInit
        self.state = False

    @property
    def execution(self):
        return self._execution

    @execution.setter
    def execution(self, vari):
        self._execution = vari
        self.info.setText(vari)

    def metodo(self, *args):
        print(args )


    def make_grid(self):

        self.display.eqTrigger.connect(lambda: self.eq(self.display))
        self.display.eqesc.connect(self._clear)
        self.display.eqdelete.connect(self._backspace)
        self.display.inputPress.connect(lambda x: self._insertButtonTexttoDisplay(Botton(x), self.display))
        self.display.operatorPress.connect(lambda x: self.signalSlot(Botton(x)))
        self.display.nPress.connect(self.invertNumber)

        for i, line_b in enumerate(self._gridMask):
            for j, colum_b in enumerate(line_b):
                buton = Botton(colum_b)

                if not isNumoDot(colum_b) and not isEmpty(colum_b) and colum_b != '=':
                    buton.setProperty('cssClass', 'numberButton')
                    self.configSpecialButton(buton)
                
                if colum_b == '=':
                    buton.setProperty('cssClass', 'OButton')
                    self.configSpecialButton(buton)
                
                if colum_b == '.':
                    self.configSpecialButton(buton)

                self.addWidget(buton, i, j)
                slot = self._makeSlot(self._insertButtonTexttoDisplay, buton, self.display)
                self.connectButtonClicked(buton, slot)
                
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    def connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def configSpecialButton(self, button):
        texto = button.text()

        if texto == 'C':
            self.connectButtonClicked(button, self._clear)

        if texto in '/*+-^':
            self.connectButtonClicked(button, self._makeSlot(self.signalSlot, button))

        if texto == '=':
            self.connectButtonClicked(button, self._makeSlot(self.eq, self.display))

        if texto == '⌫':
            self.connectButtonClicked(button, self._backspace)
        
        if texto == 'N':
            self.connectButtonClicked(button, self.invertNumber)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def makeSlot():
            func(*args, **kwargs)
        return makeSlot

    def invertNumber(self):
        displatext = self.display.text()
        self.display.setFocus()

        if not isValid(displatext):
            return

        newNumber = -float(displatext)
        self.display.setText(str(newNumber))

    def _insertButtonTexttoDisplay(self, button, dis):
        texto = button.text()
        new_texto = self.display.text() + texto
 
        if not isValid(new_texto):
            return
        
        if self.signal is None and self.frist_n is not None and self.second_n is not None and isNum(texto):
            #dis.clear()
            self.frist_n = float(texto)
            self.display.clear()

        if texto == '.':
            self.display.setText(str(eval(self.display.text()+'.')))
            self.display.backspace()
            return

        if isValid(new_texto):
            self.display.setText(str(eval(new_texto)))
        self.display.setFocus()
    @Slot()
    def _clear(self):
        self.frist_n = None
        self.second_n = None
        self.signal = None
        self.info.setText(self.executionInit)
        self.display.clear()
        self.display.setFocus()

    @Slot(Botton)
    def signalSlot(self, button):
        buttonText = button.text()
        displayText = self.display.text()
        self.display.clear()

        if not isValid(displayText) and self.frist_n is None:
            self.execution = 'Type error'
            self._showInfo('Entrada inválida', 'Digite apenas números!')
            return

        if self.frist_n is None:
            self.frist_n = float(displayText)
        
        self.signal = buttonText
        self.execution = f'{self.frist_n} {self.signal}'
        self.display.setFocus()
    def eq(self, dis: Display):
        displayText = dis.text()
        

        if not isValid(displayText):
            self.execution = 'Type error'
            self._showInfo('Segundo número é incompatível', 'O segundo dígito deve ser um número!')
            return
        
        if self.signal is None:
            return
        
        self.second_n = float(displayText)
        self.execution = f'{self.frist_n} {self.signal} {self.second_n}'
        result = None
    
        try:
            if '^' in self.execution and isinstance(self.frist_n, float):
                result = math.pow(self.frist_n, self.second_n)
                self.display.setFocus()
                #print(str(result))
                #self.display.setText(str(result))
            else:
                result = eval(self.execution)
                self.display.setFocus()
                #self.display.setText(str(result))
                #print(str(result))

        except ZeroDivisionError:
            self.execution = 'Division by zero error'
            self._showError('Dividiu por zero', 'Não é possível dividir por zero!')
            self._clear()
        
        except OverflowError:
            self.execution = 'Over flow error'
            self._showError('Conta exuberante demais', 'Contas em escalas muito grandes são incompatíveis!')
            self._clear()

        self.frist_n = result
        self.info.setText(str(result))
        dis.clear()
        self.second_n = 0.0
        self.signal = None

        if result == None:
            self.frist_n = None
    
    def makeDialog(self, text):
        msgbox = self.window.makeMsgBox()
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

        
        #result = msgbox.exec()
        #if result == msgbox.StandardButton.Ok:
            #print('Clicou em Ok')

        #if result == msgbox.StandardButton.Cancel:
            #print('Clicou em Cancel')