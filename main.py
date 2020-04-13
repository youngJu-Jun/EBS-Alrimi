import telepot
import time
import datetime

first = '8:35'
second = '9:35'
third = '10:35'
fourth = '11:35'
fifth = '13:35'
sixth = '14:35'
seventh = '15:35'

# setting bot
telgm_token = '817556304:AAFvXm9FZLGh2QQZ_b22sdIAjJ8SulJXTwE'
bot = telepot.Bot(token = telgm_token)

step = 0
scheduleList =[]
schedule = []   

def handle(msg):
    global step, scheduleList, schedule
    print(step)
    content_type, chat_type, chat_id = telepot.glance(msg)
    # print(msg['text'])
    # # msg['text'] is gotten user's last message

    # if content_type == 'text':
    #     bot.sendMessage(chat_id, msg['text'])
    
    if step == 0:
        mon = {'월요일': msg['text'].split(' ')}
        schedule.append(mon)
    if step == 1:
        tue = {'화요일': msg['text'].split(' ')}
        schedule.append(tue)
    if step == 2:
        wed = {'수요일' : msg['text'].split(' ')}
        schedule.append(wed)
    if step == 3:
        thu = {'목요일' : msg['text'].split(' ')}
        schedule.append(thu)
    if step == 4:
        fri = {'금요일' : msg['text'].split(' ')}
        schedule.append(fri)
    if step == 5:
        schedule.append(msg['text']) # name
        schedule.append(chat_id) # id
        step = 0
        scheduleList.append(schedule)
        schedule = []
        print(scheduleList)
    step += 1


bot.message_loop(handle)

arr = ['월요일','화요일','수요일','목요일','금요일']

while True:
    # [{월 일정 ... 금 일정}, 이름, id]
    time.sleep(10)
    dt = datetime.datetime.now()
    now = str(dt.hour) + ':' + str(dt.hour)
    try:
        day = arr[dt.weekday()]
    except:
        time.sleep(10)
        continue
    # 수요일일 경우 5교시 까지만 하기 ========================
    if day == '수요일':                                  #==
                                                        #==
        if now == first:                                #==
            for x in scheduleList:                     
                res = x[arr[day]][0]
                bot.sendMessage(x[2], res + ' 강의를 들을 시간입니다')
        if now == second:
            for x in scheduleList:
                res = x[arr[day]][1]
                bot.sendMessage(x[2], res + ' 강의를 들을 시간입니다')

        if now == third:
            for x in scheduleList:
                res = x[arr[day]][2]
                bot.sendMessage(x[2], res + ' 강의를 들을 시간입니다')

        if now == fourth:
            for x in scheduleList:
                res = x[arr[day]][3]
                bot.sendMessage(x[2], res + ' 강의를 들을 시간입니다')

        if now == fifth:
            for x in scheduleList:
                res = x[arr[day]][4]
                bot.sendMessage(x[2], res + ' 강의를 들을 시간입니다')
        
        if now == sixth: 
            for x in scheduleList:                   #==
                res = x[arr[day]][5]                 #==
                bot.sendMessage(x[2], res + ' 강의를 들을 시간입니다')           #==
                                                     #==
    # ==================================================
    # 수요일이 아닐경우
    else:
        if now == first:
            for x in scheduleList:
                res = x[arr[day]][0]
                bot.sendMessage(x[2], res + ' 강의를 들을 시간입니다')
        if now == second:
            for x in scheduleList:
                res = x[arr[day]][1]
                bot.sendMessage(x[2], res + ' 강의를 들을 시간입니다')

        if now == third:
            for x in scheduleList:
                res = x[arr[day]][2]
                bot.sendMessage(x[2], res + ' 강의를 들을 시간입니다')

        if now == fourth:
            for x in scheduleList:
                res = x[arr[day]][3]
                bot.sendMessage(x[2], res + ' 강의를 들을 시간입니다')

        if now == fifth:
            for x in scheduleList:
                res = x[arr[day]][4]
                bot.sendMessage(x[2], res + ' 강의를 들을 시간입니다')
        
        if now == sixth: 
            for x in scheduleList:
                res = x[arr[day]][5]
                bot.sendMessage(x[2], res + ' 강의를 들을 시간입니다')
            
        if now == seventh: 
            for x in scheduleList:
                res = x[arr[day]][6]
                bot.sendMessage(x[2], res + ' 강의를 들을 시간입니다')
                