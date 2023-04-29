"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-02-14"
-------------------------------------------------------
"""
# Imports
# Constants

def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
         name - description (type)
    ------------------------------------------------------
    """
#catch first three inputs
turns = int(input("1st line: "))
students=int(input("2nd line: "))
profs=int(input("3rd line: "))

#create variables for prev. iteration
last_student=0
last_prof=0
last_student_time=0
last_prof_time=0
#scores
student_points=0
prof_points=0

#loop thru turns, program will stop after every turn has gone
for i in range(turns):
    #give user ability to end game before turns run out
    turn=input("4th line (type 'end' to finish game) : ")
    if not turn == "end":
        #catch time, which team went, final variable doesnt matter, still had to catch it tho
        time, roaster, roasted=turn.split()
        current_time=int(time)
        current_roasting=roaster[0]
        current_num=int(roaster[1])
        #award pts for students
        if current_roasting=="s":
            student_points+=500
            #award addtional 500 if criteria is met
            if last_student==current_num and (current_time-last_student_time)<=10:
                student_points+=500
            #keep track of prev. itteration
            last_student=current_num
            last_student_time=current_time
        else:
            #same as top for profs
            prof_points+=500
            if last_prof==current_num and (current_time-last_prof_time) <=10:
                prof_points+=500
                last_prof=current_num
                last_prof_time=current_time
#print results once loop has finished
print(f"{student_points} {prof_points}")
    



