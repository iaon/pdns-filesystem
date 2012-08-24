from os import environ
import sys

from .backend import Backend
from .frontend import PdnsFrontend


def exit_with_error(error):
    sys.stderr.write(error)
    sys.exit(1)

def get_filesystem_connection(params):
    region = params['--region']
    access_key, secret_key = get_aws_credentials(params)
    if not (access_key and secret_key):
        exit_with_error('ERROR: Invalid AWS credentials supplied.')
    connection = connect_to_region(region,
                                   aws_access_key_id=access_key,
                                   aws_secret_access_key=secret_key)
    if not connection:
        exit_with_error('ERROR: unable to connect, check your region')

    return connection

def run(params):
    connection = get_filesystem_connection(params)
    backend = Backend(connection=connection, table_name=params['--table'])
    frontend = PdnsFrontend(sys.stdin, sys.stdout, backend)
    frontend.expect_helo()
    frontend.run()
