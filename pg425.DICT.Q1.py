#Program that asks continously for team name and score
d={}
f={}
g={}
while True:
    a=raw_input("Enter the name of the team : ")
    b=raw_input("Enter matches won : ")
    c=raw_input ("Enter matches lost : ")
    d[a]=[b, c]
    f[a]=[b]
    g[a]=[c]
    e=raw_input("Do you want to add more teams? [Y/N] ")
    if e=='Y' or e=='y':
        continue
    else:
        break
print "The dictionary created is : "
print d
print "All the teams are : ", d.keys() 
print "The Matches won by teams are : "
print f
print "All the matches lost by teams are : "
print g
