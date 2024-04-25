def input_data():
    f_name = input("Enter first name: ")
    s_name = input("Enter surname: ")
    m_name = input("Enter middle name: ")
    phone = input("Enter phone number: ")
    
    contact = {'first_name': f_name,
               'second_name': s_name,
               'middle_name': m_name,
               'phone_number': phone
               }
    return contact

def add_new_contact():
    # if not check_data(contact):
    #   return False
    contact = input_data()
    with open('phonebook.txt', 'a', encoding = 'utf-8') as file:
        line = ",".join(contact.values())
        file.write(line + '\n')
    # return True 

def open_phonebook():
    title = ["Name", "Family name", "Middle name", "Phone number"]
    with open('phonebook.txt', 'r', encoding = 'utf-8') as file:
        print("\t\t".join(title))
        for line in file:
            print("\t\t".join(line.split(",")))

def find_contact():
    # print(f"Search by \n1 name\n2 family name\n3 middle name\n4 number\n0 exit")
    title = ["Name", "Family name", "Middle name", "Phone number"]
    s_name = input("Enter family name: ")
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print("\t\t".join(title))
        for line in file:
            contact_info = line.strip().split(",")
            if s_name == contact_info[1]:
                print("\t\t".join(contact_info))
      

# def copy_files():
def copy_contact():
    print("list of available contacts for copying: ")
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        date_contacts_list = file.readlines()
   
    number_contact = int(input('Enter required phone number: '))
    contact_copied = date_contacts_list[number_contact - 1].strip()
    with open('contact_copied.txt', 'a', encoding='utf-8') as copied_file:
        copied_file.write(f'{contact_copied} \n\n')

    print('Contact copied successfully')

def main():
    isStop = 1
    while isStop != 0:
        print("Select an action: \n1 find\n2 add\n3 open\n4 copy\n0 exit")
        isStop = int(input(">"))
        if isStop == 1:
            find_contact()
        elif isStop == 2:
            add_new_contact()
        elif isStop == 3:
            open_phonebook()
        elif isStop == 4:
            copy_contact()
        elif isStop == 0:
            print("Bye bye!")
            break
        else:
            print("Invalid input! Please select a valid option.")
        input("Press Enter to continue")
main()



