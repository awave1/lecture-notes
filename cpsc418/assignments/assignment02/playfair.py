class Playfair():
    def __init__(self, key='ABCDEFGHIKLMNOPQRSTUVWXYZ'):
        self.key = [k.upper() for k in key]

    def encrypt(self, string):
        string = self._prepare_string()

        return ''

    def decrypt(self):
        pass

    
    def _prepare_string(self, string):
        return string.replace


def main():
    cipher = Playfair('keyword')
    message = 'secret message'
    print(cipher.encrypt(message))


if __name__ == '__main__':
    main()
