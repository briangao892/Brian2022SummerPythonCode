import sys

vars = 'a'
for i in range(50):
    print(vars)
    vars = vars + 'a'

for i in range(50):
    sys.stdout.write("a")
print()
for i in range(50):
    print(vars)
    vars = vars[:-1]
