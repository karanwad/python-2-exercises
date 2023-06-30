def ex2():
    
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    filtered_list = filter_males(people_list)
    print(filtered_list)

# if __name__ == '__main__':

def filter_males(people_list):
    male_list = list(filter(lambda person: person['sex'] == 'male', people_list))
    return male_list
ex2()