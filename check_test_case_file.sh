#!/usr/bin/env bash
# This script checks for test case file in epistemic project


set -eum  # bail if any step fails or any variable is not initialized

if [ $# -eq 0 ]
then
    echo "No directory passed for test case check" >&2
    exit 1
fi

echo "Running test file to find test case of python module"
for i in $(find $@)
do
	start_time="$(date -u +%s)"
    cat << CHECK_FOR_TEST_CASE_FILE
------------------------------------------------
BEGIN CHECK '$i'
------------------------------------------------
CHECK_FOR_TEST_CASE_FILE
    if [[ ($i != *'__init__.py') && ($i != *'.pyc') && ($i = *'.py') && ($i != *'-test.py') && ($i != *'__pycache__') ]]; then
        file_name=${i##*/}
        path=${i/${i##*/}/${file_name/.py/-test.py}}
        if [ -f $path ]; then
            echo "$path exists."
        else
            echo "$i has no test case file"
            exit 1
        fi
    fi     
    end_time="$(date -u +%s)"    
done

echo "Finished"