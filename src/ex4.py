def ex4():

    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]

    print(get_people(people_list))


def get_people(people_list):
    list_age15andover = [p['name'] for p in people_list if p['age'] >= 15]
    return list_age15andover
   
  
ex4()