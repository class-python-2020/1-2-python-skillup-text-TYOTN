def genPrime(maxnum):
  num = 2
  while(num <= maxnum):
      is_prime = True #素数かどうか判定する変数
      for i in range(2, num):
          if(num % i) == 0 : #あまりがないということは割れる＝素数ではない
            is_prime = False
            break
      if is_prime : yield num
      num += 1

it = genPrime(50)
for i in it:
  print(i, end = ' ')