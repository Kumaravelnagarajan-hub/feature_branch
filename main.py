"""
Main application entry point.
"""
from utils import greet, add_numbers
from logger import setup_logger
from config import APP_NAME, DEBUG_MODE

logger = setup_logger(__name__)

def main():
    """Main function to run the application."""
    logger.info(f"Starting {APP_NAME}")
    
    # Example function calls
    greeting = greet("Python Developer")
    logger.info(greeting)
    
    result = add_numbers(10, 20)
    logger.info(f"Sum of 10 and 20 is: {result}")
    
    logger.info(f"Debug mode: {DEBUG_MODE}")
    logger.info(f"{APP_NAME} completed successfully")

if __name__ == "__main__":
    main()