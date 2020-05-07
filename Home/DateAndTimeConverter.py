
def date_time(time: str) -> str:
    #replace this for solution
    tagHour=''
    tagMinute=''
    
    day = time[0:2]
    month = time[3:5]
    year = time[6:10]
    hour = time[11:13]
    minute = time[14:16]
    translationMonths={'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
    month = translationMonths[month]
    
    if day[0]=='0':
        day = day[1]
        
    if hour[0]=='0':
        hour = hour[1]
        
    if minute[0]=='0':
        minute = minute[1]
        
    if minute=='1':
        tagMinute='minute'
    else:
        tagMinute='minutes'
        
    if hour=='1':
        tagHour='hour'
    else:
        tagHour='hours'   

    
    return (day + ' ' + month + ' ' + year + ' year ' + hour + ' ' + tagHour +' ' + minute + ' ' +tagMinute)
    


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
