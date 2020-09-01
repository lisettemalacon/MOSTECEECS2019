def color_code(color1,color2,color3):
    color_values={'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 'green':5, 'blue':6, 'purple':7, 'gray': 8, 'white': 9}
    return (color_values[color1] * 10 + color_values[color2]) * 10**color_values[color3]
