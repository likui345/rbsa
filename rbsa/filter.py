def print_hi(overlap_file):
    overlap_data = []
    overlap = {}
    with open(overlap_file) as f:
        for line in f:
            l = line.strip().split()
            if len(l) != 12 :
                continue
            score = int(l[8]) - int(l[7])
            if score < 2000:
                continue
            if int(l[1]) < 10000 or int(l[6]) < 10000 or int(l[1]) == int(l[3]) - int(l[2]) or int(l[6]) == int(l[8]) - int(l[7]):
                continue
            if l[0] not in overlap:
                overlap[l[0]] = [tuple(l)]
            else:
                overlap[l[0]].append(tuple(l))


    for key in overlap.keys():
        overlap[key].sort(key= lambda x :  int(x[2]) - int(x[3]) )
        tmp = overlap[key]
        if len(tmp) <= 5 :
            continue
        if len(tmp) <= 20:
            overlap_data.extend(tmp)
        else:
            overlap_data.extend(tmp[0:20])
    with open('filter.overlap.paf','w') as f:
        for each in overlap_data:
            f.write('\t'.join(each))
            f.write('\n')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import sys
    overlap_file = sys.argv[1]
    print_hi(overlap_file)
