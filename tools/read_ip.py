#!/usr/bin/python

with open('/home/raimondeaug/Desktop/fichier_ip_public.txt', 'r') as f:
    lines=f.read().splitlines()

for ip in lines:
    print (ip)
