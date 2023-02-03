#!/bin/bash


while true; do
read -rsn1 input
if [ "$input" = "^[5~" ]; then
    echo "hello world"
fi
done