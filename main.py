# Import Decimal
import decimal
D = decimal.Decimal

# Import Data
from data import MENU, resources

# whether machine keep serving or not
is_off = False
# initialize money
money = D('0')


# Print Report
def print_resources():
	print(f"Water: {resources['water']}")
	print(f"Milk: {resources['milk']}")
	print(f"Coffee: {resources['coffee']}")
	print(f"Money: ${money}")


# Check if there are enough resources
def check_resources(selected_drink):
	is_ok = True
	for ingredient in MENU[selected_drink]["ingredients"]:
		if resources[ingredient] <= MENU[selected_drink]["ingredients"][ingredient]:
			print(f"Sorry there is not enough {ingredient}")
			is_ok = False
	return is_ok


# Calculate coins user inserted and return sum
def calculate_coins(inserted_quarters, inserted_dimes, inserted_nickles, inserted_pennies):
	qu = D('0.25') * inserted_quarters
	di = D('0.1') * inserted_dimes
	ni = D('0.05') * inserted_nickles
	pe = D('0.01') * inserted_pennies
	total_coins = qu + di + ni + pe
	return total_coins


# Compare received money and cost of drink that user choose
def compare_money(total_received, cost_of_drink):
	if total_received >= cost_of_drink:
		change = total_received - cost_of_drink
		print(f"Here is ${change} in change.")
		print(f"Here is your latte ☕ Enjoy!")
		return True
	else:
		print("Sorry that's not enough money. Money refunded.")
		return False


# deduct resources and add amount of sold
def make_coffee(selected_drink, received_money):
	for ingredient in MENU[selected_drink]["ingredients"]:
		resources[ingredient] -= MENU[selected_drink]["ingredients"][ingredient]
	# I don't know if I can use "global"
	global money
	money += received_money


while not is_off:
	# Ask user what kind of coffee do you want
	user_selected = input("What would you like? (espresso/latte/cappuccino): ")

	if user_selected == "report":
		print_resources()
	elif user_selected == "off":
		is_off = True
	else:
		if check_resources(user_selected):
			print("Please insert coins.")

			quarters = D(input("how many quarters?: "))
			dimes = D(input("how many dimes?: "))
			nickles = D(input("how many nickles?: "))
			pennies = D(input("how many pennies?: "))

			total = calculate_coins(quarters, dimes, nickles, pennies)
			cost = D(MENU[user_selected]["cost"])

			if compare_money(total, cost):
				make_coffee(user_selected, cost)



