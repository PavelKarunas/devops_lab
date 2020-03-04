#!/usr/bin/env python

import requests
import getpass
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--owner", nargs=1, help="Write repo owner", required=True)
parser.add_argument("--repo", nargs=1, help="Write name of repo")
parser.add_argument("--created", action="store_true", help="Creation date")
parser.add_argument("--updated", action="store_true", help="Last update date")
parser.add_argument("--pushed", action="store_true", help="Last push date")
parser.add_argument("--issues", action="store_true", help="Number of open issues")
parser.add_argument("--subs", action="store_true", help="Number of subscribers")
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

user = str(input("Please enter Github username for authentication:"))
passw = getpass.getpass(prompt='Password: ', stream=None)

if args.repo:
    try:
        req = requests.get('https://api.github.com/repos/' \
        + args.owner[0] + '/' + args.repo[0], auth=(user, passw))
        data = req.json()

    except BaseException:
        print("Bad link provided")
        exit()

    print ("Repository name: " + args.repo[0] + ", Owner: " + args.owner[0])

    if args.created:
        print ("Repository created: " + data['created_at'])

    if args.updated:
        print ("Repository updated: " + data['updated_at'])

    if args.pushed:
        print ("Repository pushed: " + data['pushed_at'])

    if args.issues:
        print ("Number of open issues: " + str(data['open_issues_count']))

    if args.subs:
        print ("Number of subscribers: " + str(data['subscribers_count']))
else:
    try:
        req1 = requests.get('https://api.github.com/users/' \
        + args.owner[0], auth=(user, passw))
        data1 = req1.json()

    except BaseException:
        print("Bad link provided")
        exit()

    print ("Git user name: " + args.owner[0])
    print ("User ID: " + str(data1['id']))
    print ("User public repositories: " + str(data1['public_repos']))
    print ("User private repositories: " + str(data1['total_private_repos']))
