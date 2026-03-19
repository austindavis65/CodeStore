#!/bin/bash


log=$1


function menu {
	echo "Menu: "
	echo "	1. Log unique invalid user attempts"
	echo "	2. Log unique ips"
	echo "	3. Log user login on date"
	echo "	4. Quit"
	echo ""

}


function usage {
	echo "Invalid operation:"
	echo "	Usage: ./parse_log <logfile>"
}


function filegone-usage {
	echo "Invalid operation:"
	echo "	File doesn't exist"
}


function one {
	echo "Cleaning out old users.txt"
	> users.txt
	echo "Old users.txt cleaned"
	echo ""
	echo "Parsing invalid users to users.txt"
	zcat "$log" | grep "invalid" | awk '{print $10}' | sort | uniq >> users.txt
	echo "Invalid users parsed"
}

function two {
	echo "Cleaning out old ips.txt"
	> ips.txt
	echo "Old ips.txt cleaned"
	echo ""
	echo "Parsing IP addresses to ips.txt"
	zcat "$log" | awk '/sshd/{ for (i=1; i<=NF; i++) { if ($i == "from") { print $(i+1); break }}}' | sort | uniq >> ips.txt
	
	head -2372 ips.txt > tmp.txt
	mv tmp.txt ips.txt

	echo "IP addresses parsed"
}

function three {
	echo "Cleaning out old early_users.txt"
	> early_users.txt
	echo "Old early_users.txt cleaned"
	echo ""
	read -p "What month do you want to check? Please use three letter abbrevation with the first letter capitalized: " month
	read -p "What day do you want to check? Please add no leading 0's: " day
	echo "Parsing early users on $month $day from 11:00 AM - 11:15:59 AM to early_users.txt"
	zcat "$log" | egrep "^${month}[[:space:]]+${day}[[:space:]]+11:(0[0-9]|1[0-5]):[0-9]{2}" | egrep -o "invalid user [^ ]+|for [^ ]+|user=[^ ]+" | awk '{print $NF}' | sed 's/^user=//' | sort | uniq > early_users.txt
	echo "Early users parsed"
}

function four {
	echo "Quitting"
	echo ""
	sleep 1
	exit 0
}


function main {
	if [ $# != 1 ]; then
		usage
	elif [ -f $log ]; then
		while true; do
			menu
			read -p "Option: " option
			if [ $option = 1 ]; then
				echo ""
				one
				echo ""
			elif [ $option = 2 ]; then
				echo ""
				two
				echo ""
			elif [ $option = 3 ]; then
				echo ""
				three
				echo ""
			elif [ $option = 4 ]; then
				echo ""
				four
			else
				echo "Invalid option try again"
				echo ""
			fi
		done
	else
		filegone-usage
	fi

}

[[ "$0" == "${BASH_SOURCE[0]}" ]] && main "$@" || true
