#!/usr/bin/env bash
# Go through each directory and print the directory name and contribution per user
for i in */; do ( echo ${i}; cd ${i}/.git/.. && git shortlog --all -s -n && echo "" || true; ); done > stats.txt
# Number of lines per projects
# for i in */; do ( echo ${i}; cd ${i}/ &&  git ls-files | xargs wc -l | tail -n 1 && echo "" || true; ); done > total_lines.txt
# Number of current line per projects per user
# for i in */; do ( echo ${i}; cd ${i}/ && git log --format='%aN' | sort -u | while read name; do git log --author="$name" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "%s\t", loc }' -; echo -en "$name\n"; done && echo "" || true; ); done > lines.txt
