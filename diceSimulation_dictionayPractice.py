
#Dice simulation
import random
def simulate_diceroll():
    "1,2,3,4,5,6"
    first_roll = random.randrange(1,7)
    second_roll = random.randrange(1,7)
    
    total = first_roll + second_roll
    
    #print(first_roll)
    #print(second_roll)
    
    return total

def main():
    dictionary1 = {}
    for _ in range(1000):
        total = simulate_diceroll()
        if total not in dictionary1:
            dictionary1[total] = 1
        else:
            dictionary1[total] += 1
    display_summary(dictionary1)

def display_summary(sample_dictionary):
    
    print ("{:<15} {:<25} {:<7}".format('Total','Simulated Percent','Expected Percent'))
    #print("Total     Simulated Percent     Expected Pecent")
    for total, frequency in sample_dictionary.items():
        #print(f'{total}      {round((frequency/1000)*100, 4)}       {round((frequency/11) * 100,2 )}')
        print ("{:<18} {:<39} {:<10}".format(total, round((frequency/1000)*100, 4), round((frequency/11) * 100,2 )))
        
main()
