import sys
import emoji
import requests
from PyQt5.QtWidgets import (QApplication , QWidget , QLabel , QLineEdit , QPushButton , QVBoxLayout) # type: ignore
from PyQt5.QtCore import Qt # type: ignore

class weatherApp(QWidget):
   def __init__(self):
      super().__init__()
      self.city_label = QLabel("enter city name" , self)
      self.city_input = QLineEdit(self)
      self.get_weather_button = QPushButton("Get weather" , self)
      self.temprature_label = QLabel(self)
      self.emoji_label = QLabel(self)
      self.description_label = QLabel(self)
      self.initUI()
      
   def initUI(self):
      self.setWindowTitle("Weather App")
      self.setGeometry(500 , 500 , 500 , 500)
      vbox  = QVBoxLayout()
      vbox.addWidget(self.city_label)
      vbox.addWidget(self.city_input)
      vbox.addWidget(self.get_weather_button)
      vbox.addWidget(self.temprature_label)
      vbox.addWidget(self.emoji_label)
      vbox.addWidget(self.description_label)
      
      self.setLayout(vbox)
      
      
      self.city_label.setAlignment(Qt.AlignCenter)
      self.city_input.setAlignment(Qt.AlignCenter)
      # self.get_weather_button.setAlignment(Qt.AlignCenter)
      self.temprature_label.setAlignment(Qt.AlignCenter)
      self.emoji_label.setAlignment(Qt.AlignCenter)
      self.description_label.setAlignment(Qt.AlignCenter)
      
      
      self.city_label.setObjectName("city_label")
      self.city_input.setObjectName("city_input")
      self.get_weather_button.setObjectName("get_weather_button")
      self.temprature_label.setObjectName("temprature_label")
      self.emoji_label.setObjectName("emoji_label")
      self.description_label.setObjectName("description_label")
      
      
      self.setStyleSheet("""
    QWidget {
        background-color: #E3F2FD;
        font-family : calibri;
    }

    QLabel#city_label {
        font-size: 40px;  /* Increased font size */
        font-weight: bold;
        color: #0D47A1;
        margin-bottom: 5px;
    }

    QLineEdit#city_input {
        font-size: 40px;  /* Increased font size */
        padding: 8px;
        border: 2px solid #1976D2;
        border-radius: 5px;
        background-color: #FFFFFF;
    }

    QPushButton#get_weather_button {
        font-size: 30px;  /* Increased font size */
        font-weight: bold;
        color: white;
        background-color: #0288D1;
        border-radius: 5px;
        padding: 10px;
    }

    QLabel#temprature_label {
        font-size: 75px;  /* Increased font size */
        font-weight: bold;
        color: #D32F2F;
        margin-top: 10px;
    }

    QLabel#emoji_label {
        font-size: 100px;  /* Bigger emoji */
        font-family : "Segoe UI Emoji";
        margin-top: 5px;
    }

    QLabel#description_label {
        font-size: 50px;  /* Increased font size */
        font-style: italic;
        color: #424242;
        margin-top: 5px;
    }
""")
      self.get_weather_button.clicked.connect(self.get_weather)
   
   
   def get_weather(self):
      api_key = "f20a091045fade423a0a2f43e05b88e2"
      city = self.city_input.text()
      url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
      
      try:
         response = requests.get(url)
         response.raise_for_status()
         data = response.json()
         
         
         if data["cod"] == 200:
            self.display_weather(data)
      except requests.exceptions.HTTPError as http_error:
         match response.status_code:
            case 400:
               self.display_error("Bad request \n check you input")
            case 401:
               self.display_error("Unathorised\nInvalid Api key")
            case 403:
               self.display_error("Forbidden\n Access is denied")
            case 404:
               self.display_error("not Found\n city not found")
            case 500:
               self.display_error("internal server Error\n please try again later")
            case 502:
               self.display_error("Bad gateway\n invalid response from the server")
            case 503:
               self.display_error("service unavailable\n server is down")
            case 504:
               self.display_error("Gateway Timeout\n no response form the server")
            case _:
               self.display_error(f"http error occured\n{http_error}")
               
      except requests.exceptions.ConnectionError:
         self.display_error("Connection error: \nCheck your internet connection")
      except requests.exceptions.Timeout:
         self.display_error("Timeout error :\n The request timed out")
      except requests.exceptions.TooManyRedirects:
         self.display_error("Too many Redirects :\n check the null")
      except requests.exceptions.RequestException as req_error:
         self.display_error(f"request Error\n {req_error}")
      
      
      
   def display_error(self , message):
      self.temprature_label.setText(message)
      self.emoji_label.clear()
      self.description_label.clear()
      
   
   def display_weather(self , data):
      temprature_k = data['main']["temp"]
      temprature_c = temprature_k -273.15
      temprature_f = (temprature_k*9/5)-459.67
      weather_id = data["weather"][0]["id"]
      weather_description = data["weather"][0]["description"]
      self.emoji_label.setText(self.get_weather_emoji(weather_id))
      self.description_label.setText(weather_description)
      self.temprature_label.setText(f"{temprature_c:.0f}℃")
      
   @staticmethod
   def get_weather_emoji(weather_id):
    if 200 <= weather_id <= 232:
        return "⛈️"  # Thunderstorm
    elif 300 <= weather_id <= 321:
        return "🌧️"  # Drizzle
    elif 500 <= weather_id <= 531:
        return "🌧️"  # Rain
    elif 600 <= weather_id <= 622:
        return "❄️"  # Snow
    elif 701 <= weather_id <= 741:
        return "🌫️"  # Mist/Fog
    elif weather_id == 751:
        return "🌪️"  # Sandstorm
    elif weather_id == 762:
        return "🌋"  # Volcanic Ash
    elif weather_id == 771:
        return "🌬️"  # Squalls
    elif weather_id == 781:
        return "🌪️"  # Tornado
    elif weather_id == 800:
        return "☀️"  # Clear sky
    elif 801 <= weather_id <= 804:
        return "☁️"  # Clouds
    else:
        return ""  # Unknown weather condition
      
      
if __name__ == "__main__":
   app = QApplication(sys.argv)
   weather = weatherApp()
   weather.show()
   sys.exit(app.exec_())