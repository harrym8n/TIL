import random

def generate_numbers(n):
    random_num_list = []

    while len(random_num_list) < n:
        rand_num = random.randint(1,45)
        if rand_num not in random_num_list:
            random_num_list.append(rand_num)
    
    return random_num_list

numbers = generate_numbers(6)


def draw_winning_numbers():
    winning_num_list = generate_numbers(n=7)
    return sorted(winning_num_list[:6]) + [winning_num_list[6]]
    
winning_num_list = draw_winning_numbers()


def count_matching_numbers(numbers, winning_num_list):
    # return len(set(numbers) & set(winning_num_list))
    return len(set(numbers).intersection(set(winning_num_list)))


def check(numbers, winning_num_list):
    
    general_correct_num = count_matching_numbers(numbers, winning_num_list[:6])
    bonus_correct_num = count_matching_numbers(numbers, winning_num_list[6:])

    if general_correct_num == 6:
        return 10**9
    elif general_correct_num == 5 and bonus_correct_num == 1:
        return (10**7)*5
    elif general_correct_num == 5:
        return (10**6) 
    elif general_correct_num == 4:
        return (10**4) * 5
    elif general_correct_num == 4:
        return (10**3) * 5
    else :
        return 0