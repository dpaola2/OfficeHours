#!/usr/bin/env python
from migrate.versioning.shell import main
import os


if __name__ == '__main__':
    main(url=os.environ.get('DATABASE_URL'), repository='migrations', debug='False')
