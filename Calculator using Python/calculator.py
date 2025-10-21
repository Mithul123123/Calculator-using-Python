import sys
from PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QLineEdit,QApplication,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
class editkeyevent(QLineEdit):
   def keyPressEvent(self, event):
       event.ignore()
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.dotcount=0
        self.operator=""
        self.preop=""
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("Calculator using Python\\tool_14995731.png"))
        self.label=QLabel("",self)
        self.text_box=editkeyevent(self)
        self.text_box.setPlaceholderText("0")
        #button main
        self.buttonce=QPushButton("CE",self)
        self.buttoncut=QPushButton("❌",self)
        self.buttonminus=QPushButton("-(x)",self)
        #button set1
        self.button1=QPushButton("1",self)
        self.button2=QPushButton("2",self)
        self.button3=QPushButton("3",self)
        self.button4=QPushButton("+",self)
        #button set2
        self.button5=QPushButton("4",self)
        self.button6=QPushButton("5",self)
        self.button7=QPushButton("6",self)
        self.button8=QPushButton("-",self)
        #button set3
        self.button9=QPushButton("7",self)
        self.button10=QPushButton("8",self)
        self.button11=QPushButton("9",self)
        self.button12=QPushButton("/",self)
        #button set4
        self.button13=QPushButton("0",self)
        self.button14=QPushButton(".",self)
        self.button15=QPushButton("=",self)
        self.button16=QPushButton("*",self)
        
        self.initui()
        self.initbuttons()
        self.design()
    def initui(self):
        
        
        self.vbox=QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.text_box) 
        self.setLayout(self.vbox)

       
        
    def initbuttons(self):
        #button set mann
        hbox5=QHBoxLayout()
        hbox5.addWidget(self.buttonce)
        hbox5.addWidget(self.buttoncut)
        hbox5.addWidget(self.buttonminus)
        #button set 1
        hbox1=QHBoxLayout()
        hbox1.addWidget(self.button1)
        hbox1.addWidget(self.button2)
        hbox1.addWidget(self.button3)
        hbox1.addWidget(self.button4)
        #button set 2
        hbox2=QHBoxLayout()
        hbox2.addWidget(self.button5)
        hbox2.addWidget(self.button6)
        hbox2.addWidget(self.button7)
        hbox2.addWidget(self.button8)
         #button set 3
        hbox3=QHBoxLayout()
        hbox3.addWidget(self.button9)
        hbox3.addWidget(self.button10)
        hbox3.addWidget(self.button11)
        hbox3.addWidget(self.button12)
        #button set 4
        hbox4=QHBoxLayout()
        hbox4.addWidget(self.button13)
        hbox4.addWidget(self.button14)
        hbox4.addWidget(self.button15)
        hbox4.addWidget(self.button16)
       
   
        self.vbox.addLayout(hbox5)
        self.vbox.addLayout(hbox1)
        self.vbox.addLayout(hbox2)
        self.vbox.addLayout(hbox3)
        self.vbox.addLayout(hbox4)
        #button register for styling 
        self.buttoncut.setObjectName("buttoncut")
        self.buttoncut.clicked.connect(self.buttoncut_click)
        self.buttonce.setObjectName("buttonce")
        self.buttonce.clicked.connect(self.buttonce_click)
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(self.button1_click)
        self.button2.setObjectName("button2")
        self.button2.clicked.connect(self.button2_click)
        self.button3.setObjectName("button3")
        self.button3.clicked.connect(self.button3_click)
        self.button4.setObjectName("button4")
        self.button4.clicked.connect(self.button4_click)
        self.button5.setObjectName("button5")
        self.button5.clicked.connect(self.button5_click)
        self.button6.setObjectName("button6")
        self.button6.clicked.connect(self.button6_click)
        self.button7.setObjectName("button7")
        self.button7.clicked.connect(self.button7_click)
        self.button8.setObjectName("button8")
        self.button8.clicked.connect(self.button8_click)
        self.button9.setObjectName("button9")
        self.button9.clicked.connect(self.button9_click)
        self.button10.setObjectName("button10")
        self.button10.clicked.connect(self.button10_click)
        self.button11.setObjectName("button11")
        self.button11.clicked.connect(self.button11_click)
        self.button12.setObjectName("button12")
        self.button12.clicked.connect(self.button12_click)
        self.button13.setObjectName("button13")
        self.button13.clicked.connect(self.button13_click)
        self.button14.setObjectName("button14")
        self.button14.clicked.connect(self.button14_click)
        self.button15.setObjectName("button15")
        self.button15.clicked.connect(self.button15_click)
        self.button16.setObjectName("button16")
        self.button16.clicked.connect(self.button16_click)
        self.buttonminus.setObjectName("buttonminus")
        self.buttonminus.clicked.connect(self.buttonminus_click)
        self.text_box.setObjectName("text_box")
        self.label.setObjectName("label")

    def preoperator(self):
      if not self.text_box.text()=="" and not self.label.text()=="":
       match (self.operator):
          case "+":
            self.label.setText(f"{(float(self.text_box.text())+float(self.label.text())):.6f}")
            self.text_box.setText("")
            self.operator=""
            self.dotcount=0
          case "-":
            self.label.setText(f"{(float(self.label.text())-float(self.text_box.text())):.6f}")
            self.text_box.setText("")
            self.operator=""
            self.dotcount=0
          case "*":
            self.label.setText(f"{(float(self.label.text())*float(self.text_box.text())):.6f}")
            self.text_box.setText("")
            self.operator=""
            self.dotcount=0
          case "/":
            self.label.setText(f"{(float(self.label.text())/float(self.text_box.text())):.6f}")
            self.text_box.setText("")
            self.operator=""
            self.dotcount=0
    
    def design(self):
        self.setStyleSheet("""
                          
                           
                           QWidget
                           {
                           background-color:#C0C0C0
                           }
                           QPushButton#button4,#button8,#button12,#button16,#button15,#buttonce,#buttoncut,#buttonminus
                           {
                           background-color:#404040;
                           color:black;
                           font-weight:bold;
                           font-size:40px;
                           padding:10px;
                           
                           }
                           QPushButton#button1,#button2,#button3,#button5,#button6,#button7,#button9,#button10,#button11,#button13,#button14
                           
                           {
                           background-color:#808080;
                           color:black;
                           font-weight:bold;
                            font-size:30px;
                            padding:17px;
                           
                           }
                           QLineEdit#text_box
                           {
                           font-size:45px;
                           background-color:white;
                           border:3px solid gray;
                           padding:5px;
                           }
                           QLabel#label
                           {
                           font-size:40px;
                           background-color:white;
                           padding:5px;
                          
                           
                           }
                           QPushButton#buttoncut
                           {
                            font-family:segoe UI emoji;
                            font-size:35px;
                            color:black;
                           
                           }
                           QPushButton#buttoncut:hover
                           {
                           
                           background-color:black;
                           }
                           QPushButton#buttonce:hover
                           {
                           color:cyan;
                           background-color:black;
                           }
                           QPushButton#button4:hover
                           {
                           color:cyan;
                           background-color:black;
                           }
                           QPushButton#button8:hover
                           {
                           color:cyan;
                           background-color:black;
                           }
                           QPushButton#button12:hover
                           {
                           color:cyan;
                           background-color:black;
                           }
                           QPushButton#button15:hover
                           {
                           color:cyan;
                           background-color:black;
                           }
                           QPushButton#button16:hover
                           {
                           color:cyan;
                           background-color:black;
                           }
                           QPushButton#button1:hover
                           {
                           color:white;
                           background-color:black;
                           }
                           QPushButton#button2:hover
                           {
                           color:white;
                           background-color:black;
                           }
                           QPushButton#button3:hover
                           {
                           color:white;
                           background-color:black;
                           }
                           QPushButton#button5:hover
                           {
                           color:white;
                           background-color:black;
                           }
                           QPushButton#button6:hover
                           {
                           color:white;
                           background-color:black;
                           }
                           QPushButton#button7:hover
                           {
                           color:white;
                           background-color:black;
                           }
                           QPushButton#button9:hover
                           {
                           color:white;
                           background-color:black;
                           }
                           QPushButton#button10:hover
                           {
                           color:white;
                           background-color:black;
                           }
                           QPushButton#buttonminus:hover
                           {
                           color:cyan;
                           background-color:black;
                           }
                           QPushButton#button11:hover
                           {
                           color:white;
                           background-color:black;
                           }
                           QPushButton#button13:hover
                           {
                           color:white;
                           background-color:black;
                           }
                           QPushButton#button14:hover
                           {
                           color:white;
                           background-color:black;
                           }
                           

                           
                            
                               """)
    def button1_click(self):#1
     self.text_box.setText(self.text_box.text()+self.button1.text())
    def button2_click(self):#2
      self.text_box.setText(self.text_box.text()+self.button2.text())
    def button3_click(self):#3
      self.text_box.setText(self.text_box.text()+self.button3.text())  
    def button4_click(self):#+
      
      self.preoperator()
      self.operator="+"
      if not self.text_box.text()=="":
       self.label.setText(self.text_box.text())
       self.text_box.setText("")
       self.dotcount=0
       
       
       
    def button5_click(self):#4
      self.text_box.setText(self.text_box.text()+self.button5.text()) 
    def button6_click(self):#5
      self.text_box.setText(self.text_box.text()+self.button6.text())
    def button7_click(self):#6
      self.text_box.setText(self.text_box.text()+self.button7.text())
    def button8_click(self):#-
    
     self.preoperator()
     self.operator="-"
     if not self.text_box.text()=="":
     
      self.label.setText(self.text_box.text())
      self.text_box.setText("")
      self.dotcount=0
     
      
    def button9_click(self):#7
      self.text_box.setText(self.text_box.text()+self.button9.text())
    def button10_click(self):#8
     self.text_box.setText(self.text_box.text()+self.button10.text())
    def button11_click(self):#9
     self.text_box.setText(self.text_box.text()+self.button11.text())
    def button12_click(self):#/
      self.preoperator()
      self.operator="/"
      if not self.text_box.text()=="":
      
       self.label.setText(self.text_box.text()) 
       self.text_box.setText("")
       self.dotcount=0
      
    def button13_click(self):#0
      self.text_box.setText(self.text_box.text()+self.button13.text()) 
    def button14_click(self):#.
    
      if self.dotcount==0 and  not self.text_box.text()=="" and self.text_box.text().count(".")==0:
       self.dotcount=self.dotcount+1
       self.text_box.setText(self.text_box.text()+self.button14.text())
    def button16_click(self):#*
      self.preoperator()
      self.operator="*"
      if not self.text_box.text()=="":
     
       self.label.setText(self.text_box.text()) 
       self.text_box.setText("")
       self.dotcount=0
       self.preop=self.operator
       
    def button15_click(self):#=
      self.dotcount=0
      if not self.text_box.text()=="" and not self.label.text()=="":
        match (self.operator):
          case "+":
            self.label.setText(f"{(float(self.label.text())+float(self.text_box.text())):.6f}")
            
            self.text_box.setText(self.label.text())
            self.operator=""
          case "-":
            self.label.setText(f"{(float(self.label.text())-float(self.text_box.text())):.6f}")
            self.text_box.setText(self.label.text())
            self.operator=""
          case "*":
            self.label.setText(f"{(float(self.label.text())*float(self.text_box.text())):.6f}")
            self.text_box.setText(self.label.text())
            self.operator=""
          case "/":
            self.label.setText(f"{(float(self.label.text())/float(self.text_box.text())):.6f}")
            self.text_box.setText(self.label.text())
            self.operator=""
    def buttoncut_click(self):#cut
     if not self.text_box.text() == "":
      char=self.text_box.text()[len(self.text_box.text())-1]
      if char=="." :
        self.dotcount=0
      self.text_box.setText(self.text_box.text()[0:len(self.text_box.text())-1])
      
    def buttonce_click(self):#ce
      self.text_box.setText("")
      self.label.setText("0")
      self.dotcount=0
    def buttonminus_click(self):
       if self.text_box.text()=="":
         self.text_box.setText("-")
      
     
      
                            
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Calculator()
    window.show()
    sys.exit(app.exec_())

