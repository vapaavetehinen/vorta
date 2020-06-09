import re
from PyQt5 import uic
from vorta.utils import get_asset

uifile = get_asset('UI/passchange.ui')
PassChangeUI, PassChangeBase = uic.loadUiType(uifile)


class PassChangeWindow(PassChangeUI, PassChangeBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.closeButton.clicked.connect(self.close)
        self.saveButton.clicked.connect(self.run)


    def run(self):
        if self.validate():
            self._set_status(self.tr('Not Implemented'))
        else:
            pass


    def _set_status(self, text):
        self.errorText.setText(text)
        self.errorText.repaint()

    @property
    def values(self):
        out = dict(
            old_passphrase=self.currentPassphraseLineEdit.text(),
            new_passphrase=self.newPassphraseLineEdit.text(),
            confirm_new_passphrase=self.confirmPassphraseLineEdit.text()
        )
        return out

    def validate(self):
        #new passphrase does not match
        if not self.values['new_passphrase'] == self.values['confirm_new_passphrase']:
            self._set_status(self.tr('New passphrases don\'t match'))
            return False
        #new passphrase too short
        if len(self.values['new_passphrase']) < 8:
            self._set_status(self.tr('Please use a longer new passphrase.'))
            return False
        return True
