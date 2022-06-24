import unittest

from solutions.day4_oop import BankAccount, InsufficientFundsException


class WithdrawTestCase(unittest.TestCase):
    def setUp(self):
        self.bank_account = BankAccount('BRD', 100)

    def test_valid_amount(self):
        self.bank_account.withdraw(70)
        self.assertEqual(self.bank_account.balance, 30)

    def test_invalid_amount(self):
        with self.assertRaises(InsufficientFundsException):
            self.bank_account.withdraw(120)
        self.assertEqual(self.bank_account.balance, 100)
