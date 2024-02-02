#!/bin/bash

# Azure Storage Account Information
account_name="your_storage_account_name"
account_key="your_storage_account_key"
container_name="your_container_name"

# File to Upload
file_path=$1

# Check if file_path is provided
if [ -z "$file_path" ]; then
  echo "Usage: $0 <file_path>"
  exit 1
fi

# Check if Azure CLI is installed
if ! command -v az &> /dev/null; then
    echo "Azure CLI is not installed. Please install it first."
    exit 1
fi

# Authenticate with Azure CLI
az login

# Upload the file to Azure Blob Storage
az storage blob upload \
  --account-name $account_name \
  --account-key $account_key \
  --container-name $container_name \
  --type block \
  --name $(basename $file_path) \
  --type block \
  --type block \
  --content-type "application/octet-stream" \
  --type block \
  --content-encoding "gzip" \
  --type block \
  --type block \
  --type block \
  --file $file_path

echo "File successfully uploaded to Azure Blob Storage."
