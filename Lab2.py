
import statistics

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    user_text = input()
    split_text = user_text.split(", ")
    user_list_string = split_text
    user_list_num = [float(num) for num in user_list_string]

    print(user_list_num)

    return user_list_num


def calc_average(input_list):
    average = sum(input_list) / len(input_list)

    print("Average = " + str(average))

    return average


def find_min_max(input_list):
    value_min = min(input_list)
    value_max = max(input_list)

    min_max_list = [value_min, value_max]

    print("Min, Max = " + str(min_max_list))

    return min_max_list


def sort_temperature(input_temperature_list):
    sorted_list = sorted(input_temperature_list)

    print("Temperatures in ascending = " + str(sorted_list))

    return sorted_list


def calc_median_temperature(input_temperature_list):

    median_value = statistics.median(input_temperature_list)

    print("Median Temp = " + str(median_value))

    return median_value


def calc_average_temperature(input_temperature_list):
    average = sum(input_temperature_list) / len(input_temperature_list)

    print("Average Temp = " + str(average))

    return float(average)


def calc_min_max_temperature(input_temperature_list):
    temp_min = min(input_temperature_list)
    temp_max = max(input_temperature_list)
    min_max = [temp_min, temp_max]

    print("Min, Max Temp = " + str(min_max))

    return min_max

def main():
    display_main_menu()
    user_input1 = get_user_input()
    calc_average(user_input1)
    find_min_max(user_input1)

    display_main_menu()
    user_input2 = get_user_input()

    sort_temperature(user_input2)
    calc_median_temperature(user_input2)
    calc_average_temperature(user_input2)
    calc_min_max_temperature(user_input2)


if __name__ == "__main__":
    main()
