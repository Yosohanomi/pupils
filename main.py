import time

class Pupils():
    def __init__(self, surname, name, mark):
        self.surname = surname
        self.name = name
        self.mark = mark

pupils = []
def print_class(pupils):
    for pupil in pupils:
        print(pupil.surname, pupil.name, "- ", pupil.mark)
    print("\n")

def print_five(pupils):
    print("Відмінники:")
    for pupil in pupils:
        if pupil.mark == 5:
            print(pupil.surname)
    print('\n')

def find_average(pupils):
    average = 0
    for pupil in pupils:
        average += pupil.mark
    average /= len(pupils)
    print("Середня оцінка класу: ", average)

start_time = time.time()
with open("pupils.txt", "r", encoding="UTF-8") as file:
    for line in file:
        data = line.split(" ")
        pupil = Pupils(data[0], data[1], data[2])
        pupils.append(pupil)

print_class(pupils)
print_five(pupils)
find_average(pupils)
print("Час виконання: ", (time.time()-start_time), ' секунд')
