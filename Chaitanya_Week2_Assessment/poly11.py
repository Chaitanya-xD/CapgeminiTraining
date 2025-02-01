"""
Create a class `Logger` with a method `log(message)`. Implement method overloading to log different message types (`error`, `warning`, `info`).

"""

class Logger:
    logs = []

    def log(self, message="This is an error message.", type="[ERROR]"):
        self.logs.append(f"{type}: {message}")

def main():
    logger = Logger()

    # Log with default error message
    logger.log()

    # Log with a custom message (defaults to [INFO])
    logger.log("This is an info message", "[INFO]")

    # Log with a custom message and type
    logger.log("This is a warning message", "[WARNING]")

    logger.log()
    
    # Print all logs
    for log in logger.logs:
        print(log)

main()