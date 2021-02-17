#!/usr/local/bin/python3

import webbrowser, time, datetime, sys, os, schedule
from classes import urls


def play_alarm(duration, freq):
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))


def say(message):
    os.system('say "{}"'.format(message))


cycle_day = 0
open_zoom_room = True
warnings = [9.5, 3, 1]  # minutes before to give warning


class_names = ["Advisor Group", "Driver's Ed", "Physics", "English", "Math", "French", "Chemistry", "History"]

rotation_schedule = [
    [0, -1,  2, 3, -1,  4, -1,  5],
    [0,  6,  7, 1,  4, -1,  2, -1],
    [0,  5,  3, 6, -1, -1, -1,  7],
    [0,  2, -1, 5,  4, -1, -1,  3],
    [0,  7,  6, 2,  4, -1, -1,  1],
    [0,  3,  5, 7, -1, -1,  6, -1]
]

path = "open -a /Applications/Google\ Chrome.app %s"

start_times = [
    datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day, 8, 20),
    datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day, 8, 50),
    datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day, 9, 50),
    datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day, 10, 50),
    datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day, 11, 50),
    datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day, 12, 10),
    datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day, 13, 5),
    datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day, 13, 30)
]


def job(message, url=None):
    if url:
        webbrowser.get(path).open(url)
    print(message + " : " + str(datetime.datetime.now()))
    play_alarm(1, 440)
    say(message)


def reset_day():
    global cycle_day
    schedule.clear("daily-tasks")
    if datetime.datetime.today().weekday() < 5:  # weekday
        cycle_day = cycle_day % 6 + 1
        print("Cycle day reset to {}".format(cycle_day))
        set_daily_tasks()


def set_daily_tasks():
    for i in range(len(start_times)):
        cur_class = rotation_schedule[cycle_day][i]
        if cur_class != -1:
            for j in warnings:
                if j == 1:
                    message = class_names[cur_class] + " in {} minute".format(j)
                else:
                    message = class_names[cur_class] + " in {} minutes".format(j)
                schedule.every().day.at((start_times[i] - datetime.timedelta(minutes=j)).strftime("%H:%M")).do(job,
                    message=message).tag("daily-tasks")

            if open_zoom_room:
                message = "Opening " + class_names[cur_class]
                schedule.every().day.at(start_times[i].strftime("%H:%M")).do(job, message=message,
                    url=urls[cur_class]).tag("daily-tasks")


def main():
    print("started")
    global cycle_day, open_zoom_room
    try:
        cycle_day = int(sys.argv[1]) - 1
        if cycle_day < 0 or cycle_day >= 6:
            raise ValueError(str(cycle_day + 1) + " is an invalid cycle day\n" + "Cycle day must be between 1 and 6")
            exit()
    except Exception as e:
        print(e)
        exit()
    try:
        if sys.argv[2] == "0":
            open_zoom_room = False
    except:
        pass
    set_daily_tasks()
    schedule.every().day.at("00:01").do(reset_day)
    while True:
        schedule.run_pending()
        time.sleep(1)
        print(str(datetime.datetime.now()), flush=True)


if __name__ == "__main__":
    main()
