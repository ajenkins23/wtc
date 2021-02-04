

def create_outline():

    #NOTE: Step 1: set()
    print('Course Topics:')
    topics = sorted(set(['* Introduction to Python', '* Tools of the Trade','* How to make decisions',
        '* How to repeat code', '* How to structure data', '* Functions', '* Modules']))
    for each in topics:
        print(each)
   
    #NOTE: Step 2: maps - dict() 
    print('Problems:')
    problem = 'Problem 1, Problem 2, Problem 3'
    problems = {topics[0]:problem, topics[1]:problem, topics[2]:problem,
        topics[3]:problem, topics[4]:problem, topics[5]:problem, topics[6]:problem}
    for key, value in problems.items():
        print(key + ' : ' + value)

    #NOTE: Step 3: tuple
    print('Student Progress:')
    students = (['1.Abrulla',' - ' + topics[1] + ' - ', '[STARTED]'],
                ['2.Sammy',' - ' + topics[2] + ' - ', '[GRADED]'],
                ['3.Rick',' - ' + topics[3] + ' - ', '[COMPLETED]'])
    for x in range(len(students)):
        for y in range(len(students[x])):
            print(students[x][y], end='')
        print('')

    pass


if __name__ == "__main__":
    create_outline()
