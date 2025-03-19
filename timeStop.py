import sys
from  PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QLabel , QVBoxLayout ,QHBoxLayout , QWidget  #type:ignore
from PyQt5.QtCore import QTimer , QTime  , Qt  #type:ignore

class StopWatch(QWidget):
   def __init__(self):
      super().__init__()
      self.time = QTime(0, 0 , 0 , 0)
      self.time_label = QLabel("00:00:00:00" , self)
      self.start_button = QPushButton("start" , self)
      self.stop_button = QPushButton("stop" , self)
      self.reset_button = QPushButton("reset" , self)
      self.timer = QTimer(self)
      self.initUI()
   
   def initUI(self):
      self.setWindowTitle("StopWatch")
      vbox =  QVBoxLayout()
      vbox.addWidget(self.time_label)
      vbox.addWidget(self.start_button)
      vbox.addWidget(self.stop_button)
      vbox.addWidget(self.reset_button)
      self.setLayout(vbox)
      self.time_label.setAlignment(Qt.AlignCenter)
      hbox = QHBoxLayout()
      # hbox.addWidget(self.time_label)
      hbox.addWidget(self.start_button)
      hbox.addWidget(self.stop_button)
      hbox.addWidget(self.reset_button)
      vbox.addLayout(hbox)
      self.setStyleSheet("""
                         QPushButton , QLabel{
                            padding:20px;
                            font-weight:bold;
                            font-family: calibri;
                         }
                         QPushButton{
                            font-size : 50px;
                            
                         }
                         QLabel{
                            font-size:120px;
                            background-color : rgb(190, 230, 248);
                           border-radius:20px;
                         }
                         
                         
                         """)
      self.start_button.clicked.connect(self.start)
      self.stop_button.clicked.connect(self.stop)
      self.reset_button.clicked.connect(self.reset)
      self.timer.timeout.connect(self.update_display)
      
   def start(self):
      self.timer.start(10)
   def stop(self):
      self.timer.stop()
   def reset(self):
      self.timer.stop()
      self.time = QTime(0,0,0,0)
      self.time_label.setText(self.format_time(self.time))
   def format_time(self , time):
      hours = time.hour()
      minutes = time.minute()
      second = time.second()
      millisecond = time.msec() // 10
      return f"{hours:02} :{minutes:02}:{second:02}:{millisecond:02}"

   def update_display(self):
      self.time = self.time.addMSecs(10)
      self.time_label.setText(self.format_time(self.time))
   
      

if __name__ == "__main__":
   app = QApplication(sys.argv)
   stopwatch = StopWatch()
   stopwatch.show()
   sys.exit(app.exec_())