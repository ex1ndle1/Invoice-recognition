from PIL import Image
import pytesseract
from language_choice import language_change
from translater import translate
from json import dump,loads


pytesseract.pytesseract.tesseract_cmd = r"D:\tesseract osr\tesseract.exe"#########################ustanovka yolini qoyishiz kerak

image  = "invoice.png"

###################################################################shu yertga xohlagann invoiceni qoyishiz mumkin
image = Image.open(image)

text = pytesseract.image_to_string(image, lang='eng') 


print("result:\n")


actual_lang = language_change(text)
text = pytesseract.image_to_string(image, lang=actual_lang)

translated_text = translate(text)


#######################  ai javobida """   olib tashlashni roragan edim, lekin u chunmadi, shuning uchun json formatga otkazayotganida """ json ni olib tashlaydi
result = translated_text.replace("```json", "").replace("```", "").strip()
parsed = loads(result)



with open('results.json','w',encoding='utf-8') as f:
    dump(parsed,f,indent=5,ensure_ascii=False)




print(parsed)