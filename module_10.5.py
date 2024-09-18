import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
'''start = datetime.datetime.now()
for filename in filenames:
    read_info(filename)
end = datetime.datetime.now()
print(end - start)'''


# Многопроцессный
if __name__ == '__main__':
    start = datetime.datetime.now()
    with Pool(processes=4) as pool:
        results = pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start)
