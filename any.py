import sys
from PyQt5.QtWidgets import QApplication , QWidget #type:ignore
from PyQt5.QtCore import QTimer , Qt , QTime #type:ignore

class digitalClock(QWidget):
   def __init__(self):
      super().__init__()
      self.initUI()
      
   def initUI(self):
      pass
   
if __name__ == "__main__":
   app = QApplication(sys.argv)
   clock = digitalClock()
   clock.show()
   sys.exit(app.exec())