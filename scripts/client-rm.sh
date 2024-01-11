#!/bin/bash
#
# Author: InferenceFailed Developers
# Created on: 02/01/2024
if [ "$EUID" -ne 0 ]; then
  echo "Error: This script requires elevated privileges. Please run as root user."
  exit 1
fi

usage() {
  echo "Usage: $0 -c client_ip [-i interface_name=wg0]"
}

client_ip=""
interface_name="wg0"

while getopts ":c:i:h" opt; do
  case $opt in
    c)
      client_ip="$OPTARG"
      ;;
    i)
      interface_name="$OPTARG"
      ;;
    h)
      usage
      exit 0
      ;;
    \?)
      echo "Invalid option provided: -$OPTARG" >&2
      usage
      exit 1
      ;;
    :)
      echo "Option '-$OPTARG' requires an argument." >&2
      usage
      exit 1
      ;;
  esac
done

if [ -z "$client_ip" ]; then
  echo "Error: Argument \"-c\" is required." >&2
  usage
  exit 1
fi

workdir=/etc/wireguard/clients/$client_ip

wg set $interface_name peer $(cat $workdir/public.key) remove
rm -r $workdir
