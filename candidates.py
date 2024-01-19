#here in a list, I specify the required skills from prospective employees.
required_skills = ['python', 'github', 'linux']

#here I use nested dictionaries. We have the first dictionary which holds the selection of candidates who have applied for the role.
#with each candidate there is a nested dictionary listing what skills they have.
candidates = {
    'anna': {'java', 'linux', 'windows', 'github', 'python', 'full stack'},
    'bob': {'github', 'linux', 'python'},
    'carol': {'linux', 'javascript', 'html', 'python', 'github'},
    'daniel': {'pascal', 'java', 'c++', 'github'},
    'joan': {'html', 'css', 'github', 'python', 'linux'},
    'nicole': {'linux', 'pascal', 'java', 'c', 'lisp', 'modula-2', 'perl', 'github'},
}

# set() function creates a set object. Items are unordered, so they will return in random order.
interviewees = set()

#using a for loop it will take the candidates, the skills within the candidates nested dictionary and
#it will then see which candidates possess all the required skills in 'required_skills'.
for candidate, skills in candidates.items():
    #if skills.issuperset(required_skills):
    if skills > set(required_skills):
        interviewees.add(candidate)

#the candidates who do not have all 3 of the skills listed in 'required_skills' will be ignored and the ones who do have
#the 'required_skills' will be added to 'interviewees'. this then gets put into a dictionary and returned to the user.
print(interviewees)