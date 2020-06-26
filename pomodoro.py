def pomodoro():

    # Imports
    import datetime
    from datetime import timedelta
    import time
    import winsound

    # Pomodoro technique default durations
    # https://en.wikipedia.org/wiki/Pomodoro_Technique
    pom_dur = {
        'pom': 25,
        'sb': 5,
        'lb': 15
    }

    # Get input
    print('Enter cycle type:\n' + \
        'pom    | 25 mins | the work cycle\n' + \
        'sb     | 05 mins | the short break\n' + \
        'lb     | 15 mins | the long break\n' + \
        'custom | ?? mins | custom duration')

    pom_input = str(input()).lower()
    if (pom_input == 'custom'):
        print('Enter your custom cycle duration in mins:')
        duration = float(input())
    else:
        duration = pom_dur[pom_input]

    # Get start & end times
    start_time = datetime.datetime.now()
    end_time = start_time + timedelta(minutes = duration)

    # Check if cycle is over
    while datetime.datetime.now() < end_time:
        # Wait 10 secs
        time.sleep(10)

    # Beep beep beep - time's up!
    beep_length = 150                           # millisecs
    freqs = [300, 350, 400, 450, 500, 550, 600] # Hz
    print('Time\'s up!')
    for freq in freqs:
        winsound.Beep(freq, beep_length)
    
    # Begin next iteration?
    print('Enter next cycle? Y or N')
    again = str(input()).lower()
    if (again == 'y'):
        pomodoro()
    else:
        exit

pomodoro()
