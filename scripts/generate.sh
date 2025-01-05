#!/bin/bash

# Remove all .wav files from the output directory
rm /home/pi/src/pele/output/*.wav

# List of melody scripts
melodies=(
    "melodies/wed.py"
    "melodies/thu.py"
    "melodies/swi.py"
    "melodies/genevive.py"
    "melodies/fea.py"
    "melodies/mor.py"
    "melodies/fie.py"
    "melodies/jun.py"
    "melodies/fas.py"
    "melodies/bey.py"
    "melodies/cop.py"
    "melodies/sun.py"
    "melodies/cia.py"
    "melodies/hoo.py"
    "melodies/hoot.py"
    "melodies/oud.py"
    "melodies/tie.py"
    "melodies/cle.py"
    "melodies/tre.py"
    "melodies/bel.py"
    "melodies/bel2.py"
    "melodies/ren.py"
    "melodies/exh.py"
    "melodies/zof.py"
    "melodies/jul.py"
    "melodies/wai.py"
    "melodies/up.py"
    "melodies/xmi.py"
    "melodies/eve.py"
    "melodies/ewe.py"
    "melodies/repeatallafterfuzz.py"
    "melodies/des.py"
    "melodies/ber.py"
)

# Get the total number of melodies
total_melodies=${#melodies[@]}

# Set the minimum and maximum number of melodies to run
min_melodies=10
max_melodies=$total_melodies

# Generate a random number of melodies to execute, ensuring it's at least $min_melodies
num_melodies_to_run=$((RANDOM % (max_melodies - min_melodies + 1) + min_melodies))

# Shuffle the melodies array and pick the first $num_melodies_to_run elements
shuffled_melodies=($(shuf -e "${melodies[@]}" | head -n $num_melodies_to_run))

# Execute the selected melodies
for melody in "${shuffled_melodies[@]}"; do
    python3 "$melody"
done
