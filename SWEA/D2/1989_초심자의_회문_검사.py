T = int(input())

for t in range(1,T+1):
    word = input()
    reverse = ''
    for letter in range(-1,-len(word)-1,-1):
        reverse += word[letter]
    if reverse == word:
        print(f'#{t} 1')
    else:    
        print(f'#{t} 0')