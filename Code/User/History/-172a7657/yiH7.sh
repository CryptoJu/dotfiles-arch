#!/bin/bash


while true; do
read -rsn4 input
if [ "$input" = "^[5~" ]; then
    echo "hello world"
fi
done