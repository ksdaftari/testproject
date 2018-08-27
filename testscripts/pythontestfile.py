from prettytable import PrettyTable

t = PrettyTable(['number', 'othernumber'])
for n in range(1, 10):
    t.add_row([n, n+5])
print(t)

# stuff
# another
