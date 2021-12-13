import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    lower_limit = 1
    upper_limit = 101
    
    while True:
        count+=1
        
        predict_number = (lower_limit + upper_limit)// 2
        
        if number > predict_number:
            lower_limit = predict_number  # смещение нижней границы поиска числа

        elif number < predict_number:
            upper_limit = predict_number  # смещение верхней границы поиска числа

        else:
            break
    return count
  
  
def score_game(random_predict) -> int:
    """#За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для вопроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)  

#RUN
if __name__ == '__main__':
     score_game(random_predict)


