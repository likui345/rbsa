#!/usr/bin/env python
# coding: utf-8

#from string import maketrans
import argparse


def reverse_end(node_id):
    node_id, end = node_id.split(":")
    new_end = "B" if end == "E" else "E"
    return node_id + ":" + new_end

def find_chr_path(agp,ctg_paths):
    chr_path = {}
    ctg_dir = {}
    with open(agp,'r') as f:
        for each in f:
            each = each.strip().split()
            if each[4] == "U":
                continue
            ctg_dir[each[5]] = each[8]
            if int(each[7]) <= 500000 :
                continue
            if each[0] not in chr_path:
                chr_path[each[0]] =  [each[5]]
            else:
                chr_path[each[0]].append(each[5])
    
    #for each in chr_path:
     #   for i in chr_path[each]:
      #      print i
       # print "lk"
    ctg_path = {} 
    with open(ctg_paths,'r') as f:
        for each in f:
            each = each.strip().split()
            if each[0] not in ctg_dir.keys():
                continue
            if ctg_dir[each[0]] == '+':

                ctg_path[each[0]] = each
            else :
                path = [ reverse_end(i) for i in each[6].split("~")]
                #print(path)
                path = list(reversed(path))
                s = path[0]
                if len(path) == 1:
                    v = path[0]
                else:
                    v = path[1]
                t = path[-1]
                path = '~'.join(path)
                ctg_path[each[0]] = [each[0],s,v,t,each[4],each[5],path]
    with open("ctg_paths","w") as f:
        for each  in ctg_path:
            each = ctg_path[each]
            f.write("\t".join(each))
            f.write("\n")
    f = open("chr_paths","w")
    #print(chr_path)
    for each  in chr_path.keys():
        name = each
        each = chr_path[name]
        begin = ctg_path[each[0]][1]
        v = ctg_path[each[0]][2]
        end = ctg_path[each[-1]][3]
        length = int(ctg_path[each[0]][4])
        score = int(ctg_path[each[0]][5])
        pre =  ctg_path[each[0]][3]
        
        
        path = []
        path.append(ctg_path[each[0]][6])
        #print each[0]
        i = 1
        while i < len(each):
            #print each[i]
            length += int(ctg_path[each[i]][4])
            score += int(ctg_path[each[i]][5])
            if pre == ctg_path[each[i]][1]:
                #print(ctg_path[each[i]][1])
                path.append(ctg_path[each[i]][6])
            else:
                path.append("~".join((pre,"gap",ctg_path[each[i]][1])))
                print((name,pre,"gap",ctg_path[each[i]][1]))
                path.append(ctg_path[each[i]][6])
            pre = ctg_path[each[i]][3]
            i += 1
        #print "lk"
        path = "|".join(path)
        f.write("\t".join((name,begin,v,end,str(length),str(score),path)))
        f.write("\n")
        
    f.close()
if __name__ == '__main__':
    parser =  argparse.ArgumentParser(usage = """chr_path_tiling.py  --agp AGP --ctg_paths CTG_PATHS""",description = "get chr_paths using agp files and ctg_paths")
    parser.add_argument('--agp',type=str,help="agp file form contig anchoring")
    parser.add_argument('--ctg_paths',type=str,help="ctg_paths from falcon")
    arg = vars(parser.parse_args())
    agp = arg["agp"]
    ctg_paths = arg["ctg_paths"]
    find_chr_path(agp,ctg_paths)
