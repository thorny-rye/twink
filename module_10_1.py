from time import sleep
from threading import Thread
from datetime import datetime
def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as f:
        for i in range(word_count):
            f.write(f'Какое-то слово №  {i+1}\n')
            sleep(0.1)
        f.close()
    print(f'Завершилась запись в файл {file_name}')

the_start = datetime.now()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
the_end = datetime.now()
res = the_end - the_start
print(res)

t_start = datetime.now()
thr1 = Thread(target=write_words, args=(10, "example5.txt"))
thr2 = Thread(target=write_words, args=(30, "example6.txt"))
thr3 = Thread(target=write_words, args=(200, "example7.txt"))
thr4 = Thread(target=write_words, args=(100, "example8.txt"))
thr1.start()
thr2.start()
thr3.start()
thr4.start()

thr1.join()
thr2.join()
thr3.join()
thr4.join()
t_end = datetime.now()
t_res = t_end - t_start
print(t_res)