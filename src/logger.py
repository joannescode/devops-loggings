import logging
import os


class LoggerForDevOps:
    def __init__(self, path_logs) -> None:
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.path_logs = path_logs

    def not_has_handlers(self, console=None, file=None):
        if console and not any(
            isinstance(h, logging.StreamHandler) for h in self.logger.handlers
        ):
            self.logger.addHandler(console)
        if file and not any(
            isinstance(h, logging.FileHandler) for h in self.logger.handlers
        ):
            self.logger.addHandler(file)

    def get_file_handler(self, filename, formatter):
        file_handler = logging.FileHandler(
            os.path.join(self.path_logs, filename), "a", "utf-8"
        )
        file_handler.setFormatter(formatter)
        return file_handler

    def logging_info(self, message):
        info_console_handler = logging.StreamHandler()
        formatter_info_message = logging.Formatter("{levelname} - {message}", style="{")
        info_console_handler.setFormatter(formatter_info_message)

        self.not_has_handlers(console=info_console_handler)
        self.logger.info(message)

    def logging_debug(self, message):
        formatter_debug_message = logging.Formatter(
            "{levelname} - {message} - {asctime}", style="{"
        )
        debug_file_handler = self.get_file_handler(
            "debug_and_warning.log", formatter_debug_message
        )

        self.not_has_handlers(file=debug_file_handler)
        self.logger.debug(message)

    def logging_warning(self, message):
        formatter_warning_message = logging.Formatter(
            "{levelname} - {message} - {asctime}", style="{"
        )
        warning_file_handler = self.get_file_handler(
            "debug_and_warning.log", formatter_warning_message
        )

        self.not_has_handlers(file=warning_file_handler)
        self.logger.warning(message, exc_info=True)

    def logging_error(self, message, exc_info=True):
        formatter_error_message = logging.Formatter(
            "{levelname} - {message} - {asctime}", style="{"
        )
        error_file_handler = self.get_file_handler(
            "error_and_critical.log", formatter_error_message
        )

        self.not_has_handlers(file=error_file_handler)
        self.logger.error(message, exc_info=exc_info, stack_info=True)

    def logging_critical(self, message):
        formatter_critical_message = logging.Formatter(
            "{levelname} - {message} - {asctime}", style="{"
        )
        critical_file_handler = self.get_file_handler(
            "error_and_critical.log", formatter_critical_message
        )

        self.not_has_handlers(file=critical_file_handler)
        self.logger.critical(message, exc_info=True, stack_info=True)
