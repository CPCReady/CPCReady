#!/bin/bash

# Allowed values for the emulator parameter
emulators=("m4" "rvm")

# Function to check if a value is in a list
isEmulator() {
    local value="$1"
    shift
    for element; do
        [[ "$element" == "$value" ]] && return 0
    done
    return 1
}

# Default values
emulator="m4"
dsk=""

# Process command line options
while [[ "$#" -gt 0 ]]; do
    case "$1" in
        -v|--version)
            show_version
            ready
            exit 0
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        -e|--emulator)
            if [[ -z "$2" ]]; then
                echo "ERROR: Missing argument for option $1" >&2
                exit 1
            fi
            if ! isEmulator "$2" "${emulators[@]}"; then
                echo "ERROR: The emulator value must be one of ${emulators[*]}" >&2
                exit 1
            fi
            emulator="$2"
            shift 2
            ;;
        -d|--dsk)
            if [[ -z "$2" ]]; then
                echo "ERROR: Missing argument for option $1" >&2
                exit 1
            fi
            dsk="$2"
            shift 2
            ;;
        *) echo "Invalid option: $1" >&2; exit 1 ;;
    esac
done

# Show option values
echo "Value of -e: $emulator"
echo "Value of -d: $dsk"
