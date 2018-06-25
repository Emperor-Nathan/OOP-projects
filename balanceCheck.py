def isBalanced(input_string):
    circle=0
    square=0
    curly=0
    for a in input_string:
        if a=='(':
            circle+=1
        elif a=='[':
            square+=1
        elif a=='{':
            curly+=1
        elif a==')':
            circle-=1
        elif a==']':
            square-=1
        elif a=='}':
            curly-=1
    return circle==0 and square==0 and curly==0
while True:
    print(isBalanced(input('Enter the sequence: ')))
