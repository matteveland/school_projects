
"""Option #1: Program Corrections, Lessons Learned, and Vehicle Inventory Program
Your portfolio project consists of three components:

Program corrections
Lessons learned reflection
Final program
Assignment Instructions

Program corrections:

Make appropriate corrections to all the programming assignments submitted as Critical Thinking Assignments from Modules 1-6.
Submit the programs along with a carefully outlined description of corrections made in order for programs to run correctly.
Lessons learned reflection:

Create a 2-3 page summary that outlines the lessons learned in this Basic Programming course.

Final program:
Create a final program that meets the requirements outlined below.

Create an automobile class that will be used by a dealership as a vehicle inventory program.  The following attributes should be present in your automobile class:
private string make
private string model
private string color
private int year
private int mileage

Your program should have appropriate methods such as:

constructor
add a new vehicle
remove a vehicle
update vehicle attributes
At the end of your program, it should allow the user to output all vehicle inventory to a text file.

Your final program submission materials must include your source code and screenshots of the application executing the application and the results.
Assignment Submission Instructions
Zip up the following files and submit in one file:

Compiled Module 1-6 programs with corrections
Lessons learned reflection
Final program course code and application screenshots"""

inventory_list = {}



inventory_list = {1: [2020, 'Ford', 'Bronco', 12, 'white'], 2: [2019, 'Chevy', 'Tahoe', 43, 'Black']}

print('There are preloaded items in the inventory to ease with menu selection.\n')
class inventory(object):

    counter = max(inventory_list) + 1
    
    def __init__(self, id):
        self.id = id

    def menu():
        print('n: Enter New Vehicle')
        print('u: Update Vehicle')
        print('d: Delete Vehicle')
        print('p: Print Vehicle')
        print('x: Export Inventory Information')
        print('q: Quit')
        print('\n')

    def new_add():
        new_vehicle = []
        print('\n')
        print('Enter Vehicle information')
        year = input('Please enter the Vehicle Year (4 digits): ')
        while True:
            try:
                if len(str(year)) < 4:
                    year = input('Please enter the Vehicle Year (4 digits): ')
                    continue
                elif len(str(year)) > 4:
                    year = input('Please enter the Vehicle Year (4 digits): ')
                    continue
                else: pass

                year = int(year)

            except ValueError:
                # Handle the exception
                year = input('Please enter the Vehicle Year (4 digits): ')
                continue
            break

        make = input('Enter Vehicle Make: ')
        model = input('Enter Vehicle Model: ')
        miles = input('Enter Vehicle Mileage: ')
        while True:
            try:
                miles = int(miles)

            except ValueError:
                # Handle the exception
                miles = input('Please enter the mileage as numbers: ')
                continue
            break
        color = input('Enter Vehicle Color: ')


        #find last dict value to add into for new dict entry
        #new_vehicle = [2020, 'toyota', 'tundra', 12, 'blue']
        new_vehicle = [year, make, model, miles, color]
        inventory_list[inventory.counter] = new_vehicle

        # increment counter for dict usage for lot inventory
        inventory.counter += 1
        print('Vehicle Information successfully added.')
        print('\n')
        inventory.menu()

    def display_inventory():
        for k, v in inventory_list.items():
            print('Vehicle Number: ', k)
            print('Vehicle Year: ', v[0])
            print('Vehicle Make: ', v[1])
            print('Vehicle Model: ', v[2])
            print('Vehicle Mileage: ', v[3])
            print('Vehicle Color: ', v[4])
            print('\n')
        inventory.menu()

    def edit_inventory(id):
        id = id
        print('\n')
        print('Edit Vehicle')
        if id in inventory_list.keys():
            for v in inventory_list.values():
                print('Selection item to edit: ')
                print('1: Vehicle Year: ')
                print('2: Vehicle Make: ')
                print('3: Vehicle Model: ')
                print('4: Vehicle Mileage: ')
                print('5: Vehicle Color: ')
                print('\n')

                edit = input('Selection item to edit: ')

                if edit == '1':
                    print('Current Vehicle Year', v[0])
                    year = input('Please enter the Vehicle Year (4 digits): ')
                    while True:
                        try:
                            if len(str(year)) < 4:
                                year = input('Please enter the Vehicle Year (4 digits): ')
                                continue
                            elif len(str(year)) > 4:
                                year = input('Please enter the Vehicle Year (4 digits): ')
                                continue
                            else: pass

                            year = int(year)
                            update = [year, v[1], v[2], v[3], v[4]]
                            inventory_list.update({id : update})
                            break

                        except ValueError:
                            # Handle the exception
                            year = input('Please enter the Vehicle Year (4 digits): ')
                            continue
                        break


                elif edit == '2':
                    print('Current Vehicle Make', v[1])
                    make = input('Enter Vehicle Make: ')
                    update = [v[0], make, v[2], v[3], v[4]]
                    inventory_list.update({id : update})
                    break

                elif edit == '3':
                    print('Current Vehicle Model', v[2])
                    model = input('Enter NEW Vehicle Model: ')
                    update = [v[0], v[1], model, v[3], v[4]]
                    inventory_list.update({id : update})
                    break

                elif edit == '4':
                    print('Current Vehicle Mileage', v[3])
                    miles = input('Enter NEW Vehicle Mileage: ')
                    while True:
                        try:
                            miles = int(miles)
                            update = [v[0], v[1], v[2], miles, v[4]]
                            inventory_list.update({id : update})
                            break
                        except ValueError:
                            # Handle the exception
                            miles = input('Please enter the mileage as numbers: ')
                            continue
                        break

                elif edit == '5':
                    print('Current Vehicle Color', v[4])
                    color = input('Enter NEW Vehicle Color: ')
                    update = [v[0], v[1], v[2], v[3], color]
                    inventory_list.update({id : update})
                    break
                break

        else:
            print('Select item ID in inventory')
        print('\n')
        inventory.display_inventory()
        print('\n')


    def delete_inventory(id):
        id = id
        del inventory_list[id]
        print('Vehicle %s successfully removed!' % id)
        print('\n')
        print('Vehicles remaining in the inventory')
        print('\n')
        inventory.display_inventory()
    
    def export_inventory():
        while True:
            try:
                # create file is does not exist
                export = open("inventory_export.txt", "x")
                export.write("{\n")
                for k, v in inventory_list.items():
                    export.write (f"Vehicle Number: %d\n\tVehicle Year: %d\n\t Vehicle Make: %s\n\tVehicle Model: %s\n\tVehicle Mileage: %d\n\tVehicle Color: %s\n" % (k, v[0], v[1], v[2], v[3], v[4])) 
                    export.write("}")
                export.close()
                print('Your file was successfully create and export.')
                break
            except FileExistsError:
                # write to file if exist
                export = open("inventory_export.txt", "w")
                export.write("{\n")
                for k, v in inventory_list.items():
                    export.write (f"Vehicle Number: %d\n\tVehicle Year: %d\n\tVehicle Make: %s\n\tVehicle Model: %s\n\tVehicle Mileage: %d\n\tVehicle Color: %s\n" % (k, v[0], v[1], v[2], v[3], v[4])) 
                    export.write("}")
                export.close()
                print('Your file was successfully and export.')
                break
            export = open("inventory_export.txt", "x")
            break
        print('\n')
        inventory.menu()


print('Welcome to Car Thingy!')
inventory.menu()
command = input('Please enter a command: ')
command_list = ('n', 'u', 'd', 'p', 'x','q')

while True:
    if command in command_list:

        if command == 'n':
            inventory.new_add()
            command = input('Please enter a command: ')

        elif command == 'u':
            inventory.display_inventory()
            id = int(input('Enter Vehicle ID for update: '))
            inventory.edit_inventory(id)
            command = input('Please enter a command: ')

        elif command == 'd':
            id = int(input('Enter Vehicle ID'))
            inventory.delete_inventory(id)

            command = input('Please enter a command: ')

        elif command == 'p':
            inventory.display_inventory()
            command = input('Please enter a command: ')

        elif command == 'x':
            inventory.export_inventory()
            command = input('Please enter a command: ')

        elif command == 'q':
            print('exiting')
            break
    else:
        print('Invalid selection')
        inventory.menu()
        command = input('Please enter a command: ')

else:
    print('Invalid selection')
    command = input('Please enter a command: ')

