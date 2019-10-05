import os


def main(device='/dev/sda3'):
    command = f'udisksctl  mount -b {device}'
    os.system(command)


if __name__ == '__main__':
    main()
