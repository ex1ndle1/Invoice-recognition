import ollama




def translate(text):
    
    response = ollama.chat(
    model='deepseek-v3.1:671b-cloud',  
    messages=[
        {"role": "system", "content": """ты ассистент которыый должен переводить текст, который тебе отправит пользователь. Ты должен отвечать только готовым ответом. Всегда переводи на английский. Скидывай ответ в формате json,твой ответ будет срзу сохраняться в json файл поэтому отвечай соответствуя синтаксису json. Твой ответ будет записываться в json файл. Твой ответ должен быть таким по типу такого :{
  "header": "©OsB <0017> ATM <770093>",
  "date": "21.02.2019 15:21:51",
  "card": "6390 02** **** **00 42",
  "operation_type": "card to card transfer",
  "operation_date": "21.02.19",
  "operation_time_msk": "15:21:33",
  "operation_id": "984468",
  "sender": "Mayevbgo: **** 0042",
  "recipient": "M card: **** 4176",
  "operation_amount": "4,169.00 RUB",
  "commission": "41.69 RUB",
  "authorization_code": "184383",
  "full_name": "",
  "contact_center": "CONTACT CENTER"
}"""},
        {"role": "user", "content": text}
    ]
)

    return(response['message']['content'])