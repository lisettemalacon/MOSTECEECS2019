binned_output_list = []
first = [0.0,1.0,0.45,0.3,0.5,0.2,0.95]
second = [0.5,0.5,0.314159,0.31459,1,1,0.99]
third = [2.1,0.1,2.8,3.1,3.102,0.565]

def bitDepthConverter(data,depth):
    discrete_bins = 2 ** depth
    bin_voltage = 3.3 / (discrete_bins)
    for number in data:
        if number != 0:
            binned_output = int(number / bin_voltage)
            binned_output_list.append(binned_output)
        else:
            binned_output = 0
            binned_output_list.append(binned_output)
    return binned_output_list




