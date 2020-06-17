#!/bin/bash
host=redis
previous=`redis-cli -h $host  get current`
if [ -z "$previous" ]
then
    redis-cli -h $host set current 0
    previous=0
fi

((next=previous+1))
awk -v num=$next -F, '{ print "SET",  "__" num "__" "\""$1"\"", "\""$0"\"" }' /sample.csv | redis-cli -h $host --pipe
redis-cli -h $host incr current
redis-cli -h $host keys "__"$previous"__*" | xargs redis-cli -h $host del 
