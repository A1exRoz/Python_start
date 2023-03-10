N = int(input('Сколько монет лежит на столе?: '))
coin_eagle = 0
coin_tails = 0
if N == 1:
    print('Нет смысла считать')
else:
    for i in range(N):
        coin = int(input('Какая следующая монета? Орел - 1, Решка - 0: '))
        if coin == 1:
            coin_eagle += 1
        else:
            coin_tails += 1
    if coin_eagle > coin_tails:
        print(f'Решек - {coin_tails} шт')
    elif coin_tails > coin_eagle:
        print(f'Орлов - {coin_eagle} шт')
    else:
        print('Без разницы, одинаковое кол-во монет')
