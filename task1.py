#!/usr/bin/env python
import os
import glob
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group1 = parser.add_mutually_exclusive_group()
group.add_argument("--parent", help="Search only in parent folder", action="store_true")
group.add_argument("--recursive", help="Search recursively", action="store_true")
parser.add_argument("--extension", nargs=1, help="Filter files by extension")
parser.add_argument("--path", nargs='?', default='./', action="store", help='Path to search')
group1.add_argument("--byname", action="store_true", help="Orders files by name")
group1.add_argument("--bydate", action="store_true", help="Orders files by date")
args = parser.parse_args()


def parent(path):
    files_all = [f for f in glob.glob(path + "/*", recursive=True)]
    files = [f for f in files_all if os.path.isfile(f)]
    return files


def recursive(path):
    files_all = [f for f in glob.glob(path + "**/*", recursive=True)]
    files = [f for f in files_all if os.path.isfile(f)]
    return files


if args.parent:
    new = parent(args.path)
    if args.extension:
        new = [f for f in new if f.endswith("." + args.extension[0])]
        if args.extension and not args.byname and not args.bydate:
            print("\n".join(new))
            exit()
    if args.bydate:
        new.sort(key=os.path.getmtime)
        print("\n".join(new))
        exit()
    if args.byname:
        print("\n".join(sorted(new)))
        exit()
    print("\n".join(new))
    exit()


if args.recursive:
    new = recursive(args.path)
    if args.extension:
        new = [f for f in new if f.endswith("." + args.extension[0])]
        if args.extension and not args.byname and not args.bydate:
            print("\n".join(new))
            exit()
    if args.bydate:
        new.sort(key=os.path.getmtime)
        print("\n".join(new))
        exit()
    if args.byname:
        print("\n".join(sorted(new)))
        exit()
    print("\n".join(new))
    exit()
