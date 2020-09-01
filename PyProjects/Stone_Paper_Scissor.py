import random
loop=1
i=0
k=0
j=0
print("Game Start")
print("Enter Your Name")
name=input()
print("You Have 10 Rounds")
while(loop<=10):
    print(f"Round {loop}")
    print("Stone Paper Scissor")
    print("press s: Stone, p: Paper, sc: Scissor")
    inp=input()
    List=["s","p","sc"]
    choose = random.choice(List)
    print(choose)
    if  (inp == "s" and choose == "sc") or(inp == "p"and choose == "s")or(inp == "sc" and choose == "p"):
        print("Won\n")
        i = i + 1

    elif (inp == "s" and choose == "p") or (inp=="p" and choose =="sc") or (inp== "sc" and choose =="s"):
        print("Lost\n")
        k = k + 1
    elif (inp == "s" and choose == "s") or (inp == "p" and choose =="p") or (inp == "sc" and choose =="sc"):
        print("Tie\n")
        j = j + 1
    loop=loop+1

print("Game Over\n")
print(f"Number of Game {name} Won = {i}",)
print(f"Number of Game Computer Won = {k}")
print(f"Number of Game Tied = {j}")





