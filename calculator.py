# Importing Modules
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QGridLayout,QHBoxLayout,QVBoxLayout
from PyQt5.QtGui import QFont

# Adding Main Window class
class CalcApp(QWidget):
    def __init__(self):
        super().__init__()

        # Sets Main Window Requirements
        self.setWindowTitle("Calculatoruh")
        self.resize(250,300)

        # Creating Widgets
        self.textBox=QLineEdit()
        self.textBox.setFont(QFont("Helvetica", 32))
        self.grid=QGridLayout()
        self.buttons=["7","8","9","/","4","5","6","*","1","2","3","+","0",".","=","-"]
        row,col=0,0
        for text in self.buttons:
            button=QPushButton(text)
            button.clicked.connect(self.buttonClick)
            button.setStyleSheet('''
                                 QPushButton{
                                    font: 25px Comic Sans MS;
                                    padding: 10px;
                                 }
                                 ''')
            self.grid.addWidget(button,row,col)
            col+=1
            if col>3:
                col,row=0,row+1
        self.clear=QPushButton("C")
        self.delete=QPushButton("AC")

        # Adds CSS Styles to "clear" Widget
        self.clear.setStyleSheet('''
                                 QPushButton{
                                    font: 25px Comic Sans MS;
                                    padding: 10px;
                                 }
                                 ''')

        # Adds CSS Styles to "delete" Widget
        self.delete.setStyleSheet('''
                                  QPushButton{
                                    font: 25px Comic Sans MS;
                                    padding: 10px;
                                  }
                                  ''')

        # Designing Layouts
        masterLayout=QVBoxLayout()
        masterLayout.addWidget(self.textBox)
        masterLayout.addLayout(self.grid)
        buttonRow=QHBoxLayout()
        buttonRow.addWidget(self.clear)
        buttonRow.addWidget(self.delete)
        masterLayout.addLayout(buttonRow)
        masterLayout.setContentsMargins(25,25,25,25)    #Left, Top, Right, Bottom Coordinates
        self.setLayout(masterLayout)

        # Trigger Events
        self.clear.clicked.connect(self.buttonClick)
        self.delete.clicked.connect(self.buttonClick)

    # Functions
    def buttonClick(self):
        button=app.sender()
        text=button.text()
        if text=="=":
            symbol=self.textBox.text()
            try:
                res=eval(symbol)
                self.textBox.setText(str(res))
            except Exception as e:
                print("Error: ",e)
                self.textBox.setText("ERROR OCCURED! see the terminal")
        elif text=="AC":
        	self.textBox.clear()
        elif text=="C":
            currentValue=self.textBox.text()
            self.textBox.setText(currentValue[:-1])
        else:
            currentValue=self.textBox.text()
            self.textBox.setText(currentValue+text)

# Execution
if __name__=="__main__":
    app=QApplication([])
    mainWindow=CalcApp()

    # Adding CSS Styles to "mainWindow" object (or) "CalcApp" class
    mainWindow.setStyleSheet('''
                             QWidget{
                                background-color: #111;
                                color: #f1f1f1;
                             }
                             ''')
    mainWindow.show()
    app.exec_()
