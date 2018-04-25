#!/usr/bin/python

"""Gets a bunch of info about the current machine"""

import plistlib
import subprocess


def hardware_info():
    '''Returns system_profiler hardware info as a dictionary'''
    cmd = ['/usr/sbin/system_profiler', 'SPHardwareDataType', '-xml']
    output = subprocess.check_output(cmd)

    info = plistlib.readPlistFromString(output)

    hardware_info = info[0]['_items'][0]
    return hardware_info

def storage_info():
    '''Returns system_profiler storage info as a dictionary'''
    cmd = ['/usr/sbin/system_profiler', 'SPStorageDataType', '-xml']
    output = subprocess.check_output(cmd)

    info = plistlib.readPlistFromString(output)

    storage_info = info[0]['_items'][0]
    return storage_info
    
def software_info():
    '''Returns system_profiler software info as a dictionary'''
    cmd = ['/usr/sbin/system_profiler', 'SPSoftwareDataType', '-xml']
    output = subprocess.check_output(cmd)

    info = plistlib.readPlistFromString(output)

    software_info = info[0]['_items'][0]
    return software_info    

def main():
    hw_info = hardware_info()
    processor = hw_info['cpu_type'] + ' ' + hw_info['current_processor_speed']
    disk_info = storage_info()
    os_info = software_info()
    info = {}
    info['Host name'] = os_info['local_host_name']
    info['Serial number'] = hw_info['serial_number']
    info['Machine model'] = hw_info['machine_model']
    info['Processor'] = processor
    info['Memory'] = hw_info['physical_memory']
    info['Users'] = 'Not yet implemented'
    info['Disk size (GB)'] = disk_info['size_in_bytes'] / 1000000000
    info['Disk free space (GB)'] = disk_info['free_space_in_bytes'] / 1000000000
    info['OS version'] = os_info['os_version']

    for key, value in info.items():
        print '%s: %s' % (key, value)


if __name__ == "__main__":
    main()
