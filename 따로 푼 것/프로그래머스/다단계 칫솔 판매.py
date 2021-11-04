def solution(enroll, referral, seller, amount):
    organization = {enroll[i]: referral[i] for i in range(len(enroll))}
    answer = {enroll[_]: 0 for _ in range(len(enroll))}

    for j in range(len(seller)):
        money = amount[j]*100
        member = seller[j]

        while True:
            if organization[member] == "-" or money == 0:
                answer[member] += money - money//10
                break
            answer[member] += money - money//10
            money //= 10
            member = organization[member]

    return list(answer.values())
