class Bank:

    def __init__(self, balance: List[int]):
        self.balances = balance

    def _is_valid_account(self, account: int) -> bool:
        if account < 1 or account > len(self.balances):
            return False
        return True

    def _has_funds(self, account: int, money: int) -> bool:
        return self.balances[account - 1] >= money

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self._is_valid_account(account1) or not self._is_valid_account(account2):
            return False

        if not self._has_funds(account1, money):
            return False

        self.balances[account1 - 1] -= money
        self.balances[account2 - 1] += money

        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._is_valid_account(account):
            return False

        self.balances[account - 1] += money
        return True


    def withdraw(self, account: int, money: int) -> bool:
        if not self._is_valid_account(account):
            return False

        if not self._has_funds(account, money):
            return False

        self.balances[account - 1] -= money
        return True



# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)