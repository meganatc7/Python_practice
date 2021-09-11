import math

def solution(fees, records):
    accumulate_time = {}
    in_out_info = {}
    car_info = []

    for record in records:
        time, car_number, state = record.split()
        car_info.append(car_number)
        if state == 'IN':
            in_out_info[car_number] = time
            if not accumulate_time.get(car_number):
                accumulate_time[car_number] = 0
        if state == 'OUT':
            in_hour, in_minute = map(int,in_out_info[car_number].split(':'))
            out_hour, out_minute = map(int, time.split(':'))
            in_time = (int(in_hour) * 60) + int(in_minute)
            out_time = (int(out_hour) * 60) + int(out_minute)

            parking_time = out_time - in_time
            accumulate_time[car_number] += parking_time
            in_out_info[car_number] = ''

    for car_number, time in in_out_info.items():
        end_time = 24 * 60 - 1
        if time:
            in_hour, in_minute = map(int, time.split(':'))
            in_time = (int(in_hour) * 60) + int(in_minute)
            parking_time = end_time - in_time
            accumulate_time[car_number] += parking_time
    print(in_out_info)
    print(accumulate_time)

    base_time, base_fee, per_time, per_fee = fees
    answer = []
    for car_number in sorted(list(set(car_info))):
        total_parking_time = accumulate_time[car_number]
        if total_parking_time <= base_time:
            total_fee = base_fee
        else:
            total_fee = base_fee + (math.ceil(((total_parking_time - base_time) / per_time)) * per_fee)

        answer.append(total_fee)


    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))