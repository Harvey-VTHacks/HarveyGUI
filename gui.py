# gui.py - Main application to run the UI
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize, Qt
from ui_mic import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Track microphone state (False = Off/Muted, True = On/Recording)
        self.mic_active = False
        
        # Make the button checkable so it can toggle between On/Off states
        self.ui.toolButton.setCheckable(True)
        self.ui.toolButton.setChecked(False)  # Start in Off state
        
        # Connect the microphone button to a function
        self.ui.toolButton.clicked.connect(self.on_mic_clicked)
        
        # Set window title
        self.setWindowTitle("Harvey - Personal Digital Assistant")
        
    def on_mic_clicked(self):
        """Handle microphone button click - toggle between states"""
        print(f"Microphone button clicked! Current state: {self.mic_active}")
        
        # Toggle the microphone state
        self.mic_active = not self.mic_active
        
        if self.mic_active:
            # Microphone is now ON (recording)
            print("Microphone activated - Recording...")
            self.ui.toolButton.setChecked(True)  # This switches to the "On" icon
            
            # Add your voice recording/recognition logic here
            self.start_recording()
            
        else:
            # Microphone is now OFF (muted)
            print("Microphone deactivated - Stopped recording")
            self.ui.toolButton.setChecked(False)  # This switches to the "Off" icon  
            
            # Stop recording logic here
            self.stop_recording()
            
    def start_recording(self):
        """Start voice recording/recognition"""
        # Add your speech recognition code here
        print("Starting voice recognition...")
        pass
        
    def stop_recording(self):
        """Stop voice recording/recognition"""
        # Add code to stop recording here
        print("Stopping voice recognition...")
        pass
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
