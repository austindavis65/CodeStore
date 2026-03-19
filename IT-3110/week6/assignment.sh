#!/bin/bash

usage() {
    echo "./assignment.sh url startip user <remove>"
    exit 1
}

get_file() {

    url="$1"
    filename="$2"

    curl -s "$url" -o "/tmp/bad_$filename"

    tail -n +3 "/tmp/bad_$filename" > "/tmp/$filename"
    echo "/tmp/$filename"
}

generate_dhcp_entry() {

    firstname="$1"
    lastname="$2"
    mac="$3"
    currentip="$4"
    filename="$5"

    {
        echo "  host ${firstname}-${lastname} {"
        echo "  hardware ethernet $mac;"
        echo "  fixed-address 10.50.100.$currentip;"
        echo "}"
    } >> "$filename"
}

myssh() {

    command="$1"
    user="$2"

    result=$(ssh -n -o 'StrictHostKeyChecking no' "${user}@vm.cs.utahtech.edu" "${command}")
    echo $result
}

main() {

    if [ $# -lt 3 ] || [ $# -gt 4 ]; then
        usage
    fi

    url="$1"
    currentip="$2"
    user="$3"
    action="$4"

    filename=$(basename "$url")
    dhcpfile="/tmp/dhcpconf.txt"

    > "$dhcpfile"

    cleanfile=$(get_file "$url" "$filename")

    while read id username firstname lastname rest; do

        hostname="${firstname}-${lastname}-${currentip}"

        if [ "$action" == "remove" ]; then

            myssh "/qemu/bin/citv removevm $hostname" "$user"

        else

            myssh "/qemu/bin/citv clonevm f23_jammy_partitioned_dhcp $hostname 256 2083" "$user"

            mac=$(myssh "/qemu/bin/citv showvm | awk '\$1 == $hostname {print \$6; exit}'" "$user")

            generate_dhcp_entry "$firstname" "$lastname" "$mac" "$currentip" "$dhcpfile"

        fi

        ((currentip++))

    done < "$cleanfile"

}

[[ "$0" == "${BASH_SOURCE[0]}" ]] && main "$@"
