def toi(height, fromPole, midPole, toPole):
    if (height == 1):
        print("Move disk 1 from",fromPole,"to", toPole)
        return 1
    else:
        toi(height-1,fromPole, toPole, midPole)
        print("Move disk",height,"from",fromPole,"to", toPole)
        toi(height-1, midPole, fromPole, toPole)
        return 1
 
height = int(input("Enter the height = "))
toi(height,'A','B','C')
