# Импорт нужных библиотек
import gtts
import PyPDF2

# Стартовое сообщение
print('Before you will start, please, put your .pdf file in folder "docs/". Then write only name of your file, for example "MyFile.pdf"')

# Пользователь вводит имя файла
pdfFileName = input("File name: ")
# Пользватель вводит язык текста в файле
fileLang = input("(ru/en) File language: ")

# Проверка на корректный ввод языка
if fileLang == "ru" or fileLang == "en":
    # Оставляет пустую строку, проверка пройдена
    print('')
# Если программе не знаком такой язык
else:
    # Вывод сообщения об ошибке
    print('Wrong language.')
    # Выход из программы
    exit()

# Переменная, обозначающая расположение файла относительно самого скрипта
pdfFileDirection = 'docs/' + pdfFileName

# Проверка на наличие указанного файла
try:
    # Открывает файл
    pdfFile = open(pdfFileDirection, 'rb')

# Если файл не найден
except FileNotFoundError:
    # Выводит сообщение об ошибке
    print("This file doesn't exists.")

# Если файл найден
else:
    # Считывает PDF файл
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    # Заносит кол-во страниц файла в переменную pages
    pages = pdfReader.numPages
    # Добавление переменной fileContent. Позже здесь будет все текстовое содержимое PDF файла
    fileContent = ''

    # Цикл, который перебирает каждую страницу
    for i in range(0, pages):
        # Добавление переменной pageObj, хранит в себе информацию о странице
        pageObj = pdfReader.getPage(i)
        # Из информации о странице получает текст и добавляет его к fileContent
        fileContent += pageObj.extractText()

    # Закрывает PDF-Файл
    pdfFile.close()

    # Озвучка текста
    tts = gtts.gTTS(fileContent, lang=fileLang)
    # Разбивает директорию файла на две части: директория и название файла, а также формат файла
    mp3FileName = pdfFileDirection.split('.')
    # Сохраняет файл в той же директории, где находится PDF-файл, добавляя формат .mp3
    tts.save(mp3FileName[0] + '.mp3')

    # Выводит в консоль сообщение о готовности создания .mp3 файла
    print(f'{mp3FileName[0]}.mp3 is ready.')
