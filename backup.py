import os
import subprocess
from datetime import datetime

disk = '/mnt/baf22b98-c9d5-4b3e-941d-b9e64f70621d'
home = os.getenv('HOME')
include = os.path.join(home, '.rsync_include')
exclude = os.path.join(home, '.rsync_exclude')
logfile = os.path.join(disk, 'home/alexandr/backups/backups_log')
dest_dir = os.path.join(disk, "home/alexandr/backups")
time = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')


def is_mounted():
    if not os.path.exists('/media/alexandr/baf22b98-c9d5-4b3e-941d-b9e64f70621d'):
        subprocess.call([
            'udisksctl', 'mount', '-b', '/dev/sda3', '1>/dev/null'
        ])


def main():
    # is_mounted()

    try:
        os.remove(logfile)
    except FileNotFoundError:
        pass

    with open(include) as f:
        for i in f:
            i = i.strip()
            if not i.startswith('#') and i is not '':
                if i.startswith('.'):
                    subprocess.call([
                        'rsync', '-a', '--delete', f'--log-file={logfile}', f'{home}/{i}', f'{dest_dir}/latest'
                    ])
                else:
                    subprocess.call([
                        'rsync', '-a', '--delete', '--delete-excluded', f'--exclude-from={exclude}',
                        f'--log-file={logfile}', f'{home}/{i}', f'{dest_dir}/latest'
                    ])

    subprocess.call([
        'cp', '-a', '-l', f'{dest_dir}/latest', f'{dest_dir}/{time}'
    ])


if __name__ == '__main__':
    # print(logfile)
    # print(disk)
    # print(dest_dir)
    # print(exclude)

    main()
