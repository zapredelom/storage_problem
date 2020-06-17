#!/bin/bash
previous=`redis-cli  get current`
if [ -z "$previous" ]
then
    redis-cli set current 0
    previous=0
fi

((next=previous+1))
awk -v num=$next -F, '{ print "SET",  "__" num "__" "\""$1"\"", "\""$0"\"" }' sample.csv | redis-cli --pipe
redis-cli incr current
redis-cli keys "__"$previous"__*" | xargs redis-cli del
