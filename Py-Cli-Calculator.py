print("""
       ***********************************************************
       ******  Welcome to Py Cli Calculator Version 1.0  ********  
       ===========================================================
""")
def print_sol(sol): # Print result function
	print("Solution = > " + str(sol))
	print("""
==============================================
**********************************************

	""")

def add_num(num1 , num2): # Defined Addition
	sol = num1 + num2
	print_sol(sol)

def sub_num(num1 , num2): # Defined Subtraction
	sol = num1 - num2
	print_sol(sol)

def mul_num(num1 , num2): # Defined Multiplication
	sol = num1 * num2
	print_sol(sol)

def div_num(num1 , num2): # Defined Division
	sol = num1 / num2
	print_sol(sol)

while True:
	print("Choose Your Operation with Two Numbers")
	print("""
		Press A For Addition
		Press S For Substration
		Press M For Multiplication
		Press D For Division

		Press Q For EXIT
		""")
	option = str.lower(input("Select from A S M D >> ")) # Option input field
	if option in ("a" , "s" , "m" , "d" ):
		num1 = int(input("Enter 1st Number => "))
		num2 = int(input("Enter 2nd Number => "))
		if option == "a": # Add function 
			add_num(num1,num2)
		if option == "s": # Subtract function
			sub_num(num1,num2)
		if option == "m": # Multiply function
			mul_num(num1,num2)
		if option == "d": # Divide function
			div_num(num1,num2)
	elif option == "q":
		exit()

	else : 
		print("""
	 =============================================
		  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
		  !!!!!!!![Invalid Input]!!!!!!!!!   
		  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  
	 =============================================
		""")

	
