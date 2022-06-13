def count_increases():
    # Correct answer: 1446

    previous_depth = 0
    current_depth = 0
    increase_count = 0

    with open('data/sonar_meassurements.txt', 'r') as sweep:
        previous_depth = sweep.readline()
        current_depth = sweep.readline()
        eof = current_depth == ''
        while not eof:
            increase = int(current_depth) > previous_depth
            if increase:
                increase_count += 1
            
            previous_depth = int(current_depth)
            current_depth = sweep.readline()
            eof = current_depth == ''
    
    return increase_count


def count_increases_group():
    # Correct answer: 1486

    previous_group_sum = 0 
    current_group_sum = 0
    increase_count = 0

    with open('data/sonar_meassurements.txt', 'r') as sweep:
        current_group = [int(sweep.readline()), int(sweep.readline()), int(sweep.readline())]
        previous_group_sum = current_group[0] + current_group[1] + current_group[2]
        latest_pointer = sweep.readline()
        eof = latest_pointer == ''
        while not eof:
            current_group[0] = current_group[1]
            current_group[1] = current_group[2]
            current_group[2] = int(latest_pointer)
            current_group_sum = current_group[0] + current_group[1] + current_group[2]
            increase = current_group_sum > previous_group_sum
            if increase:
                increase_count += 1

            previous_group_sum = current_group_sum
            latest_pointer = sweep.readline()
            eof = latest_pointer == ''
        
    return increase_count
 

def main():
    result = count_increases_group()
    print(result)

if __name__ == '__main__':
    main()

