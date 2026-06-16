import secrets
import string
import argparse

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description='Secure Random Password Generator')
    parser.add_argument('-l', '--length', type=int, default=12, help='Password length (default: 12)')
    parser.add_argument('--no-upper', action='store_false', dest='upper', help='Exclude uppercase letters')
    parser.add_argument('--no-digits', action='store_false', dest='digits', help='Exclude digits')
    parser.add_argument('--no-symbols', action='store_false', dest='symbols', help='Exclude symbols')
    parser.add_argument('-c', '--count', type=int, default=1, help='Number of passwords to generate')
    args = parser.parse_args()

    print(f"\nGenerating {args.count} password(s) of length {args.length}...\n")
    for i in range(args.count):
        pwd = generate_password(args.length, args.upper, args.digits, args.symbols)
        print(f"  Password {i+1}: {pwd}")
    print()

if __name__ == '__main__':
    main()