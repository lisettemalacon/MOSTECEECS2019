import math

def resistanceExtractor(vcc,ra,vout):
    ratio = 1.0*vout/vcc
    r_b = ratio*ra/(1-ratio)
    return r_b


def brightnessExtractor(vcc,ra,vout):
    first = (log(resistanceExtractor(vcc,ra,vout),10) - 8.65) / -2.0
    return 10 ** first

