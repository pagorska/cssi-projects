from random import randint

def randL(r):
     return r[randint(0,len(r)-1)]

def pS(number):
    print number * ' boop '
#pS(16)

def add(num1, num2):
    print num1+num2

#add(3,4)

groceries = ['banana','pineapple', 'milk', 'milk', 'chips']

for index in range(len(groceries)):
    print '%s. %s' %(index + 1, groceries[index])


#print groceries[randint(0, 4)]

tasks = ['do chores', 'walk the dog', 'visit grandma', 'check the mail', 'do my homework', 'pay the bills', 'find a babysitter', 'go to class', 'tutor my friend', 'apply for a job']
excuses = ['I had better things to do', 'I went to see Hamilton', 'I wanted to see my friends', 'there was a tornado', 'my car broke down']

#randL("hello")
#randL(tasks)
#randL(excuses)
print 'I didn\'t %s because %s.'%(randL(tasks), randL(excuses))

#print 'I didn\'t %s because %s.'%(tasks[randint(0,len(tasks)-1)], excuses[randint(0,len(excuses)-1)])
# name = raw_input('Enter your name: ')
# print "Hello " + name
#
# verb = raw_input('Enter a past tense verb: ')
# noun = raw_input('Enter a noun: ')
#
# print "Mad Libs! My " + noun + " " + verb + " at my party!"
#
# print "My %s %s at my party!"%(noun, verb)
