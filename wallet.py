class Wallet:
    def __init__(self):
        self.balance = 0

    def display_balance(self):
        print(f"Баланс: {self.balance} грн")

    def add_money(self, amount):
        self.balance += amount
        print(f"Додано {amount} грн. Новий баланс: {self.balance} грн")

    def spend_money(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Витрачено {amount} грн. Новий баланс: {self.balance} грн")
        else:
            print("Недостатньо коштів")


# test_wallet.py

import pytest
from wallet import Wallet


@pytest.fixture
def wallet():
    return Wallet()


def test_initial_balance(wallet):
    assert wallet.balance == 0


def test_add_money(wallet):
    wallet.add_money(50)
    assert wallet.balance == 50


def test_spend_money(wallet):
    wallet.add_money(100)
    wallet.spend_money(50)
    assert wallet.balance == 50


def test_insufficient_funds(wallet, capsys):
    wallet.spend_money(20)
    captured = capsys.readouterr()
    assert "Недостатньо коштів" in captured.out


def test_display_balance(wallet, capsys):
    wallet.add_money(30)
    wallet.display_balance()
    captured = capsys.readouterr()
    assert "Баланс: 30 грн" in captured.out


def main():
    wallet = Wallet()

    while True:
        print("\n1. Переглянути баланс")
        print("2. Додати гроші")
        print("3. Витратити гроші")
        print("0. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            wallet.display_balance()
        elif choice == "2":
            amount = float(input("Введіть суму для додавання: "))
            wallet.add_money(amount)
        elif choice == "3":
            amount = float(input("Введіть суму для витрати: "))
            wallet.spend_money(amount)
        elif choice == "0":
            print("Дякую за використання гаманця. До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте знову.")


if __name__ == "__main__":
    main()
