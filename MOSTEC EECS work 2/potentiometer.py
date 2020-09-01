def voltage_divider(vcc,ra,rb):
    return vcc*(rb/(ra+rb))

def potentiometer(vin,rp,beta):
    return voltage_divider(vin,(1-beta)*rp,beta*rp)


## vin*(rp*beta / (rp*beta + (1-beta)*rp))
