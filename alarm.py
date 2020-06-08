import winsound, time, os, platform

def sound():
    
    for i in range(2): 
        
        for j in range(10):  
            
            winsound.MessageBeep()


def alarm(n):
    
    print('\nAlarm goes off in:', n ,'Seconds')
    time.sleep(n)  # Waits for n seconds before ringing
    print('Alarm Went off')
    
    sound()

def input_type(alarm_type):
    
        if alarm_type == 1:

            alarm_type = int(input('Enter Hours: '))
            alarm_time = ((alarm_type * 60) * 60)  # Convert hours to seconds
            alarm(alarm_time)

        elif alarm_type == 2:

            alarm_type = int(input('Enter Minutes: '))
            alarm_time = (alarm_type * 60)  # Convert minutes to seconds
            alarm(alarm_time)

        elif alarm_type == 3:

            alarm_type = int(input('Enter Seconds: '))
            alarm_time = (alarm_type)  # No conversion needed
            alarm(alarm_time)

        elif alarm_type == 4:

            hours = int(input('Enter Hours: '))
            minutes = int(input('Enter Minutes: '))
            seconds = int(input('Enter Seconds: '))

            alarm_time = (((hours * 60) * 60) + (minutes * 60) + seconds)  # combination of Hours, minutes & seconds
            alarm(alarm_time)
            
        else:
            
            
            try:
                os.system('cls')   # for windows
                user()
                
            except:
                
                os.system('clear')  # for linus/mac
                user()
        
def user():
    
    user_input = int(input('What type of Alarm would you like to use?\n1.Hours\n2.Minutes\n3.Seconds\n4.Combination\n: '))
    
    input_type(user_input)
    
user()