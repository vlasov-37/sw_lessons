for lesson_count in range(1, 11):
    lessons_time = lesson_count * 45
    break_time_5 = ((lesson_count - 1) - ((lesson_count - 1) // 2)) * 5
    break_time_15 = (lesson_count - 1) // 2 * 15
    total_time = break_time_5 + break_time_15 + lessons_time
    hours = total_time // 60
    minutes = total_time - hours * 60
    time = str(hours + 9) + ":" + str(minutes)
    print(str(lesson_count) + " урок заканчивается в " + time)
