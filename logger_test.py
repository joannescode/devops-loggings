from library.logger import LoggerForDevOps
import requests

folder_logs = "logs"
loggers = LoggerForDevOps(path_logs=folder_logs)

url_dict = {
    "404": "https://httpbin.org/status/404",
    "500": "https://httpbin.org/status/500",
    "403": "https://httpbin.org/status/403",
    "400": "https://httpbin.org/status/400",
    "200": "https://github.com/joannescode",
}

try:
    for _, address in url_dict.items():
        session = requests.Session()
        r = session.get(url=address, timeout=10)

        if r.status_code == 200:
            loggers.logging_info(
                message=f"Successful connection to {address} with status code {r.status_code}."
            )
        elif r.status_code == 404:
            loggers.logging_warning(
                message=f"Warning: Resource not found at {address}. Status code: {r.status_code}."
            )
        elif r.status_code == 500:
            loggers.logging_warning(
                message=f"Server error at {address}. Status code: {r.status_code}."
            )
        elif r.status_code == 403:
            loggers.logging_error(
                message=f"Access denied at {address}. Status code: {r.status_code}.",
            )
        elif r.status_code == 400:
            loggers.logging_critical(
                message=f"Bad request to {address}. Status code: {r.status_code}."
            )

except TimeoutError as te:
    loggers.logging_error(
        message=f"TimeoutError: Connection timed out for {address}.", exc_info=True
    )

except ConnectionError as ce:
    loggers.logging_critical(
        message=f"ConnectionError: Failed to connect to {address}. Verify if the URL is correct.",
        exc_info=True,
    )

finally:
    if session:
        session.close()
