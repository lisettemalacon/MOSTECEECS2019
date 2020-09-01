def voltage_divider(vcc,ra,rb):
    return 1.0*vcc*rb/(ra+rb)


def pull_up(vcc,r,switch):
        if switch == False:
            return voltage_divider(vcc,(r*100000000000000/(r+r*100000000000000)),r*100000000000000)
        else:
            return voltage_divider(vcc,r+0,0)
        
    
