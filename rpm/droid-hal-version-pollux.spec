# rpm_device is the name of the ported device
%define rpm_device pollux
# rpm_vendor is used in the rpm space
%define rpm_vendor sony

# Manufacturer and device name to be shown in UI
%define vendor_pretty Sony
%define device_pretty Xperia Tablet Z

# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator 0
%define have_led 0

%include droid-hal-version/droid-hal-version.inc
