import collections

def solution(participant, completion):
    participant= collections.deque(sorted(participant))
    completion = collections.deque(sorted((completion)))
    answer = ''

    while completion:
        if participant[0] == completion[0]:
            participant.popleft()
            completion.popleft()
        elif participant[0] != completion[0]:
            answer = participant[0]
            break
    if not answer:
        answer = participant[0]

    return answer





###
def solution(participant, completion):

    marathon = {}
    answer = ''
    for p in participant:
        marathon[p] = marathon.get(p,0) + 1

    for c in completion:
        marathon[c] -= 1
        if marathon[c] == 0:
            marathon.pop(c)
    answer = list(marathon.keys())[0]
    return answer