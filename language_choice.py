import ollama




def language_change(text):
    

    response = ollama.chat(
    model='deepseek-v3.1:671b-cloud', 
    messages=[
        {"role": "system", "content": "ты ассистент,который будет выбирать на каком языке написан текст(исходя из контекста),который тебе отправит пользователь. Ты должен только отправить одно слово а именно язык. Вот языки (chi_tra,chi_sim,eng,rus). "},
        {"role": "user", "content": text}
    ]
)

    return(response['message']['content'])

    

