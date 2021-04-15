# amogus-demotivators
Создаёт демотиватор с рандомным текстом, как например здесь: <https://www.youtube.com/watch?v=MV8sI3pR-2Y>

# Установка
Выполняем 2-е команды, чтобы установить
```
pip install -r requirements.txt
pip3 install https://github.com/Infqq/simpledemotivators/archive/main.zip --upgrade
```
# Использование
## Настройки
***
### Рандомный текст
Писать надо через пробел
```py
TEXT = " قالو سوري..."
```
***
### Сохранение картинок
Укажите здесь путь до папки, куда будут всё сохраняться
**Важно! В этой папке должна ещё лежать начальная картинка (`pic_0.jpg`) и все другие должны быть формата `.jpg`**
```py
PATH_PICS = "pics"
```
***
### Начальный текст
Этот текст будет только в картинке `pic_1.jpg`
```py
START_TEXT = "Amogus"
```
***
### Кол-во картинок
Кол-во картинок должно быть меньше рандомного текста 
```py
PICS_NUMBER = 76
```
***
## Ошибки
```
Error text is lower, than your pics
```
> Кол-во картинок должно быть меньше рандомного текста 
***
P.s. В данном случае, может быть другая ошибка
```
Traceback (most recent call last):
  ...
ModuleNotFoundError: No module named 'requests'
```
Чтобы её исправить, нужно выполнить команду, в папке с проектом:
```
pip install -r requirements.txt
```
