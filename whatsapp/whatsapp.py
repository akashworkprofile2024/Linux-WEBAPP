from PyQt5.QtCore import QUrl, QCoreApplication
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
import sys

class WhatsAppApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WhatsApp Desktop")
        self.setGeometry(100, 100, 1280, 720)

        # Set up QWebEngineView to load WhatsApp Web
        self.browser = QWebEngineView()

        # Set a custom user agent
        user_agent = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/117.0.5938.92 Safari/537.36"
        )
        profile = QWebEngineProfile.defaultProfile()
        profile.setHttpUserAgent(user_agent)
        
        # Load WhatsApp Web
        self.browser.setUrl(QUrl("https://web.whatsapp.com/"))
        self.setCentralWidget(self.browser)

def apply_dark_theme(app):
    dark_palette = QPalette()

    # Define color roles for the dark theme
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.Base, QColor(42, 42, 42))
    dark_palette.setColor(QPalette.AlternateBase, QColor(66, 66, 66))
    dark_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.Text, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
    dark_palette.setColor(QPalette.Highlight, QColor(142, 45, 197).lighter())
    dark_palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))

    # Apply the palette to the application
    app.setPalette(dark_palette)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_dark_theme(app)  # Apply the dark theme to the app
    window = WhatsAppApp()
    window.show()
    sys.exit(app.exec_())

