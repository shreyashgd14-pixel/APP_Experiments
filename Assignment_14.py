import logging

logging.basicConfig(
    filename="app.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
    level=logging.DEBUG
)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

name = "Samara"
logging.debug(f"{name=}")

donuts = 5
guests = 0
try:
    donuts_per_guest = donuts / guests
except ZeroDivisionError:
    logging.exception("DonutCalculationError")
