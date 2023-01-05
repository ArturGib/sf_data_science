#Game - "Guess the number"
#"The computer itself guesses the number and guesses itself"

import numpy as np

def predict_in_section(number, start_point, end_point) -> tuple:
    """Возвращает отрезок в котором находится число
        Функция вызывается в основном цикле поиска до тех пор,
        пока начальная и конечная точка отрезка не совпадут.
        Поиск числа основан на бинарном поиске.
    Args:
        number (_int_): _looking for this number_
        start_point (_int_): _start point in section_
        end_point (_int_): _end point in section_
        
    Returns:
        tuple: (start_point:int, end_point:int) start and end point of section
    """    
    center = (start_point+end_point)/2 
    center_min = int(center) 
    center_max = center_min if center_min == center else center_min+1
    
    if number == center:
        return center, center
    elif number<center:
        return start_point, center_min
    else:
        return center_max, end_point
             
        
def predict_random(number:int = 1) -> int:
    """Возвращает число попыток угадывания случайного числа number

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Номер попытки с которой удалось угадать число
    """    
    count = 0
    start_point = 1
    end_point = 100
    while True:
        count += 1
        #predict_number = np.random.randint(1, 101) 
        start_point, end_point = predict_in_section(number, start_point, end_point)
        if start_point == end_point:
            return count
        

def score_game(predict_random) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает 
    алгоритм

    Args:
        predict_random (_type_): функция угадывания

    Returns:
        int: average guessing count
    """    
    
    count_ls = [] # список для сохранения количества попыток
    #np.random.seed(10) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(predict_random(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == "__main__":
     
    score_game(predict_random)