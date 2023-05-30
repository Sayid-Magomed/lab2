color = ('красный', 'синий', 'желтый')
color1 = input('первый цвет: ', )
color2 = input('второй цвет: ', )
if color1 in color and color2 in color:
    if color1 != color2:
        if color1 in ('красный', 'синий') and color2 in ('красный', 'синий'):
            print('фиолетовый')
        elif color1 in ('красный', 'желтый') and color2 in ('красный', 'желтый'):
            print('оранжевый')
        elif color1 in ('синий', 'желтый') and color2 in ('синий', 'желтый'):
            print('зеленый')
    else:
        print('одинаковые цвета')
else:
    print('неправильный цвет')