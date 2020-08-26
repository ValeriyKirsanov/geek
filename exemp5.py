seconds = int(input("введите секунды __"))

#a = seconds / 60
#b = seconds // 60
#print(a == b)
if seconds < 60:
    print("0 hour, 0 minute, ", seconds, "seconds")
elif seconds / 60 == seconds // 60 and seconds / 60 < 60:
    minute = seconds // 60
    print("0 hour, ", minute, "minute, 0 seconds")
elif seconds / 60 != seconds // 60 and seconds / 60 < 60:
    minute = seconds // 60
    seconds2 = seconds % 60
    print("0 hour, ", minute, "minute, ", seconds2, " seconds")
elif seconds / 60 == seconds // 60 and seconds / 60 > 60:
    hour = seconds // 3600
    minute = (seconds - hour * 3600) // 60
    seconds2 = (seconds - hour * 3600 - minute * 60)
    print(hour, " hour, ", minute, "minute, ", seconds2, " seconds")
elif seconds / 60 != seconds // 60 and seconds / 60 > 60:
    hour = seconds // 3600
    minute = (seconds - hour * 3600) // 60
    seconds2 = (seconds - hour * 3600 - minute * 60)
    print(hour, " hour, ", minute, "minute, ", seconds2, " seconds")
else:
    print("wats up")
