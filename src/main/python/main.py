import sys
# from pprint import pprint
# from random import choice

from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QShortcut

from dictionary import close_matches, get_word

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('dictionary.ui', self)
        self.pushButton.clicked.connect(self.printValue)
        self.textBrowser.setAcceptRichText(True)
        # self.setWindowIcon(QtGui.QIcon('icon.png'))
        # Press Enter to search text instead of pressing button
        QShortcut(QtCore.Qt.Key_Return, self.lineEdit, self.printValue)
        self.setFixedSize(550, 350)

    def printValue(self):
        word = self.lineEdit.text()
        result = get_word(word)
        self.textBrowser.clear()
        if result == "N\A":
            self.textBrowser.append("<h1 style='color: red;'>Didn't find any match, check your spelling and try later</h1>")
            matches = close_matches(word)
            str = ""
            #adding to a string
            if matches != []:
                for i in matches:
                    str += f"<li>{i}</li>"
                self.textBrowser.append("<h2 style='color: orange;'>Possible Matches</h2>")
                self.textBrowser.append(f"<ol style='color: orangered;'>{str}</ol>")
            else:
                self.textBrowser.append("<h2 style='color:red;'>No Close Matches Found</h2>")
        else: # the real thing
            self.textBrowser.append(f"<h1>{result['word']}</h1>")
            pos = ""
            for i in result['results']:
                defs = ""
                for j in i['defs']:
                    defs += f"<li>{j}</li>"
                pos += f"<li><h3>{i['pos']}</h3><ol>{defs}</ol></li>"
            pos = f"<ul>{pos}</ul>"
            self.textBrowser.append(pos)
                
        vScroll = self.textBrowser.verticalScrollBar()
        vScroll.setValue(0)
        

if __name__=="__main__":
    # App context for fbs
    appctxt = ApplicationContext()
    App = QApplication(sys.argv)
    # style = choice(QtWidgets.QStyleFactory.keys())
    # app.setStyle(style)
    
    App.setStyle('Fusion')
    window = AppDemo()
    window.show()

    try:
        sys.exit(appctxt.app.exec())
    except SystemExit:
        sys.exit()
