#!/bin/bash

readonly RED="\033[1;31m"
readonly GREEN="\033[1;32m"
readonly YELLOW="\033[1;33m"
readonly DEFAULT="\033[0m"

set -euo pipefail

echo -e "${YELLOW}Starting installation..."

REQUIREMENTS=("xxd" "curl" "wget" "git")

. /etc/os-release

install() {

	case "$ID" in
		arch|omarchy)
			yes | sudo pacman -S $@
			;;
		debian|ubuntu|kali)
			sudo apt install $@ -y
			;;
		*)
			echo "Unsupported distro. Try installing xxd."
			;;
	esac
}

install "${REQUIREMENTS[@]}"
clear
echo -e "${GREEN}Requirements intalled successfully!${DEFAULT}"
