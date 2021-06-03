#!/bin/bash

request_url='http://192.168.99.107/.hidden/'
pattern='/">(.*)</a>'

answer=$(curl -iL $request_url)
iter=0


echo "$answer"

while IFS= read -r line
do
    [[ $line =~ $pattern ]]
    echo ${BASH_REMATCH[1]}
done <<< "$answer"