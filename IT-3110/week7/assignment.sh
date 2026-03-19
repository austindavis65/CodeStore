#! /bin/bash

email=$1
ip=$2
dnumber=$3

function one {
	egrep "^car.*s$" /usr/share/dict/words
}

function two {
	egrep "rya" /usr/share/dict/words
}

function three {
	egrep "mail|chick" /usr/share/dict/words
}	

function four {
	egrep "[^aeiou]{8}" /usr/share/dict/words
}

function five {
	egrep "^.{15}$" /usr/share/dict/words
}

function six {
	egrep "ux$" /usr/share/dict/words
}

function seven {
	egrep "^[b|s].*zz.*$" /usr/share/dict/words
}

function eight {
	egrep "^(.)(.).\2\1$" /usr/share/dict/words
}

function nine {
	egrep "^(.)(.)(.).{0,1}\3\2\1$" /usr/share/dict/words
}

function ten {
	egrep "^[^aeiou]*a[^aeiou]*e[^aeiou]*i[^aeiou]*o[^aeiou]*u[^aeiou]*$" /usr/share/dict/words
}

function eleven {
	egrep "^.*([a-z])\1([a-z])\2([a-z])\3.*$" /usr/share/dict/words
}

function twelve {
	egrep "^[^A-Z].*'.*[^A-Z][^s]$" /usr/share/dict/words
}

function thirteen {
	egrep "^[a-z][a-z]$" /usr/share/dict/words	
}

function fourteen {
    if echo "$email" | egrep -q '^[^@]+@[^@]+\.[^@]+$'; then
        echo "$email is valid"
    else
        echo "$email is invalid"
    fi
}

function fifteen {
    if echo "$ip" | egrep -q '^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$'; then
        echo "$ip is valid"
    else
        echo "$ip is invalid"
    fi
}

function sixteen {
    if echo "$dnumber" | egrep -q '^d[0-9]{8}$'; then
        echo "$dnumber is valid"
    else
        echo "$dnumber is invalid"
    fi
}

function main {
	> wc.txt
	one
	two
	three
	four
	five
	six
	seven
	eight
	nine
	ten
	eleven
	twelve
	thirteen
	fourteen
	fifteen
	sixteen
}

[[ "$0" == "${BASH_SOURCE[0]}" ]] && main "$@" || true
