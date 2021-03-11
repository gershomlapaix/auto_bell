# this is the file for bell configuration

# fetch list of the bells from the database
# list of the bells
domBell = "Dom Bell"
classBell = "Class Bell"
dinBell = "Dining Bell"

print('\n        Rename the bells\n')
print(f'1. {domBell}      2. {classBell}       3. {dinBell}\n')


class Switcher(object):
    def bell_numbers(self, argument):
        method_name = 'bellN0_'+str(argument)
        method = getattr(self, method_name, lambda: "Invalid bell number")
        return method()

    def bellN0_1(self):
        print(f'Current bell: {domBell}\n             ----------\n')

        # insert a new bell
        newDbName = input("Give new dom bell name : ")
        print(
            f'New Dom  bell name: {newDbName}\n                 ----------\n')

    def bellN0_2(self):
        print(f'Current bell: {classBell}\n             ----------\n')

        # insert a new bell
        newDbName = input("Give new class bell name : ")
        print(
            f'New class  bell name is : {newDbName}\n                 ----------\n')

    def bellN0_3(self):
        print(f'Current bell: {dinBell}\n             ----------\n')

        # insert a new bell
        newDbName = input("Give new dining bell name : ")
        print(
            f'New dining  bell name: {newDbName}\n                 ----------\n')


# instantiate the class
classInst = Switcher()
bell = int(input("Enter the bell (1-3) to configure: "))

if bell == 1:
    classInst.bell_numbers(bell)
elif bell == 2:
    classInst.bell_numbers(bell)
elif bell == 3:
    classInst.bell_numbers(bell)
else:
    print('No shuch bell')
