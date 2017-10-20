# race_history_individual.py
import requests
import csv
# import pandas as pd
# import matplotlib.pyplot as plt


# get relevant data and write to file
def get_athlete_races(fname, lname):
    url = 'https://ultrasignup.com/service/events.svc/history/%s/%s' % (fname,
                                                                        lname)
    file_name = fname + '_' + lname + '.csv'
    results = requests.get(url)
    athlete_json = results.json()
    with open(file_name, 'w') as target:
        writer = csv.writer(target, delimiter=",")
        writer.writerow(["Event", "Event Date", "Finish Time", "Place", "Rank"])
        for i in athlete_json:
            for results in i['Results']:
                eventname = results.get('eventname')
                eventdate = results.get('eventdate')
                place = results.get('place')
                rank = results.get('runner_rank')
                time = results.get('time')
                row = eventname, eventdate, time, place, rank
                writer.writerow(row)


def main():
    # ask for name
    fname = input('Enter athlete first name:')
    lname = input('Enter athlete last name:')
    get_athlete_races(fname, lname)


if __name__ == '__main__':
    main()
