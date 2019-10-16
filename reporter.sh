#!/usr/bin/env bash
# replace with current file path here
deal_path='your project path here'
repo=''
echo "Reporter 0.1.43 |4everlynn, DISVER| (default, Oct 16 2019, 10:56:21) "
while [[ $# -gt 0 ]];
do
    case "$1" in
        -repo)
             shift;
             repo=$1
             shift
             ;;
        *)
             echo "param error"
             echo "output help information"
             exit 1
             ;;
    esac

done

paths=(${repo//,/ })
index=1
for path in ${paths[@]}
do
    cd ${path}
    git log --pretty=format:"%cn[sep]%s[sep]%cd" > ${deal_path}/log-${index}.rep
    let index+=1
done
cd ${deal_path}
python3 core.py