#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import dotenv

def main():
    """Run administrative tasks with enhanced environment handling."""
    dotenv.load_dotenv() 
    required_env_vars = ["DJANGO_SECRET_KEY"]
    missing_vars = [var for var in required_env_vars if not os.getenv(var)]

    if missing_vars:
        raise RuntimeError(f"Missing required environment variables: {', '.join(missing_vars)}. Check your .env file.")

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
