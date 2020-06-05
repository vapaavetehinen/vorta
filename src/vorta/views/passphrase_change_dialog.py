import re
from PyQt5 import uic

uifile = get_asset('UI/passchange.ui')
PassChangeUI, PassChangeBase = uic.loadUiType(uifile)


class PassChangeWindow(PassChangeUI, PassChangeBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.closeButton.clicked.connect(self.close)
        self.saveButton.clicked.connect(self.run)


    def run(self):
        self._set_status('Not Implemented')

    def _set_status(self, text):
        self.errorText.setText(text)
        self.errorText.repaint()
