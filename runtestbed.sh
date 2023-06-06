#!/bin/bash

program="/path/to/your/program.py"  # Replace with the actual path to your Python script

# Random inputs for option 4
ip_option4="example.com"  # Replace with the desired IP or host for option 4
s_option4=1800  # Duration in seconds for option 4
p_t_option4=1.5  # Ping interval for option 4
n_hops_option4=10  # Number of hops for option 4

# Random inputs for option 5
t_option5=1800  # Duration in seconds for option 5
ip_option5="example.com"  # Replace with the desired Gateway IP for option 5

# Run the program and provide user input for options 4 and 5
python3 "$program" <<EOF
4
$ip_option4
$s_option4
$p_t_option4
$n_hops_option4
EOF

sleep $s_option4

python3 "$program" <<EOF
5
$t_option5
$ip_option5
EOF
