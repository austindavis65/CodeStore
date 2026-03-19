#! /bin/bash

file=$1
ip=$2
ssh_user=$3
remove=$4
logfile="logfile.log"

function log {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$logfile"
}

function create {
	if [ -f students.txt ]; then
		log "Removing old student.txt"
		rm students.txt
		log "Old student.txt removed Creating new student.txt"
		curl -s "$file" -o students.txt
		log "student.txt created"
	else
		log "Creating student.txt"
		curl -s "$file" -o students.txt
		log "student.txt created"
	fi
	
	current_ip="$ip"

	if [ -f dhcp.txt ]; then
		rm dhcp.txt
	fi

	while read id username first last rest; do

		hostname="${first}-${last}-${current_ip}"
		
		log "Creating VM $hostname"	
		ssh -n "$ssh_user@vm" \ "/qemu/bin/citv clonevm f23_jammy_partitioned_dhcp $hostname 256 2083"
		log "VM $hostname created"

		log "Harvesting MAC address for $hostname"
		mac=$(ssh -n "$ssh_user@vm" \ "/qemu/bin/citv showvm | awk '\$1 == \"$hostname\" {print \$6; exit}'")
		log "MAC address for $hostname harvested"

		log "Adding host and mac to dhcp.txt"
		
		echo "host ${first}-${last} {" >> dhcp.txt
		echo "	hardware ethernet $mac;" >> dhcp.txt
		echo "	fixed-address 10.50.100.$current_ip;" >> dhcp.txt
		echo "}" >> dhcp.txt
		
		log "Added host and mac to dhcp.txt"

		((current_ip++))
	
	done < <(tail -n +3 students.txt)

	log "Sending dhcp.txt to dhcp server and updating dhcp config"
	scp dhcp.txt root@144.38.204.34:/etc/dhcp/dhcp.txt
	ssh root@144.38.204.34 "systemctl restart isc-dhcp-server"
	log "dhcp config updated and restarted"
}

function remove {
	if [ -f students.txt ]; then
		rm students.txt
		curl -s "$file" -o students.txt
	else
		curl -s "$file" -o students.txt
	fi

	current_ip="$ip"

	while read id username first last rest; do

		hostname="${first}-${last}-${current_ip}"
		log "Removing $hostname"
		ssh -n "$ssh_user@vm" \ "/qemu/bin/citv removevm $hostname"
		log "$hostname removed"
		current_ip=$((current_ip+1))

	done < <(tail -n +3 students.txt)
	log "Clearing dhcp config on dhcp server"
	ssh root@144.38.204.34 \
        "echo '' > /etc/dhcp/dhcp.txt && systemctl restart isc-dhcp-server"
        rm students.txt
	log "Cleared"
}

function usage {
    echo "Usage: ./assignment.sh <studentfile> <lastoctetip> <userforssh> [remove]"
    exit 1
}

function main {
	if [ $# -lt 3 ] || [ $# -gt 4 ]; then
		usage
	else		
		if [ "$remove" == "remove" ]; then
			remove
		else
			create
		fi
	fi
}

[[ "$0" == "${BASH_SOURCE[0]}" ]] && main "$@" || true

