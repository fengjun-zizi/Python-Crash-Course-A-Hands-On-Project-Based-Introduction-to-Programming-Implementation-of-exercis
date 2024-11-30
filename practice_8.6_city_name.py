# 定义一个全局列表
all = []

def city_ame(state='continue'):
    while state == 'continue':
        country = input('Country: ')
        city = input('City: ')
        print(f"{country}, {city}")
        all.append({'country': country, 'city': city})
        state = input('Continue or finish: ')
        if state == 'finish':
            print("\nEntries:")
            for entry in all:
                print(entry) 

            print("\nAll entries:")
            print(all)
            break

city_ame()

