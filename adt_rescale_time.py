import numpy as np
class ADT_rescale_time:
    def __init__(self):
        super(ADT_rescale_time, self).__init__()

    def match_time_sampling(self, time_array, sampling_rate=0.02):
        new_time_array = []

        for t in time_array:
            t = float(t)
            q, r = divmod(t, sampling_rate)
            low_v = q * sampling_rate
            high_v = (q + 1) * sampling_rate

            low_r = abs(t - low_v)
            high_r = abs(t - high_v)

            if low_r < high_r:
                low_v = round(low_v, 2)
                new_time_array.append(low_v)
            else:
                high_v = round(high_v, 2)
                new_time_array.append(high_v)

        return new_time_array

    def rescale_ADT(self, txt_file, del_array=['\t', '\n', ' ']):
        data = open("./" + txt_file + ".txt", 'r')

        time_drum = []
        time = []
        drum = []

        for t_d in data:
            for del_i in del_array:
                t_d = t_d.replace(del_i, '')
            time_drum.append(t_d)
            time.append(t_d[:-2])
            drum.append(t_d[-2:])

        rescale_time = self.match_time_sampling(time)
        return time, rescale_time, drum