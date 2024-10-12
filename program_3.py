# Program #3: Tax Rate
#date = 10.11.24
#Programmer = Caiden Nelson
# A retail company must file a monthly sales tax report listing the total sales for the month,
# and the amount of state and county sales tax collected.
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.
# Write a program that asks the user to enter the total sales for the month.
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program



#def num(sale):
#    return 5*sale
#sale = int(input("what"))
#print(num(sale))
def tax_calculator():
    #find total sales
    sale = int(input("what are your sales "))
    #calculate State tax
    def stateTax(sale):
        return round((.05*sale),2)
    #calculate county tax
    def countyTax(sale):
        return round((.025*sale),2)
    #display amount owed

    #calculate total tax
    def totalTax():
        return round((countyTax(sale) + stateTax(sale)),2)

    #display amount owed
    print('you owe the county', countyTax(sale), 'dollars in taxes')
    print('you owe the state government', stateTax(sale), 'dollars in taxes')
    print('in total you owe',totalTax(),'dollars in taxes')

tax_calculator()
