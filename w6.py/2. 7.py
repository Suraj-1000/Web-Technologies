def check():
    """this function is used to check the a specific key and value exist in a dictinary"""
    students=[
        {"student_id": 1, "name": "Jean Castro", "class": "V"},
        {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
        {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'},
        {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'},
        {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
        ]
    key_term=input("enter the key:")
    value_term=input("enter the value:")
    for student in students:
        if key_term in student.key() and value_term in student.values():
            print(f"key: '{key_term}' and value '{value_term}' do exist")
            break
        else:
                print(f"key: 'key{key_term}' and value '{value_term}'doesn't exist")