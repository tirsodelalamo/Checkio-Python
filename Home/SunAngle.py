
def sun_angle(time):
    #replace this for solution
    hour = int(time[:-3]) + int(time[-2:])/60
    if hour < 6 or hour > 18:
        return "I don't see the sun!"        
    else:
        return (hour-6)/12*180


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
