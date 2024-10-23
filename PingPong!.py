

def pingPong(PingArray, win):
    finalGame = []
    for i in range(len(PingArray) - 1):
        finalGame.append(PingArray[i])
        finalGame.append("Pong!")
    finalGame.append("Ping!")
    if win == True:
        finalGame.append("Pong!")
    print(finalGame)
        




#Example 1
pingPong(["Ping!"], True)
#output = ["Ping!", "Pong!"]

#Example 2
pingPong(["Ping!", "Ping!"], False)
#output = ["Ping!", "Pong!", "Ping!"]

#Example 3
pingPong(["Ping!", "Ping!", "Ping!"], True)
#output = ["Ping!", "Pong!", "Ping!", "Pong!", "Ping!", "Pong!"]