from prettytable import PrettyTable

table =  PrettyTable()
table.add_column("Name",["Jaya","Vijaya","Siddhi","Buddhi"],'c','m')
table.add_column("Meaning",["Win","Victory","Accomplishment","Intellect"],'c','m')

print(table)
table.add_row(["Namaste","Bow down to divine light inside you"])
table.align = 'r'
print(table)