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


class expenseTest(unittest.TestCase):

  def test_0_add_item(self):
    print("Starting add item test\n")
    #instantiate Expense class
    myExpenses = Expenses()
    expense1 = LineItem("Mcdonalds 11/18/18", 5.50)
    expense2 = LineItem("Lift Tickets 11/1/18", 130.0)
    expense3 = LineItem("Chipotle 11/12/18", 8.00)
    expense4 = LineItem("bad expense 00/0/00", -453)

    self.assertEqual(myExpenses.add_item(expense1, 'Food'), "Line item Added jk")
    print("Added Line item 1 to and created Food category")
    print("Current Expense List")
    print(myExpenses._expense_items)
    print("\n")

    self.assertEqual(myExpenses.add_item(expense2, 'Leisure'), "Line item Added")
    print("Added Line item 2 and created Leisure category")
    print("Current Expense List")
    print(myExpenses._expense_items)
    print("\n")

    self.assertEqual(myExpenses.add_item(expense3, 'Food'), "Line item Added")
    print("Added Line item 3 to Food category")
    print("Current Expense List")
    print(myExpenses._expense_items)
    print("\n")

    self.assertEqual(myExpenses.add_item(expense4, 'Food'), "Invalid Amount")
    print("Attempted to add a line item with an invalid amount")
    print("Current Expense List")
    print(myExpenses._expense_items)
    print("\n")

  def test_1_calculate_category_total(self):
    print("Starting calculate category total test\n")
    #instantiate Expense class
    myExpenses = Expenses()
    expense1 = LineItem("Mcdonalds 11/18/18", 5.50)
    expense2 = LineItem("Lift Tickets 11/1/18", 130.0)
    expense3 = LineItem("Chipotle 11/12/18", 8.00)
    expense4 = LineItem("Red Rocks 11/5/18", 70.0)
    expense5 = LineItem("Sprouts 11/22/18", 100)

    expected_food_total1 = 13.50
    expected_food_total2 = 113.50
    expected_leisure_total = 200

    myExpenses.add_item(expense1, 'Food')
    myExpenses.add_item(expense3, 'Food')

    print("Calculated total money spent on food after adding two items")
    self.assertEqual(myExpenses.calculate_category_total('Food'), expected_food_total1)
    print("Current list of food expenses")
    print(myExpenses._expense_items['Food'])
    print("\n")

    myExpenses.add_item(expense2, 'Leisure')
    myExpenses.add_item(expense4, 'Leisure')

    print("Calculated total money spent on leisure after adding two items")
    self.assertEqual(myExpenses.calculate_category_total('Leisure'), expected_leisure_total)
    self.assertEqual(myExpenses.calculate_category_total('Food'), expected_food_total1)
    print("Current list of leisure expenses")
    print(myExpenses._expense_items['Leisure'])
    print("\n")

    myExpenses.add_item(expense5, 'Food')

    print("Calculated total money spent on food after adding a third item")
    self.assertEqual(myExpenses.calculate_category_total('Food'), expected_food_total2)
    print("Current list of food expenses")
    print(myExpenses._expense_items['Food'])
    print("\n")

  def test_2_calculate_total_expenses(self):
    print("Starting calculate total expenses test\n")
    #instantiate Expense class
    myExpenses = Expenses()
    expense1 = LineItem("Mcdonalds 11/18/18", 5.50)
    expense2 = LineItem("Lift Tickets 11/1/18", 130.0)
    expense3 = LineItem("Chipotle 11/12/18", 8.00)
    expense4 = LineItem("Red Rocks 11/5/18", 70.0)
    expense5 = LineItem("Gas 11/22/18", 50)

    expected_total1 = 213.50
    expected_total2 = 263.50


    myExpenses.add_item(expense1, 'Food')
    myExpenses.add_item(expense3, 'Food')
    myExpenses.add_item(expense2, 'Leisure')
    myExpenses.add_item(expense4, 'Leisure')
    self.assertEqual(myExpenses.calculate_total_expenses(), expected_total1)
    print("Calculated total expenses after adding 4 line items")
    print("Current list of expenses")
    print(myExpenses._expense_items)
    print("Total Expenses")
    print(myExpenses._total_expenses)
    print("\n")

    myExpenses.add_item(expense5, 'Gas')
    self.assertEqual(myExpenses.calculate_total_expenses(), expected_total2)
    print("Recalculated total expenses after adding an additional item to expense list")
    print("Current list of expenses")
    print(myExpenses._expense_items)
    print("Total Expenses")
    print(myExpenses._total_expenses)
    print("\n")

if __name__ == '__main__':
    unittest.main()
