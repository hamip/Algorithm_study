def solution(a: int, b: int) -> str:
    # Friday comes first because the starting day Jan 1 is Friday
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    num_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if a == 1:
        total_days = b
    else:
        total_days = sum(num_days[:a-1]) + b
        
    return days[total_days % 7 - 1]
