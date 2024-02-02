import click
from azure.storage.blob import BlobServiceClient
@click.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.argument('account_name')
@click.argument('account_key')
@click.argument('container_name')
def upload_to_azure(file_path, account_name, account_key, container_name):
    upload_file_to_azure(file_path, account_name, account_key, container_name)

if __name__ == '__main__':
    upload_to_azure()
