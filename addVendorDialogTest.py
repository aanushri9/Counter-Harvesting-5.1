import sys
import unittest
from PyQt5.QtWidgets import QApplication, QDialog,QMainWindow
from PyQt5.QtCore import Qt


from ui import AddVendor

app = QApplication(sys.argv)

vendor_dialog = QMainWindow()
vendor_dialog_ui = AddVendor.Ui_addVendorDialog()
vendor_dialog_ui.setupUi(vendor_dialog)

class AddVendorDialogTests(unittest.TestCase):

    def test_defaults(self):
        '''Test the defaults'''
        self.assertEqual(vendor_dialog_ui.nameEdit.text(), "")
        self.assertEqual(vendor_dialog_ui.customerIdEdit.text(), "")
        self.assertEqual(vendor_dialog_ui.URLEdit.text(), "")
        self.assertEqual(vendor_dialog_ui.requesterIdEdit.text(), "")
        self.assertEqual(vendor_dialog_ui.All_reports_edit_fetch.date().toString(Qt.ISODate), "2020-01-01")
        self.assertEqual(vendor_dialog_ui.apiKeyEdit.text(), "")
        self.assertEqual(vendor_dialog_ui.notesEdit.text(), "")
        self.assertEqual(vendor_dialog_ui.platformEdit.text(), "")
        self.assertEqual(vendor_dialog_ui.providerEdit.text(), "")
        self.assertEqual(vendor_dialog_ui.twoattemptsCheckbox.checkState(), False)
        self.assertEqual(vendor_dialog_ui.requestcheckBox.checkState(), False)
        self.assertEqual(vendor_dialog_ui.ipcheckBox.checkState(), False)


    def test_ok_button(self):
        okWidget = vendor_dialog_ui.buttonBox.Ok
        self.assertIsNotNone(okWidget)
        cancelWidget = vendor_dialog_ui.buttonBox.Cancel
        self.assertIsNotNone(cancelWidget)

if __name__ == "__main__":
        unittest.main()