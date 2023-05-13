#!/usr/bin/env bash

DATE=$(date '+%Y-%m-%d')
read -p "Enter the subject in lower-kebab-case: " SUBJECT

CREATED_MESSAGE=$(hugo new --kind adr 09_architecture-decisions/${DATE}_${SUBJECT})
CREATED_DIR=$(echo ${CREATED_MESSAGE} | cut -d ' ' -f1)

sed -i 's/YYYY-MM-DD/'${DATE}'/g' "${CREATED_DIR}/index.md"

echo ${CREATED_MESSAGE}
