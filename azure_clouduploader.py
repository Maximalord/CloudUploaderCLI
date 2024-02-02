#Import Necessary Libraries
import click
from azure.storage.blob import BlobServiceClient

#Set Up CLI Structure
@click.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.argument('account_name')
@click.argument('account_key')
@click.argument('container_name')
def upload_to_azure(file_path, account_name, account_key, container_name):
    upload_file_to_azure(file_path, account_name, account_key, container_name)

if __name__ == '__main__':
    upload_to_azure()

#File Upload Function
def upload_file_to_azure(file_path, account_name, account_key, container_name):
    connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_path)

    try:
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)
        print(f'Successfully uploaded {file_path} to {container_name}')
    except Exception as e:
        print(f'Error uploading {file_path} to {container_name}: {e}')
