
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    all_platzi_members = [member['name'] for member in DATA if member['organization'] == 'Platzi']
    adults = list(filter( lambda worker: worker['age'] > 18, DATA))
    adults = list(map( lambda worker: worker['name'], adults ))
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    all_python_devs_ho = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs_ho2 = list(map(lambda worker: worker['name'], all_python_devs_ho))

    adultslcp = [worker['name'] for worker in DATA if worker['age'] > 18]
    old_peoplelcp2 = {'old' : worker['age'] for worker in DATA if worker['age'] > 70 }
    old_peoplelcp = [worker | {'old' : worker['age'] > 70} for worker in DATA ]
    
    for worker in all_python_devs:
        print(worker, '\n')

    for member in all_platzi_members:
         print(member, '\n')
    
    for worker in adults:
         print(worker, '\n')

    for worker in old_people:
         print(worker, '\n')    

    for worker in all_python_devs_ho:
        print(worker, '\n' )
        print(all_python_devs_ho2)

    for worker in adultslcp:
         print(worker, '\n')

    for worker in old_peoplelcp2:
        print(worker, '\n')

    for worker in old_peoplelcp:
        print(worker, '\n')



if __name__ == '__main__':
    run()