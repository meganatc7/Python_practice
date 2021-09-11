def solution(id_list, report, k):
    report_count = {}
    report_member = {}
    email_count = {}

    for id in id_list:
        report_count[id] = 0
        report_member[id] = []
        email_count[id] = 0

    # 신고한 멤버와 횟수 세기
    for re in report:
        reporter, reported = re.split()
        if reporter not in report_member[reported]:
            report_member[reported].append(reporter)
            report_count[reported] += 1

    # 신고 횟수에 따라 이메일 보내기
    for key, value in report_count.items():
        if value >= k:
            for reporter in report_member[key]:
                email_count[reporter] += 1

    answer = []
    # 이메일 받은 횟수 answer에 담기
    for id in id_list:
        answer.append(email_count[id])

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))