#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

def pluck(fname):
    for farm in farms:
        if farm["name"] == fname:
            print(f"Here at the {fname} we have: ")
            for animals in farm["agriculture"]:
                print(animals)

def main:

