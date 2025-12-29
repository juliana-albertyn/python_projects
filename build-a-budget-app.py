"""
Build-a-budget-app
A freeCodeCamp certification project:
Build a simple budget app that tracks spending in different categories
and can show the relative spending percentage on a graph.
"""

__author__ = "Juliana Albertyn"
__email__ = "julie_albertyn@yahoo.com"
__status__ = "development"  # or testing or production
__date__ = "2025-12-29"

import math
from typing import List

key_amount = "amount"
key_description = "description"


class Category:
    """
    A simple representation of a budget.

    This class provides methods to deposit, withdraw, transfer to another category,
    get the balance, check the balance before withdrawing and transferring money,
    and print the class.
    It is intended as a demonstration of object-oriented programming concepts.

    Attributes
    ----------
    name : str
        The name of the spending category.

    Methods
    -------
    deposit(amount: float) -> None
        Add money to the account.
    withdraw(amount: float) -> None
        Remove money from the account if sufficient funds exist.
    get_balance() -> float
        Return the current balance.
    """

    def __init__(self, name: str) -> None:
        """Initialise a new Category instance.

        Args:
        name (str): The name of the category.

        Attributes:
        name (str) : The name of the category
        ledger (list[dict[str, float]]): A list of transaction records, each with amount and description.
        """
        self.name = name
        self.ledger = []

    def __str__(self) -> str:
        """Returns a string representation of the class.

        Returns:
        str : Returns:
        str: A formatted string showing the category name and transactions.
        """
        result = f"{self.name.center(30, "*")}\n"
        transaction = dict()
        for transaction in self.ledger:
            amount = f"{transaction[key_amount]:.2f}"
            result += f"{transaction[key_description][0:23]:<23}{amount:>7}\n"
        result += f"Total: {self.get_balance()}"
        return result

    def deposit(self, amount: float, description: str = ""):
        """Deposit transaction.

        Args:
        amount (float): Amount to deposit.
        description (str): Description of the transaction. Defaults to empty string.

        Raises:
        ValueError : if deposit amount is zero or negative.
        """
        if amount <= 0:
            raise ValueError("Deposits must be a positive amount")
        else:
            self.ledger.append({key_amount: amount, key_description: description})

    def withdraw(self, amount: float, description: str = "") -> bool:
        """Withdrawal transaction.

        Args:
        amount (float): Amount to withdraw.
        description (str): Description of the transaction. Defaults to empty string.

        Returns:
        bool: True if withdrawal succeeded, False if insufficient funds.

        Raises:
        ValueError: if withdrawal amount is zero or negative.
        """
        if amount <= 0:
            raise ValueError("Withdrawals must be a positive amount")
        else:
            if self.check_funds(amount):
                self.ledger.append({key_amount: -amount, key_description: description})
                return True
            else:
                return False

    def get_balance(self) -> float:
        """Returns the balance.

        Returns:
        float : The balance for this category.
        """
        balance = 0
        for transaction in self.ledger:
            balance += transaction[key_amount]
        return balance

    def transfer(self, amount: float, destination: "Category") -> bool:
        """Transfer money from one Category to another

        Args:
        amount (float): The amount to be transferred.
        destination (Category): Which category must receive the money.

        Returns:
        bool: True if the transfer succeeded, False otherwise.
        """
        if self.check_funds(amount):
            if self.withdraw(amount, f"Transfer to {destination.name}"):
                destination.deposit(amount, f"Transfer from {self.name}")
                return True
            else:
                return False
        else:
            return False

    def check_funds(self, amount: float) -> bool:
        """Checks whether the amount is available to withdraw or transfer.

        Args:
        amount (float): Amount of withdrawal or transferral.

        Returns:
        bool : True if the amount is less than or equal to the balance.
        """
        if amount <= self.get_balance():
            return True
        else:
            return False


def create_spend_chart(categories: list[Category]) -> str:
    """Returns a bar-chart string of percentage spent per category.

    Args:
    categories (list[Category]):  A list of categories to add to the spend chart.

    Returns:
    str : a bar-chart str.
    """
    result = "Percentage spent by category"
    total_spent = 0
    spent_per_category = dict()
    for category in categories:
        spent_per_category[category.name] = 0
        for transaction in category.ledger:
            if (
                transaction[key_amount] < 0
                and not "Transfer" in transaction[key_description]
            ):
                spent_per_category[category.name] += transaction[key_amount]
        total_spent += spent_per_category[category.name]
    for category in categories:
        spent_per_category[category.name] = math.floor(
            (spent_per_category[category.name] * 100) / total_spent
        )
    indent = " " * 4
    max_length = 0
    for category in categories:
        if len(category.name) > max_length:
            max_length = len(category.name)
    for p in range(100, -10, -10):
        s = f"{p:>3}|"
        for category in categories:
            if spent_per_category[category.name] >= p:
                s += "o".center(3, " ")
            else:
                s += " ".center(3, " ")
        result += f"\n{s} "
    s = f"{indent}{"-" * (3 * len(categories) + 1)}"
    result += f"\n{s}"
    for i in range(0, max_length, 1):
        s = ""
        for index, category in enumerate(categories):
            if index == 0:
                s = indent
            if i < len(category.name):
                s += category.name[i].center(3, " ")
            else:
                s += " " * 3
        result += f"\n{s} "
    return result


try:
    food = Category("Food")
    food.deposit(1000, "deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(10.99, "dress")
    house = Category("House")
    food.transfer(200, house)
    house.withdraw(200, "roof")
    print(f"{food}\n")
    print(f"{clothing}\n")
    print(f"{house}\n")
    print(create_spend_chart([food, clothing, house]))
except ValueError as e:
    print(f"Invalid transaction: {e}")
