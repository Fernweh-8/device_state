from datetime import datetime


def data_to_dict(file: str) -> dict:
    # keys = ["time", "state"]
    state_dict = {}
    with open(file, 'r') as f:
        for line in f.readlines():
            new_list = line.split(" ")
            new_list[0] = new_list[0] + ", " + new_list[1] + ", " + new_list[2]
            # print(new_list)
            for index, element in enumerate(new_list):
                # print(index, element)
                if index == 0:
                    state_dict.setdefault("time", []).append(element)
                if index == 7:
                    element = element.strip('\n')
                    state_dict.setdefault("state", []).append(element)
    # print(state_dict)
    date = state_dict['time']
    state = state_dict["state"]
    state_dict = dict(zip(date, state))
    # print(state_dict)
    return state_dict


date_time_format = "%b, %d, %H:%M:%S.%f"


def parse_and_calculate(starting_time, ending_time):
    starting_time = datetime.strptime(starting_time, date_time_format)
    ending_time = datetime.strptime(ending_time, date_time_format)
    current_time_difference = ending_time - starting_time
    return current_time_difference.total_seconds()

def time_difference(dictionary: dict):
    max_starting_time = None
    max_ending_time = None
    temp_time = []
    max_time_difference_in_seconds = 0.0

    for idx, (key, value) in enumerate(dictionary.items()):
        print(f"Current {idx} | {key} | {value}")
        if value == "ON":
            temp_time.append(key)
        elif value != "ON" and len(temp_time) == 0:
            continue
        else:
            # print(len(temp_time))
            starting_time = temp_time[0]
            ending_time = temp_time[-1]
            current_period_total_seconds = parse_and_calculate(starting_time, ending_time)
            if current_period_total_seconds > max_time_difference_in_seconds:
                max_starting_time = starting_time
                max_ending_time = ending_time
                max_time_difference_in_seconds = current_period_total_seconds
            temp_time = []

    print(max_time_difference_in_seconds)
    print(max_starting_time)
    print(max_ending_time)


def main():
   state_dict = data_to_dict("entries.log")
   # print(state_dict)
   time_difference(state_dict)


if __name__ == "__main__":
    main()
