import numpy as np


    
def predict_random(number:int = 1) -> int:
    """Возвращает число попыток угадывания случайного числа number

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Номер попытки с которой удалось угадать число
    """    
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if predict_number == number:
            return count
        

def score_game(predict_random) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает 
    алгоритм

    Args:
        predict_random (_type_): _description_

    Returns:
        int: _description_
    """    
    
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(10) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(predict_random(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

#RUN 
if __name__ == "__main__":
    score_game(predict_random)