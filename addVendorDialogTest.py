import sys
import unittest
from PyQt5.QtWidgets import QApplication, QLineEdit, QCheckBox, QDateEdit
from ui.AddVendor import Ui_addVendorDialog

class TestAddVendorDialog(unittest.TestCase):
    def __init__(self, methodName='runTest', manage_vendors_ui: Ui_addVendorDialog = None):
        super().__init__(methodName)
        self.app = QApplication(sys.argv)
        self.dialog = manage_vendors_ui or Ui_addVendorDialog()

    def tearDown(self):
        self.app.exit()

    def test_defaults(self):
        '''Test the defaults'''
        self.assertEqual(self.dialog.nameEdit.text(), "")
        self.assertEqual(self.dialog.customerIdEdit.text(), "")
        self.assertEqual(self.dialog.baseUrlEdit.text(), "")
        self.assertEqual(self.dialog.requesterIdEdit.text(), "")
        self.assertEqual(self.dialog.apiKeyEdit.text(), "")
        self.assertEqual(self.dialog.platformEdit.text(), "")
        # Assuming local_only_check_box is part of Ui_addVendorDialog
        self.assertEqual(self.dialog.local_only_check_box.checkState(), 0)  # Unchecked state
        self.assertEqual(self.dialog.descriptionEdit.toPlainText(), "")

    def test_widgets_exist(self):
        '''Test the existence of widgets'''
        self.assertIsInstance(self.dialog.nameEdit, QLineEdit)
        self.assertIsInstance(self.dialog.customerIdEdit, QLineEdit)
        self.assertIsInstance(self.dialog.baseUrlEdit, QLineEdit)
        self.assertIsInstance(self.dialog.requesterIdEdit, QLineEdit)
        self.assertIsInstance(self.dialog.apiKeyEdit, QLineEdit)
        self.assertIsInstance(self.dialog.platformEdit, QLineEdit)
        # Assuming local_only_check_box is part of Ui_addVendorDialog
        self.assertIsInstance(self.dialog.local_only_check_box, QCheckBox)
        self.assertIsInstance(self.dialog.descriptionEdit, QLineEdit)
        self.assertIsInstance(self.dialog.All_reports_edit_fetch, QDateEdit)

    def test_button_click(self):
        '''Test button click action'''
        # Assuming a function named on_validate_button_click exists
        okWidget = self.dialog.buttonBox.button(self.dialog.buttonBox.Ok)
        self.assertIsNotNone(okWidget)

        cancelWidget = self.dialog.buttonBox.button(self.dialog.buttonBox.Cancel)
        self.assertIsNotNone(cancelWidget)

if __name__ == "__main__":
    unittest.main()
