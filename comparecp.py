# -*- coding: utf-8 -*-
import os
import pathlib
import sys


def cpfile(src, dst):
    basename = os.path.dirname(dst)
    if not os.path.exists(basename):
        pathlib.Path(basename).mkdir(parents=True)
    with open(src, 'br') as fr:
        with open(dst, 'bw') as fw:
            fw.write(fr.read())


def getfiles(filelist, root, base='', sub=''):
    if not os.path.isdir(os.path.join(root, base, sub)):
        filelist.append(os.path.join(base, sub))
    else:
        cur_base = os.path.join(base, sub)
        for f in os.listdir(os.path.join(root, cur_base)):
            getfiles(filelist, root, cur_base, f)


def compareandmv(src, dst):
    dstfiles = []
    srcfiles = []

    getfiles(srcfiles, src)
    getfiles(dstfiles, dst)

    print("src total:{src_total}, dst total:{dst_total}".format(
            src_total=len(srcfiles), dst_total=len(dstfiles)))

    for f in srcfiles:
        if f not in dstfiles:
            print("coping {f}".format(f=f))
            cpfile(os.path.join(src, f), os.path.join(dst, f))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("<src> <dst>")
        sys.exit(-1)
    src = sys.argv[1]
    dst = sys.argv[2]
    compareandmv(src, dst)
    print('Done.')
