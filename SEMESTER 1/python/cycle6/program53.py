class Time:
    def __init__(self):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0

    def set_time(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        total_seconds_self = self.__hour * 3600 + self.__minute * 60 + self.__second
        total_seconds_other = other.__hour * 3600 + other.__minute * 60 + other.__second

        total_seconds_sum = total_seconds_self + total_seconds_other

        hours = total_seconds_sum // 3600
        minutes = (total_seconds_sum % 3600) // 60
        seconds = total_seconds_sum % 60

        result = Time()
        result.set_time(hours, minutes, seconds)
        return result

    def display_time(self):
        print(f"Time: {self.__hour}:{self.__minute}:{self.__second}")


hour1 = int(input("Enter hours for time 1: "))
minute1 = int(input("Enter minutes for time 1: "))
second1 = int(input("Enter seconds for time 1: "))

hour2 = int(input("Enter hours for time 2: "))
minute2 = int(input("Enter minutes for time 2: "))
second2 = int(input("Enter seconds for time 2: "))

time1 = Time()
time1.set_time(hour1, minute1, second1)

time2 = Time()
time2.set_time(hour2, minute2, second2)

result_time = time1 + time2

print("\nTime 1:")
time1.display_time()

print("\nTime 2:")
time2.display_time()

print("\nSum of Time 1 and Time 2:")
result_time.display_time()
