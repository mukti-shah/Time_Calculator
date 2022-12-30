import math

def add_time(start, duration, week=''):

    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    
    
    if (len(start.split())==3):
        time, clock, week= start.split()
        
    else:
        time, clock= start.split()
         
    week = week.lower()
    print(week)
       
    start_hr, start_min = time.split(":")
    stop_hr, stop_min = duration.split(":")
    

    new_hr = 0
    after=''
    
    new_min = int(start_min) + int(stop_min)
    if(new_min>59):
        new_min-=60
        new_hr += 1
    
    new_hr += (int(start_hr) + int(stop_hr))

    if (new_hr>=12):
        # if(new_hr>12):
            half_day = new_hr//12
            # print(half_day)
            
            new_hr-=12*half_day
        
            if new_hr==0:
                new_hr=12
            
            flag = 1
            if half_day %2 == 1:    
                if clock=='AM':
                    clock='PM'
                    
                else:
                    clock='AM'
                    flag = 2
                    days_later = math.ceil(half_day/2)
                    if days_later==1:
                        after='next day'
                    else:
                        after = str(days_later) + ' days later'

                    if week != '':   
                        week_index = week_days.index(week)
                        week_index+=(days_later)
                        if week_index>=7:
                            week_index = (week_index % 7)
                        week = week_days[week_index].title()
            
            if half_day != 1 and clock!='PM' and flag!= 2:
                days_later = math.ceil(half_day/2)
                if days_later==1:
                    after='next day'
                else:
                    after = str(days_later) + ' days later'
                
                if week != '':  
                    print(week) 
                    week_index = week_days.index(week)
                    week_index+=(days_later)
                    if week_index>=7:
                        week_index = (week_index % 7)
                    week = week_days[week_index].title()

    week=week.title()
    
    if not week and not after:
        new_time = f'{new_hr}:{new_min:02} {clock}'
        
    elif not after:
        new_time = f'{new_hr}:{new_min:02} {clock}, {week}'
        
    elif not week:
        new_time = f'{new_hr}:{new_min:02} {clock} ({after})'
        
    else:
        new_time = f'{new_hr}:{new_min:02} {clock}, {week} ({after})'
    

    return new_time