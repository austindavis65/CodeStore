#!/bin/bash

machine="$1"
column="$2"
url="$3"
file="/tmp/sample.txt"

get_file() {
    wget -q -O "$file" "$url"

    tail -n +3 "$file" > "${file}.tmp"
    mv "${file}.tmp" "$file"
}

get_column() {
	result=$(grep -w "$machine" "$file" | awk -v col="$column" '{print $col}')
}

show_output() {
    echo "$result"
}

make_dhcp() {
    get_file
    mac=$(grep -w "$machine" "$file" | awk '{print $2}')
    ip=$(grep -w "$machine" "$file" | awk '{print $3}')

    echo "host $machine {"
    echo "hardware ethernet $mac;"
    echo "fixed-address $ip;"
    echo "}"

}

make_dns() {
    get_file
    ip=$(grep -w "$machine" "$file" | awk '{print $3}')
    printf "$machine\tIN\tA\t$ip\n"  
}

main() {
    get_file
    get_column
    show_output
}

[[ "$0" == "${BASH_SOURCE[0]}" ]] && main "$@" || true
