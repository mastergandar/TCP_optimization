
import diagnostic as di
import optimization as opt
import sys
from PyQt5 import QtWidgets
from ui import Ui_MainWindow


def state(func):
    def wrapper(self):
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.centralwidget.repaint()
        func(self)
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton_2.setEnabled(True)

    return wrapper


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.diag_clicked)
        self.ui.pushButton_2.clicked.connect(self.opt_clicked)

    @state
    def diag_clicked(self):

        self.ui.textBrowser.setPlainText(str(di.MakeInfo()))

    @state
    def opt_clicked(self):

        self.ui.textBrowser.setText(str(opt.MakeGrate()))


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    application = MyWindow()
    application.show()

    sys.exit(app.exec_())
