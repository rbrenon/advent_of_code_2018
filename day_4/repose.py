from pprint import pprint


def main():
    with open("input.txt") as file:
        raw_input = file.readlines()

    input_data = parse_data(raw_input)
    part_one(input_data)
    return


def parse_data(data: list[str]) -> list[tuple]:
    parsed_data = []

    for index, line in enumerate(data):
        date = data[index][1:11]
        time = data[index][12:17]
        action = data[index][19:]
        parsed_data.append((date, time, action))

    parsed_data.sort()
    return parsed_data


def part_one(data):
    repose = {}
    guard_no = 0

    for record in data:
        """
        record examples
        ('1518-02-03', '23:50', 'Guard #661 begins shift\n')
        ('1518-02-04', '00:01', 'falls asleep\n')
        ('1518-02-04', '00:57', 'wakes up\n')
        """

        action = record[2].split()
        """
        action examples
        ['Guard', '#661', 'begins', 'shift']
        ['falls', 'asleep']
        ['wakes', 'up']
        """

        if action[0] == "Guard":
            guard_no: int = int(action[1][1:])
            if guard_no in repose.keys():
                pass
            else:
                repose[guard_no] = {
                    "asleep": [],
                    "awake": [],
                    "sleep": 0,
                }
        elif action[0] == "falls":
            repose[guard_no]["asleep"].append(record[1:2])
        elif action[0] == "wakes":
            repose[guard_no]["awake"].append(record[1:2])

    # calculate time asleep
    for guard in repose:
        try:
            for index, wake_time in enumerate(repose[guard]["awake"]):
                waking = wake_time[0].split(":")[1]
                sleeping = repose[guard]["asleep"][index][0].split(":")[1]
                sleep_time = int(waking) - int(sleeping)
                try:
                    previous_sleep_time = repose[guard]["sleep"]
                    repose[guard]["sleep"] = previous_sleep_time + sleep_time
                except KeyError as ke:
                    repose[guard]["sleep"] = sleep_time
        except Exception as e:
            print(e)

    # find guard that slept the most
    most_time_asleep = 0
    sleepiest_guard = 0
    for guard_on_duty in repose.keys():
        if repose[guard_on_duty]["sleep"] > most_time_asleep:
            most_time_asleep = repose[guard_on_duty]["sleep"]
            sleepiest_guard = guard_on_duty

    pprint(f"Guard: {sleepiest_guard} slept for {most_time_asleep} minutes")
    # pprint(f"{repose[sleepiest_guard]}")

    # sorts all
    # guard_by_total_sleep = [(guard, repose[guard]['sleep']) for guard in repose]  # (guard, sleep) tuples
    # guard_by_total_sleep.sort(key=lambda guard_sleep_tuple: guard_sleep_tuple[1], reverse=True) # (guard, sleep) tuples sorted descending by sleep
    # pprint(repose[guard_by_total_sleep[0][0]])  # guard with highest sleep time

    # create dict key "min_asleep" and populate with {min=0: count=0, 1:0 ... 59:0}
    # go through asleep:awake pairs and increment keys
    # find largest min key
    # {'asleep': [('00:38',), ('00:14',), ('00:08',)]
    #  'awake': [('00:52',),  ('00:49',), ('00:56',)]}
    repose[sleepiest_guard]["min_asleep"] = {x: 0 for x in range(60)}
    for index, wake_time in enumerate(repose[sleepiest_guard]["awake"]):
        wake_min = int(wake_time[0].split(":")[1])
        sleep_min = int(repose[sleepiest_guard]["asleep"][index][0].split(":")[1])
        for minute in range(sleep_min, wake_min):
            repose[sleepiest_guard]["min_asleep"][minute] += 1
    # pprint(repose[sleepiest_guard])

    # find the minute where the guard sleeps the most
    min_asleep_most = max(
        repose[sleepiest_guard]["min_asleep"],
        key=repose[sleepiest_guard]["min_asleep"].get,
    )
    pprint(f"min asleep most: {min_asleep_most}")

    pprint(
        f"Part One solution is: {sleepiest_guard} * {min_asleep_most} = {sleepiest_guard * min_asleep_most}"
    )
    # correct: 35184  high: 35917; low: 34451


if __name__ == "__main__":
    main()
