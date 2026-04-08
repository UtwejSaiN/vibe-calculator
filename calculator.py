#!/usr/bin/env python3
"""
Vibe Calculator - A colorful terminal calculator
"""

import sys


class Colors:
    """ANSI color codes for terminal styling"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    PINK = '\033[95m'
    ORANGE = '\033[38;5;208m'


def print_banner():
    """Display cool ASCII banner"""
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔═══════════════════════════════════════╗
║                                       ║
║     ✨ VIBE CALCULATOR ✨            ║
║                                       ║
║     Where Math Meets Aesthetic        ║
║                                       ║
╚═══════════════════════════════════════╝
{Colors.END}
    """
    print(banner)


def print_menu():
    """Display operation menu"""
    menu = f"""
{Colors.YELLOW}Choose your operation:{Colors.END}

  {Colors.GREEN}[1]{Colors.END} ➕  Addition
  {Colors.BLUE}[2]{Colors.END} ➖  Subtraction
  {Colors.PINK}[3]{Colors.END} ✖️   Multiplication
  {Colors.ORANGE}[4]{Colors.END} ➗  Division
  {Colors.RED}[5]{Colors.END} 🚪  Exit

{Colors.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.END}
    """
    print(menu)


def get_number(prompt):
    """Get a number from user with error handling"""
    while True:
        try:
            value = input(f"{Colors.CYAN}{prompt}{Colors.END}")
            return float(value)
        except ValueError:
            print(f"{Colors.RED}❌ Invalid input! Please enter a number.{Colors.END}")
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}Exiting...{Colors.END}")
            sys.exit(0)


def add(x, y):
    """Addition"""
    result = x + y
    print(f"\n{Colors.GREEN}{Colors.BOLD}✨ Result: {x} + {y} = {result}{Colors.END}\n")
    return result


def subtract(x, y):
    """Subtraction"""
    result = x - y
    print(f"\n{Colors.BLUE}{Colors.BOLD}✨ Result: {x} - {y} = {result}{Colors.END}\n")
    return result


def multiply(x, y):
    """Multiplication"""
    result = x * y
    print(f"\n{Colors.PINK}{Colors.BOLD}✨ Result: {x} × {y} = {result}{Colors.END}\n")
    return result


def divide(x, y):
    """Division"""
    if y == 0:
        print(f"\n{Colors.RED}{Colors.BOLD}❌ Error: Cannot divide by zero!{Colors.END}\n")
        return None
    result = x / y
    print(f"\n{Colors.ORANGE}{Colors.BOLD}✨ Result: {x} ÷ {y} = {result}{Colors.END}\n")
    return result


def main():
    """Main calculator loop"""
    print_banner()

    while True:
        print_menu()

        try:
            choice = input(f"{Colors.BOLD}Enter choice (1-5): {Colors.END}")

            if choice == '5':
                print(f"\n{Colors.CYAN}{Colors.BOLD}👋 Thanks for vibing with us! Peace out! ✌️{Colors.END}\n")
                break

            if choice not in ['1', '2', '3', '4']:
                print(f"{Colors.RED}❌ Invalid choice! Please select 1-5.{Colors.END}\n")
                continue

            # Get numbers from user
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            # Perform calculation
            if choice == '1':
                add(num1, num2)
            elif choice == '2':
                subtract(num1, num2)
            elif choice == '3':
                multiply(num1, num2)
            elif choice == '4':
                divide(num1, num2)

            # Ask if user wants to continue
            input(f"{Colors.YELLOW}Press Enter to continue...{Colors.END}")
            print("\n" * 2)

        except KeyboardInterrupt:
            print(f"\n\n{Colors.CYAN}{Colors.BOLD}👋 Caught you trying to escape! Peace out! ✌️{Colors.END}\n")
            break
        except Exception as e:
            print(f"{Colors.RED}❌ An error occurred: {e}{Colors.END}\n")


if __name__ == "__main__":
    main()
