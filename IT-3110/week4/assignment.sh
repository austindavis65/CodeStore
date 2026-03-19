#!/bin/bash

VAR=$#
ip=$1
option=$2
user=$3

one () {
    if ping -c 1 -W 2 $ip &> /dev/null; then
	    echo "$ip is awake"
    else
	    echo "$ip is not awake"
    fi
}

two () {
    ssh -o 'StrictHostKeyChecking no' $user@$ip "service apache2 status | sed -n '3p' | awk '{ print \$2 }'"
}

three () {
    ssh -o 'StrictHostKeyChecking no' $user@$ip "df | egrep /$ | awk '{ print \$5 }'"
}

four () {
    ssh -o 'StrictHostKeyChecking no' $user@$ip "hostname"
}

five () {
    ssh -o 'StrictHostKeyChecking no' $user@$ip "who | wc -l"
}


cmd () {
    if [ $option = 1 ]; then
	    one
    elif [ $option = 2 ]; then
	    two
    elif [ $option = 3 ]; then
	    three
    elif [ $option = 4 ]; then
	    four
    elif [ $option = 5 ]; then
	    five
    else
	    echo "Invalid option" 
    fi
}


main () {
    if [ $VAR != 3 ]; then
	    echo "Incorrect operation"
	    echo "Usage: ./assignment ip option user"
	    echo "1: Test if host is awake"
	    echo "2: Get apache process status on remote host"
	    echo "3: Get disk percentage"
	    echo "4: Get hostname"
	    echo "5: Display logged in users"
	    exit 1
    else
	    cmd
    fi
}

[[ "$0" == "${BASH_SOURCE[0]}" ]] && main "$@" || true
