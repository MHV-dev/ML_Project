# src/exception.py

import sys
import logging


def error_message_detail(error: Exception) -> str:
    exc_type, exc_value, exc_tb = sys.exc_info()
    if exc_tb is not None and exc_tb.tb_frame is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return f"Error occurred in script: {file_name} at line {line_number} | Error message: {str(error)}"
    else:
        return f"Error message: {str(error)}"

class CustomException(Exception):
    def __init__(self, error_message: Exception):
        self.error_message = error_message_detail(error_message)
        super().__init__(error_message)

    def __str__(self):
        return self.error_message

# Testing block
if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divided by zero")
        raise CustomException(e)
