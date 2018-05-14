#!/bin/bash

# Script to grab custom brain files from usb. ###################################################################
# Please add that command in /etc/udev/rules.d/99-usbhook.rules to run script when a usb drive is plugged in
#
#	ACTION=="add",KERNEL=="sd*", SUBSYSTEMS=="usb", ATTRS{product}=="*", RUN+="/home/botserv/usbhook.sh %k"
#
#	(Change run command according to the location of that script)
#
#	run that command to update udev rules :  sudo udevadm control --reload-rules
#
################################################################################################################

# CONFIGURATION
LOG_FILE=/var/log/usbhook
exec > >(tee -a ${LOG_FILE} )
exec 2> >(tee -a ${LOG_FILE} >&2)

# CONFIGURATION: Destination folder
DEST="/home/botserv/brain"

DEVICE="$1" # the device name

NUMBER="${DEVICE: -1}"


if [ "$NUMBER" = "1" ]
then
	exit 0
fi

mkdir /tmp/"$DEVICE"

# Mount ntfs usb drive
mount -t ntfs-3g /dev/"$DEVICE"1 /tmp/"$DEVICE"

cp -R /tmp/"$DEVICE"/*.rive "$DEST"/
chmod 777 -R "$DEST"/*

umount /tmp/"$DEVICE"
rm -r /tmp/"$DEVICE"

exit 0
