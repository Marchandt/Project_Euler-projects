FTerm = 1
STerm = 2
TTerm = int()


while TTerm <= 4000000:
    if TTerm%2==0:
      print(TTerm)

    FTerm = STerm
    STerm = TTerm
    TTerm = FTerm + STerm