data = [int(i) for i in open('17.txt')]

all_counter = 0

for i in range(0, len(data) - 2):

    mx = -1000000
    pre_res = [data[i], data[i + 1], data[i + 2]]

    try:
        cnt = 0
        if str(pre_res[0])[-1] == "2" and str(pre_res[0])[-2] == "4":
            cnt += 1
        if str(pre_res[1])[-1] == "2" and str(pre_res[1])[-2] == "4":
            cnt += 1
        if str(pre_res[2])[-1] == "2" and str(pre_res[2])[-2] == "4":
            cnt += 1

        if cnt >= 2:
            all_counter += 1
            mx = max(mx, pre_res[0] * pre_res[1] * pre_res[2])


    except Exception as e:
        print(e)
