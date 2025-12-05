#!/bin/bash

function get_lang () {
  cmd=$(ls /usr/games/ | shuf -n 1)
  echo "Going to render text in $cmd"
}

function do_foo() {
echo "This script will first render whatever it finds at /foo.txt into some funny language"
[ ! -f /foo.txt ] &&  echo "ERROR: /foo.txt not found!" && return 1


local cmd=''
get_lang
echo "here is the plaintext"
cat /foo.txt
echo "here is translated text"
cat /foo.txt | exec $cmd
echo 
}

function do_fortune() {
echo "Now I will render a fortune, if you have it installed, into some funny language"
[ ! -f /usr/games/fortune ] &&  echo "ERROR: Fortunes package not found!" && return 1
local cmd=''
get_lang
f=$(fortune)
echo "Here is the original fortune"
echo "$f"
echo "Here is the translated version"
echo "$f" | $cmd
echo
}

function check_var() {
echo "Now checking to see if an environment variable DOCK_EXAM exists with correct content"

[ -z $DOCK_EXAM ] &&  echo "ERROR: DOCK_EXAM environment var not found!" && return 1

[ $DOCK_EXAM == "halloween" ] && echo "Contents are successful."  || echo "DOCK_EXAM env var has incorrect contents"

}
function check_bind_mount() {
echo "Now checking to see if bind mount is working correctly"
#can I write something to the path?
[ ! -d /text ] &&  echo "ERROR: Bind path not found!" && return 1

echo "Here is a sample file " > /text/test1.txt

}


echo "******************"
do_foo
echo "******************"
do_fortune
echo "******************"
check_var
echo "******************"
check_bind_mount
echo "******************"

