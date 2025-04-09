def main():
    string = '1h 45m,360s,25m,30m 120s,2h 60s'
    min = 0
    string = string.split(',')
    for time in string:
        time = time.split()
        for instance in time:
            if 'h' in instance:
                h = instance.replace('h','')
                min += int(h) * 60
            elif 'm' in instance:
                m = instance.replace('m','')
                min += int(m)
            elif 's' in instance:
                s = instance.replace('s','')
                min += int(s) / 60

    calc_sum(round(min, 2))


def calc_sum(min):
    print(f'The summ of minutes is {min}')


if __name__ == "__main__":
    main()
