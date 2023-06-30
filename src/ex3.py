def ex3():
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]
    new_people_list = calc_bmi(people_list)
    print(new_people_list)

def calc_bmi(people_list):
    bmi_list = list(map(lambda p: {'id': p['id'], 'name': p['name'], 'weight_kg': p['weight_kg'], 'height_meters': p['height_meters'], 'bmi': round(p['weight_kg'] / p['height_meters'] ** 2, 1)}, people_list))
    return bmi_list

ex3()