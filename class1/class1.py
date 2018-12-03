import unittest



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


class budgetTest(unittest.TestCase):

  #instantiate the budget class
  myBudget = Budget()

  #checks the add category method
  def test_0_add_category(self):
    #instantiate the budget class
    myBudget = Budget()
    print("Start add category test\n")
    category1 = Category('Food', 450)
    category2 = Category('Leisure', 600)
    category3 = Category('Rent', -34)

    self.assertEqual(myBudget.add_category(category1), "Category added")
    self.assertEqual(myBudget._categories['Food'], 450)
    print("Added Food Category")
    print("Current Budget")
    print(myBudget._categories)
    print("\n")

    self.assertEqual(myBudget.add_category(category2), "Category added")
    self.assertEqual(myBudget._categories['Leisure'], 600)

    print("Added Leisure Category")
    print("Current Budget")
    print(myBudget._categories)
    print("\n")

    self.assertEqual(myBudget.add_category(category1), "Category already exists")

    print("Attempted to add an existing category")
    print("Current Budget")
    print(myBudget._categories)
    print("\n")

    self.assertEqual(myBudget.add_category(category3), "Invalid amount")
    print("Attempted to add a category with an invalid amount")
    print("Current Budget")
    print(myBudget._categories)
    print("\n")

  def test_1_modify_category(self):
    #instantiate the budget class
    myBudget = Budget()

    print("Start modify category test\n")
    category1 = Category('Food', 450)
    myBudget.add_category(category1)
    print("Added Food Category")
    print("Current Budget")
    print(myBudget._categories)
    print("\n")

    self.assertEqual(myBudget.modify_category('Food', 565), "Category modified")
    self.assertEqual(myBudget._categories['Food'], 565)
    print("Modified Food Category")
    print("Current Budget")
    print(myBudget._categories)
    print("\n")

    self.assertEqual(myBudget.modify_category('Gas', 154), "Category does not exist")
    print("Attempted to modify a nonexistent category")
    print("Current Budget")
    print(myBudget._categories)
    print("\n")

    self.assertEqual(myBudget.modify_category('Food', -1), "Invalid amount")
    self.assertEqual(myBudget._categories['Food'], 565)

    print("Attempted to modify an existing category with an invalid amount")
    print("Current Budget")
    print(myBudget._categories)
    print("\n")

  def test_2_calculate_total_budget(self):
    #instantiate the budget class
    myBudget = Budget()
    print("Start calculate total budget test\n")
    category1 = Category('Food', 450)
    category2 = Category('Leisure', 600)
    expected_total1 = 1050
    expected_total2 = 1250

    myBudget.add_category(category1)
    myBudget.add_category(category2)
    self.assertEqual(myBudget.calculate_total_budget(), expected_total1)
    print("Calculated budget total after adding two categoreies")
    print("Current Budget")
    print(myBudget._categories)
    print("Budget Total")
    print(myBudget._total_budget)
    print("\n")
    myBudget.modify_category('Leisure', 800)
    self.assertEqual(myBudget.calculate_total_budget(), expected_total2)
    print("Calculated budget total after modifiying Leisure category")
    print("Current Budget")
    print(myBudget._categories)
    print("Budget Total")
    print(myBudget._total_budget)
    print("\n")

  def test_3_calculate_margin(self):
    #instantiate the budget class
    myBudget = Budget()
    print("Start calculate margin test\n")
    category1 = Category('Food', 450)
    category2 = Category('Leisure', 600)

    monthly_income1 = 1500
    monthly_income2 = 1000

    expected_margin1 = 450
    expected_margin2 = -50
    expected_margin3 = 150

    myBudget.add_category(category1)
    myBudget.add_category(category2)
    myBudget.set_income(monthly_income1)
    self.assertEqual(myBudget.calculate_margin(), expected_margin1)
    print("Calculated budget margin after adding two categories and monthly income")
    print("Current Budget")
    print(myBudget._categories)
    print("Budget Total")
    print(myBudget._total_budget)
    print("Monthly Income")
    print(myBudget._monthly_income)
    print("Budget Margin")
    print(myBudget._margin)
    print("\n")

    myBudget.set_income(monthly_income2)
    self.assertEqual(myBudget.calculate_margin(), expected_margin2)

    print("Calculated budget margin after changing monthly income")
    print("Current Budget")
    print(myBudget._categories)
    print("Budget Total")
    print(myBudget._total_budget)
    print("Monthly Income")
    print(myBudget._monthly_income)
    print("Budget Margin")
    print(myBudget._margin)
    print("\n")
    myBudget.modify_category('Leisure', 400)
    self.assertEqual(myBudget.calculate_margin(), expected_margin3)

    print("Calculated budget margin after modifying Leisure category")
    print("Current Budget")
    print(myBudget._categories)
    print("Budget Total")
    print(myBudget._total_budget)
    print("Monthly Income")
    print(myBudget._monthly_income)
    print("Budget Margin")
    print(myBudget._margin)


if __name__ == '__main__':
    unittest.main()
