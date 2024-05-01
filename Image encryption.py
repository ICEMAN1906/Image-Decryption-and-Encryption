"""
Author:Aaron Brown
4/20/2024
 Encrypt encrypted pictures
"""
def encrypt_image(path, key):
    try:
        # Print path of image file and encryption key
        print('The path of file:', path)
        print('Key for encryption:', key)

        # Open file for reading purpose
        with open(path, 'rb') as fin:
            # Store image data in variable "image"
            image = bytearray(fin.read())

        # Perform XOR operation on each value of bytearray
        for index, value in enumerate(image):
            image[index] = value ^ key

        # Open file for writing purpose
        with open(path, 'wb') as fout:
            # Write encrypted data to image
            fout.write(image)

        print('Encryption Done...')

    except FileNotFoundError:
        print('Error: File not found')
    except PermissionError:
        print('Error: Permission denied to access the file')
    except Exception as e:
        print(f'Error caught: {type(e).__name__}')


if __name__ == "__main__":
    try:
        # Take path of image and encryption key as input
        path = input(r'Enter path of Image: ')
        key = int(input('Enter Key for encryption of Image: '))

        encrypt_image(path, key)

    except ValueError:
        print('Error: Key must be an integer')
    except KeyboardInterrupt:
        print('Encryption process interrupted by user')


def decrypt_image(path, key):
    try:
        # Print path of image file and decryption key
        print('The path of file:', path)
        print('provide the same Encryption and Decryption key.')
        print('Key for Decryption:', key)

        # Open file for reading purpose
        with open(path, 'rb') as fin:
            # Store image data in variable "image"
            image = bytearray(fin.read())

        # Perform XOR operation on each value of bytearray for decryption
        for index, value in enumerate(image):
            image[index] = value ^ key

        # Open file for writing purpose
        with open(path, 'wb') as fout:
            # Write decrypted data to image
            fout.write(image)

        print('Decryption Done...')

    except FileNotFoundError:
        print('Error: File not found')
    except PermissionError:
        print('Error: Permission denied to access the file')
    except ValueError:
        print('Error: Key must be an integer')
    except Exception as e:
        print(f'Error caught: {type(e).__name__}')


if __name__ == "__main__":
    try:
        # Take path of image and decryption key as input
        path = input(r'Enter path of Image: ')
        key = int(input('Enter Key for decryption of Image: '))

        decrypt_image(path, key)

    except KeyboardInterrupt:
        print('Decryption process interrupted by user')
