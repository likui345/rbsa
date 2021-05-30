# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
name = sys.argv[1]

def print_hi(name):
    with open(name, "r") as f:
        gfa = {}
        for each in f:
            l = each.strip().split()
            if len(l) !=9 or l[0] != 'A' :
                continue
            if l[1] not in gfa:
                gfa[l[1]] = [each]
            else:
                gfa[l[1]].append(each)
    #for key in gfa.keys():
     #   print(key,gfa[key])
    utg = {}
    for key in gfa.keys():
        utg[key] = []
    utg_len = dict.fromkeys(gfa.keys(),0)
    #for key in gfa.keys():
     #   print(key,utg_len[key])
    utg_overlap = dict.fromkeys(gfa.keys(),0)
    for key in gfa.keys(): 
        pre = None
        for l in gfa[key]:
            if pre == None :
                pre = l.strip().split()
                pre[2] = int(pre[2])
                pre[6] = int(pre[6])
                #print(type(pre),pre[0],pre[1],pre[2],pre[3],pre[4],pre[5])
                #print(pre)
                if  pre[3] == '-' :
                    utg[key].append(pre[4] + ':B')
                elif  pre[3] == '+' :
                    utg[key].append(pre[4] + ':E')
            else:
                #print(pre)
                #print(type(pre),pre[0],pre[1],pre[2],pre[3],pre[4],pre[5])
                l = l.strip().split()
                l[2] = int(l[2])
                l[6] = int(l[6])
                if  l[3] == '-' :
                    #print(pre[2])
                    utg[key].append(l[4] + ':B')
                    #print(l[2],pre[2])
                    utg_len[key] += l[2] - pre[2]
                    utg_overlap[key] += abs(l[6] - l[2] + pre[2] )
                elif  l[3] == '+' :
                    utg[key].append(l[4] + ':E')
                    utg_len[key] += l[2] - pre[2]
                    utg_overlap[key] += abs(l[6] - l[2] + pre[2] )
                pre = l
    for key in utg.keys():
        if(len(utg[key])>1):
            print(key,utg[key][0],utg[key][1],utg[key][-1],utg_len[key],utg_overlap[key],"~".join(utg[key]))
        else:
            print(key,utg[key][0],utg[key][0],utg[key][-1],utg_len[key],utg_overlap[key],"~".join(utg[key]))
if __name__ == '__main__':
    print_hi(name)




