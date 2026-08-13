# Given a list of emails, use a set to remove duplicates and count unique domains
list = [
    'siddhu@gmail.com',
    'raghu@yahoo.com',
    'lakshmi@gmail.com',
    'srinu@x.com']
set = {email.split('@')[1] for email in list}
print(set)
print(len(set))

# Given employee_name: salary, find the top 3 highest-paid employees.
details = {
    'Siddhu': 200000
    'Raghu': 100000
    'Srinu': 230000
}
