import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        # Initialize a BankAccount instance with a balance of 100
        self.account = BankAccount(100)
    
    def tearDown(self):
        # Tear down the BankAccount instance after each test
        self.account = None
    
    def test_initial_balance(self):
        # Check if the initial balance is correctly set
        self.assertEqual(self.account.balance, 100)
    
    # Test deposit operation with a positive amount
    def test_deposit_positive_amount(self):
        self.account.deposit(50)  # Perform a deposit of 50
        self.assertEqual(self.account.balance, 150)
    
    # Test deposit operation with zero amount
    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    # Test withdrawal operation with a valid amount
    def test_withdraw_valid_amount(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)

    # Test withdrawal operation that exceeds balance
    def test_withdraw_exceed_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

if __name__ == '__main__':
    unittest.main()  
