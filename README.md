# Установка AnyWord:
- Установите Python (желательно) 3.10 и добавьте Python в PATH при установке.
- В консоли:
```sh
pip install awcon argparse scikit-learn
git clone https://github.com/WiSpace/AnyWord.git
```
- Добавьте папку anyword в PATH

# Использование AnyWord:
- Для запуска кода: `anyword path/to/file.aw`
- Помощь: `anyword -h`
- Файл awl:
Необязательный файл, со списком библиотек для импорта. По стандарту anyword ищет файлы awl с названием main.awl или таким же названием, как у aw файл. Например если файл называется test.aw, anyword будет искать test.awl или main.awl в директории с файлом test.aw.

Вы так же можете написать `anyword --libfile path/to/file.awl`.

В данном файле библиотеки пишутся через новую строку.

# Использование AWLIB (пакетный менеджер):
- Для загрузки библиотек посетите сайт https://awlib.wsm001.repl.co/ со списком библиотек и их описанием. Установка: `awlib --install lib_name`
- Помощь: `awlib -h`

# Использование awcon (написание библиотек для AnyWord на Python):
- В начале файла с библиотекой напишите:
```py
import awcon

__awc__ = awcon.__awc__
__awvar__ = awcon.__awvar__
```
- Функция:
lib/lib.py
```py
# список примеров для обработки ИИ текста
@awcon.awfun(["say", "ask"])
def say(arg1=None, *args):
    print(arg1, *args)
```

Использование данной функции:
test.awl
```
lib
```

test.aw
```
say pls "hello world" and "heey!"
hey! ask user "hey"
```

- Переменные:
```py
awcon.awvar("name", "value")
```