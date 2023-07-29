#!/bin/bash

# Using for loop to iterate from 100 to 1
for (( i = 100; i >= 1; i-- )); do
    unzip "$i.zip"
    # Add your desired commands or actions here, if needed
done

