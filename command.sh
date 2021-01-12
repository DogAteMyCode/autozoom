#!/bin/bash

function autozoom() {
	BASEDIR=${$(type -a autoZoom)/\/command.sh/}
	BASEDIR=${BASEDIR/autoZoom is a shell function from /}
	echo $BASEDIR
	python3 $BASEDIR $1
}