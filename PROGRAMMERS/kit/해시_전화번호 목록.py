def solution(phone_book):
    answer = True

    pb = {}
    phone_book.sort(key=len)
    # phone_book.sort(key=lambda x: len(x))
    for phone in phone_book:
        for i in range(len(phone)+1):
            if pb.get(phone[:i]) == 1:
                answer = False
                return answer
        pb[phone] = 1


    return answer

print(solution(["119", "97674223", "1195524421"]))