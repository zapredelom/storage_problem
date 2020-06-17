#!/bin/bash
host=redis
previous=`redis-cli $host  get current`
if [ -z "$previous" ]
then
    redis-cli $host set current 0
    previous=0
fi

((next=previous+1))
awk -v num=$next -F, '{ print "SET",  "__" num "__" "\""$1"\"", "\""$0"\"" }' /sample.csv | redis-cli $host --pipe
redis-cli $host incr current
redis-cli $host keys "__"$previous"__*" | xargs redis-cli $host del
