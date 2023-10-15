names = ['Kelvin', 'Ama', 'kweku', 'Duke', 'Derrick']
pos = -1
while True:
    if pos < -abs(len(names)):
        break
    else:
        print(names[pos])
        pos -= 1
