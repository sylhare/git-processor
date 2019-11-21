#!/usr/bin/env bash
# Go through each directory and print the directory name and contribution per user
for i in */; do ( echo ${i}; cd ${i}/.git/.. && git shortlog --all -s -n && echo "" || true; ); done > stats.txt