from adt_rescale_time import ADT_rescale_time

txt_file = 'SOS_16.ADT'

adt_rescale_time = ADT_rescale_time()
time, rescale_time, drum = adt_rescale_time.rescale_ADT(txt_file)

KD_timing = []
SD_timing = []
HH_timing = []

for n, d in enumerate(drum):
    if d == 'KD':
        KD_timing.append(rescale_time[n])
    elif d == 'SD':
        SD_timing.append(rescale_time[n])
    elif d == 'HH':
        HH_timing.append(rescale_time[n])

f_KD = open("./"+txt_file+"_KD.txt", 'w')
f_KD.write(str(KD_timing)[1:-1])
f_KD.close()

f_SD = open("./"+txt_file+"_SD.txt", 'w')
f_SD.write(str(SD_timing)[1:-1])
f_SD.close()

f_HH = open("./"+txt_file+"_HH.txt", 'w')
f_HH.write(str(HH_timing)[1:-1])
f_HH.close()
