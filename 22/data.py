
f = open("sample.txt", "r")
# f = open("sample2.txt", "r")
f = open("data.txt", "r")
data = []

player1 = []
player2 = []

for d in f :
    dstr = d.rstrip()
    data.append(dstr)
    if "Player 1" in dstr:
        player = player1
    elif "Player 2" in dstr:
        player = player2
    elif len(dstr) > 0 :
        player.append(int(dstr))

print(player1)
print(player2)

# cnt =0
# while len(player1) > 0 and len(player2) > 0 :
#     n1=player1[0]
#     n2=player2[0]
#     player1.remove(n1)
#     player2.remove(n2)
#     if n1 > n2 :
#         player1.append(n1)
#         player1.append(n2)
#     if n2 > n1 :
#         player2.append(n2)
#         player2.append(n1)
#     print(cnt,player1)
#     print(cnt, player2)
#     cnt += 1
gameId = 0

def combat(p1, p2) :
    global gameId
    id = gameId+1
    gameId = gameId+1
    print(f'=== Game {id} ===')
    rnd = 0
    win = None
    p1round = []
    p2round = []
    gameover = False
    while len(p1) > 0 and len(p2) > 0 and not gameover:
        rnd += 1
        print(f'-- Round {rnd} (Game {id}) --')
        print(f'Player 1 deck: {p1}')
        print(f'Player 2 deck: {p2}')
        p1check = p1 in p1round
        p2check = p2 in p1round
        if p1check or p2check :
            print(p1round)
            print(p2round)
            win=1
            gameover = True
        else:
            p1round.append(p1.copy())
            p2round.append(p2.copy())
            n1=p1[0]
            n2=p2[0]
            print(f'Player 1 plays: {n1}')
            print(f'Player 2 plays: {n2}')
            p1.remove(n1)
            p2.remove(n2)
            if n1 <= len(p1) and n2 <= len(p2) :
                print(f'Start a sub game')
                win=combat(p1[:n1], p2[:n2])
            else :
                if n1 > n2 :
                    win = 1
                if n2 > n1 :
                    win = 2
            if win == 1 :
                p1.append(n1)
                p1.append(n2)
            if win == 2 :
                p2.append(n2)
                p2.append(n1)

        print(f'Player {win} wins round {rnd} of game {id}')
    return win

combat(player1,player2)
player = player1 if len(player1) > 0 else player2
score = 0
for i in range(1, len(player)+1) :
    score += player[len(player)-i] * i
print(score)