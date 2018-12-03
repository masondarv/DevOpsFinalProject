import unittest

class LineItem:
  def __init__(self, description, amount):
    self.description = description
    self.amount = amount

class Expenses:
  def __init__(self):
    # Creates a list of expenses with descriptions and values
    self._expense_items = dict()
    self._total_expenses =0

	#adds expense item to the list of expenses
  def add_item(self, lineitem: LineItem, category):
    if lineitem.amount < 0:
      return "Invalid Amount"
    if category not in self._expense_items:
      self._expense_items[category] = dict()
    self._expense_items[category][lineitem.description] =lineitem.amount
    return "Line item Added"

  def calculate_total_expenses(self,):
    self._total_expenses = sum(sum(items.values()) for items in self._expense_items.values())
    print(self._total_expenses)
    return(self._total_expenses)

  def calculate_category_total(self, category):
    print("Total expenses for " + category)
    total = sum(self._expense_items[category].values())
    print(total)
    return total

  def meets_budget_category(self, budget, category):
    if category not in budget._categories:
      return"Category not found in budget"
    if category not in self._expense_items:
      return"Category not found in expenses"
	#compare calculated total for this budget category to specified category amount in budget
    if self.calculate_category_total(category) < budget._categories[category]:
      return category + " budget met"
    else:
      return category + " budget not met"

  def meets_total_budget(self, budget):
    self._total_expenses = sum(sum(items.values()) for items in self._expense_items.values())
    budget.calculate_total_budget()

    if self._total_expenses <= budget._total_budget:
      return "Total budget met"

    else:
      return "Failed to meet total budget"




class Category:
  def __init__(self, description, amount):
    self.description = description
    self.amount = amount


class Budget:

  def __init__(self):
    # Creates a dictionary of budget categories with descriptions and values
    self._categories = dict()
    self._monthly_income = 0
    self._total_budget =0
    self._margin = 0;

  def add_category(self, category: Category):
    if category.amount < 0:
      # print("Invalid amount")
      return "Invalid amount"
    if category.description in self._categories:
      # print("Category already exists")
      return "Category already exists"
    else:
      self._categories[category.description] = category.amount
      # print("Category added")
      return"Category added"
  def modify_category(self, description, amount):
    if amount <0:
      # print("Invalid amount")
      return "Invalid amount"
    if description not in self._categories:
      # print("Category does not exist")
      return"Category does not exist"

    else:
      self._categories[description] = amount
      # print("Category modified")
      return"Category modified"


  def set_income(self, income):
    self._monthly_income = income

  def calculate_total_budget(self):
    self._total_budget = sum(self._categories.values())
    # print(self._total_budget)
    return self._total_budget

  def calculate_margin(self):
    self._total_budget = sum(self._categories.values())
    self._margin = self._monthly_income - self._total_budget
    # print(margin)
    return self._margin

class integrationTest(unittest.TestCase):

  def test_0_meets_budget_category(self):
    print("Starting meets budget category test\n")
    #instantiate Expense class
    myExpenses = Expenses()
    #instantiate Budget class
    myBudget = Budget()
    category1 = Category('Food', 100)
    category2 = Category('Leisure', 100)
    expense1 = LineItem("Mcdonalds 11/18/18", 5.50)
    expense2 = LineItem("Pizzeria Local 11/12/18", 80.0)
    expense3 = LineItem("Sprouts 11/22/18", 100.0)
    expense4 = LineItem("Gas 11/1/18", 50)

    myBudget.add_category(category1)
    myBudget.add_category(category2)
    myExpenses.add_item(expense1, 'Food')
    myExpenses.add_item(expense2, 'Food')
    myExpenses.add_item(expense4, 'Gas')

    self.assertEqual(myExpenses.meets_budget_category(myBudget, 'Food'), "Food budget met")
    print("Food budget met, as expected")
    print("\n")
    myExpenses.add_item(expense3,'Food')

    self.assertEqual(myExpenses.meets_budget_category(myBudget, 'Food'), "Food budget not met")
    print("Food budget not met, as expected")
    print("\n")

    self.assertEqual(myExpenses.meets_budget_category(myBudget, 'Leisure'), "Category not found in expenses")
    print("Category not found in expenses, as expected")
    print("\n")

    self.assertEqual(myExpenses.meets_budget_category(myBudget, 'Gas'), "Category not found in budget")
    print("Category not found in budget, as expected")
    print("\n")

  def test_1_meets_total_budget(self):
    print("Starting meets total budget test\n")
    #instantiate Expense class
    myExpenses = Expenses()
    #instantiate Budget class
    myBudget = Budget()
    category1 = Category('Food', 100)
    category2 = Category('Leisure', 100)
    expense1 = LineItem("Mcdonalds 11/18/18", 5.50)
    expense2 = LineItem("Pizzeria Local 11/12/18", 80.0)
    expense3 = LineItem("Sprouts 11/22/18", 100.0)
    expense4 = LineItem("Climbing 11/1/18", 20)

    myBudget.add_category(category1)
    myBudget.add_category(category2)
    myExpenses.add_item(expense1, 'Food')
    myExpenses.add_item(expense2, 'Food')
    myExpenses.add_item(expense4, 'Leisure')

    self.assertEqual(myExpenses.meets_total_budget(myBudget), "Total budget met" )
    print("Total budget met after initial expenses and budget were set.")
    print("\n")

    myExpenses.add_item(expense3, 'Food')
    self.assertEqual(myExpenses.meets_total_budget(myBudget), "Failed to meet total budget" )
    print("Total budget not met after adding expense.")
    print("\n")

    myBudget.modify_category('Food', 200)

    self.assertEqual(myExpenses.meets_total_budget(myBudget), "tTotal budget met" )
    print("Total budget met after increasing Food budget.")
    print("\n")

if __name__ == '__main__':
    unittest.main()
