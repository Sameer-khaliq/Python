# Requirements:

# BankAccount class — owner, account number, balance
# deposit() — positive amount only
# withdraw() — insufficient funds check
# transfer() — ek account se doosre mein
# get_statement() — poori transaction history
# SavingsAccount(BankAccount) — child class — interest rate add hoga
# CurrentAccount(BankAccount) — child class — overdraft limit hogi
# __str__ — clean display
# Custom exceptions — InsufficientFundsError, InvalidAmountError
# CLI — multiple accounts banana, transactions karna


class InsufficientFundsError(Exception):
    """Raised when an account does not have enough balance or overdraft limit."""
    pass


class InvalidAmountError(Exception):
    """Raised when an invalid amount (negative or zero) is provided for a transaction."""
    pass


class BankAccount:
    account_counter = 1000  # Class variable — auto account numbers

    def __init__(self, owner, initial_balance=0):
        if initial_balance < 0:
            raise InvalidAmountError("Initial balance cannot be negative.")
        
        self.owner = owner
        self.account_number = f"ACC{BankAccount.account_counter}"
        BankAccount.account_counter += 1
        
        # Using double underscores for true encapsulation (private variables)
        self.__balance = initial_balance
        self.__transactions = []
        
        # Log initial deposit if any
        if initial_balance > 0:
            self.__transactions.append(f"Initial Deposit: +PKR {initial_balance}")

    # --- Property Getters ---
    @property
    def balance(self):
        return self.__balance

    # Helper setter inside the class to safely update balance internally
    def _update_balance(self, amount):
        self.__balance += amount

    def _log_transaction(self, statement):
        self.__transactions.append(statement)

    # --- Core Methods ---
    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")
        
        self._update_balance(amount)
        self._log_transaction(f"Deposited: +PKR {amount}")
        print(f"Successfully deposited PKR {amount}. New Balance: PKR {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise InsufficientFundsError(f"Insufficient funds. Available balance: PKR {self.__balance}")
        
        self._update_balance(-amount)
        self._log_transaction(f"Withdrew: -PKR {amount}")
        print(f"Successfully withdrew PKR {amount}. Remaining Balance: PKR {self.balance}")

    def transfer(self, target_account, amount):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a valid BankAccount instance.")
        if amount <= 0:
            raise InvalidAmountError("Transfer amount must be positive.")
            
        # First check if this account has enough money to withdraw
        # (Overdraft logic for CurrentAccount is safely handled due to polymorphism)
        self.withdraw(amount) 
        
        # Deposit into the target account
        target_account.deposit(amount)
        
        # Replace the default log statements with transfer-specific logs
        self.__transactions[-1] = f"Transfer to {target_account.account_number}: -PKR {amount}"
        target_account.__transactions[-1] = f"Transfer from {self.account_number}: +PKR {amount}"
        print(f"Successfully transferred PKR {amount} to {target_account.owner} ({target_account.account_number}).")

    def get_statement(self):
        if not self.__transactions:
            return "No transactions found."
        
        statement_str = f"\n--- Transaction History for {self.account_number} ({self.owner}) ---\n"
        for txn in self.__transactions:
            statement_str += f"- {txn}\n"
        statement_str += f"Current Balance: PKR {self.balance}\n" + "-"*50
        return statement_str

    def __str__(self):
        return f"[{self.__class__.__name__}] Acc No: {self.account_number} | Owner: {self.owner} | Balance: PKR {self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, owner, initial_balance=0, interest_rate=0.05):
        super().__init__(owner, initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        # Calculate interest based on current balance
        interest = self.balance * self.interest_rate
        if interest > 0:
            self._update_balance(interest)
            self._log_transaction(f"Interest Earned ({self.interest_rate*100}%): +PKR {interest}")
            print(f"Interest of PKR {interest} added. New Balance: PKR {self.balance}")
        else:
            print("No interest added (Balance is 0).")


class CurrentAccount(BankAccount):
    def __init__(self, owner, initial_balance=0, overdraft_limit=5000):
        super().__init__(owner, initial_balance)
        self.overdraft_limit = overdraft_limit

    # Overriding withdraw to respect the overdraft limit
    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        
        # Total accessible funds = balance + overdraft_limit
        total_accessible = self.balance + self.overdraft_limit
        
        if amount > total_accessible:
            raise InsufficientFundsError(
                f"Transaction denied. Amount exceeds balance and overdraft limit. "
                f"Max available: PKR {total_accessible}"
            )
        
        self._update_balance(-amount)
        self._log_transaction(f"Withdrew (Overdraft Allowed): -PKR {amount}")
        print(f"Successfully withdrew PKR {amount}. Remaining Balance: PKR {self.balance}")


# ==========================================
# CLI — Interactive Banking System
# ==========================================

def main():
    accounts = {}  # Dictionary to store accounts by their account number
    print("=== Welcome to the OOP Banking System ===")

    while True:
        print("\nMain Menu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. View Account Statement")
        print("6. List All Accounts")
        print("7. Add Interest (Savings Account Only)")
        print("8. Exit")
        
        choice = input("Select an option (1-8): ").strip()
        
        try:
            if choice == "1":
                owner = input("Enter account holder name: ").strip()
                if not owner:
                    print("Error: Owner name cannot be empty.")
                    continue
                
                print("Choose Account Type:\n 1. Savings Account\n 2. Current Account")
                acc_type = input("Option: ").strip()
                
                bal = float(input("Enter initial deposit amount: ") or 0)
                
                if acc_type == "1":
                    rate = float(input("Enter interest rate (e.g., 0.05 for 5%): ") or 0.05)
                    acc = SavingsAccount(owner, bal, rate)
                elif acc_type == "2":
                    limit = float(input("Enter overdraft limit (Default 5000): ") or 5000)
                    acc = CurrentAccount(owner, bal, limit)
                else:
                    print("Invalid choice. Account creation canceled.")
                    continue
                
                accounts[acc.account_number] = acc
                print(f"\nAccount Created Successfully!\n{acc}")
                
            elif choice in ["2", "3", "4", "5", "7"]:
                if not accounts:
                    print("No accounts available in the system yet. Create one first!")
                    continue
                
                acc_num = input("Enter account number: ").strip().upper()
                if acc_num not in accounts:
                    print("Account not found.")
                    continue
                
                account = accounts[acc_num]
                
                if choice == "2":
                    amt = float(input("Enter amount to deposit: "))
                    account.deposit(amt)
                    
                elif choice == "3":
                    amt = float(input("Enter amount to withdraw: "))
                    account.withdraw(amt)
                    
                elif choice == "4":
                    target_num = input("Enter recipient account number: ").strip().upper()
                    if target_num not in accounts:
                        print("Recipient account not found.")
                        continue
                    if target_num == acc_num:
                        print("Cannot transfer money to the same account.")
                        continue
                    
                    amt = float(input("Enter transfer amount: "))
                    account.transfer(accounts[target_num], amt)
                    
                elif choice == "5":
                    print(account.get_statement())
                    
                elif choice == "7":
                    if isinstance(account, SavingsAccount):
                        account.add_interest()
                    else:
                        print("Error: This operation is only available for Savings Accounts.")
            
            elif choice == "6":
                if not accounts:
                    print("No accounts registered yet.")
                else:
                    print("\n--- All Registered Accounts ---")
                    for acc in accounts.values():
                        print(acc)
                        
            elif choice == "8":
                print("\nThank you for using our Banking System. Goodbye!")
                break
            else:
                print("Invalid option selection. Please try again.")
                
        except (InsufficientFundsError, InvalidAmountError) as e:
            print(f"\n[BANK ERROR]: {e}")
        except ValueError:
            print("\n[INPUT ERROR]: Please enter a valid number numeric value.")
        except Exception as e:
            print(f"\n[ERROR]: An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()