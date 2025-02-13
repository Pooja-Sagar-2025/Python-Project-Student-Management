stud = {}
while True:
    print('\n')
    print('1:Add Student')
    print('2:Remove Student')
    print('3:Search Student')
    print('4:Exit')
    print('\n')
    ch = int(input('Enter your choice:'))
    if ch == 1:
         no_of_student = int(input('How Many No.Of Student To Be Added:'))
         i=1
         while i <= no_of_student:
             print('\n')
             roll_no = input('Enter student roll number:')
             name = input('Enter student name:')
             marks = input('Enter english marks:')
             i=i+1
             stud[roll_no] = {}
             stud[roll_no]['name'] = name
             stud[roll_no]['marks'] = {}
             stud[roll_no]['marks']['eng'] = marks
         else:
             print('\n')
             print('Student data:',stud)
    elif ch == 2:
        print('\n')
        roll_no = input('Enter roll no of student that you want to delete:')

        if roll_no in stud:
            del(stud[roll_no])
            print('\n')
            print('Dictionary after removing desire student',stud)
        else:
            print('\n')
            print('Student does not exist')
    elif ch == 3:
        print('\n')
        roll_no = input('Enter student roll no to be search.')
        if roll_no in stud:
            print('Student is present in database:',stud[roll_no])
        else:
            print('Student is not present in database!!!!!PLEASE ADD STUDENT!!!!!')
    elif ch == 4:
        print('Thanks for using system!!!!')
        break
else:
    print('Success')
