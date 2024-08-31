import logging
import os


class LoggerForDevOps:
    def __init__(self, path_logs: str) -> None:
        """
        Inicializa a instância do logger para uso em processos DevOps.

        Esta classe cria e configura um logger com nível de detalhamento definido para `DEBUG`.
        O logger pode ser utilizado para registrar eventos de depuração, warnings, erros e mensagens críticas durante a execução de scripts e automações.

        Args:
            path_logs (str): O caminho para o diretório onde os arquivos de log serão armazenados.
                             Deve ser um caminho válido no sistema de arquivos local.

        Atributos:
            logger (logging.Logger): Instância do logger configurada com o nome da classe.
            path_logs (str): Caminho especificado para armazenar os logs.
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)  # Global level is DEBUG, capturing all logs
        self.path_logs = path_logs
        self.logger.handlers = []

    def _get_file_handler(
        self, filename: str, formatter: logging.Formatter
    ) -> logging.FileHandler:
        """
        Cria e configura um `FileHandler` para registrar logs em um arquivo específico.

        Este método define um `FileHandler` que irá armazenar os logs em um arquivo com o nome fornecido,
        localizado no diretório de logs configurado. O arquivo será aberto no modo de escrita (`append`),
        com codificação UTF-8, e os registros serão formatados conforme o formatter passado.

        Args:
            filename (str): Nome do arquivo de log (`.log`) onde os registros serão armazenados.
            formatter (logging.Formatter): Instância de `Formatter` que define o formato dos logs que serão gravados no arquivo.

        Returns:
            logging.FileHandler: Um `FileHandler` configurado com o caminho do arquivo, o modo de escrita e o formato de log.
        """
        file_handler = logging.FileHandler(
            os.path.join(self.path_logs, filename), "a", "utf-8"
        )
        file_handler.setFormatter(formatter)
        return file_handler

    def logging_info(self, message: str) -> None:
        """
        Registra uma mensagem de nível INFO no console.

        Esta função cria um `StreamHandler` para exibir as mensagens no console com um formato específico.
        Antes de adicionar o handler, verifica se o logger já possui um `StreamHandler` para evitar duplicidade.

        Args:
            message (str): Mensagem a ser registrada no nível INFO.

        Comportamento:
            - A mensagem será formatada com o nível de log.
            - Se o `StreamHandler` ainda não tiver sido adicionado ao logger, ele será adicionado e a mensagem será registrada.
        """
        info_console_handler = logging.StreamHandler()  # Only StreamHandler for console
        formatter_info_message = logging.Formatter("{levelname} - {message}", style="{")
        info_console_handler.setFormatter(formatter_info_message)

        self.logger.handlers = [
            h for h in self.logger.handlers if not isinstance(h, logging.StreamHandler)
        ]
        self.logger.addHandler(info_console_handler)
        self.logger.info(message)

    def logging_debug(self, message: str) -> None:
        """
        Registra uma mensagem de nível DEBUG em um arquivo de log.

        Esta função utiliza um `FileHandler` para gravar as mensagens de depuração em um arquivo de log.
        O arquivo é nomeado como "debug_and_warning.log" e cada mensagem é formatada com o nível de log e o timestamp.

        Args:
            message (str): Mensagem a ser registrada no nível DEBUG.

        Comportamento:
            - A mensagem será formatada com o nível de log e a data/hora.
            - Se o `FileHandler` ainda não tiver sido adicionado ao logger, ele será adicionado e a mensagem será registrada.
        """
        formatter_debug_message = logging.Formatter(
            "{levelname} - {message} - {asctime}", style="{"
        )
        debug_file_handler = self._get_file_handler(
            "debug.log", formatter_debug_message
        )

        self.logger.handlers = [
            h for h in self.logger.handlers if not isinstance(h, logging.StreamHandler)
        ]
        self.logger.addHandler(debug_file_handler)
        self.logger.debug(message)

    def logging_warning(self, message: str) -> None:
        """
        Registra uma mensagem de nível WARNING em um arquivo de log.

        Esta função utiliza um `FileHandler` para gravar as mensagens de aviso em um arquivo de log.
        O arquivo é nomeado como "debug_and_warning.log" e as mensagens são formatadas com o nível de log, a mensagem e o timestamp.
        Inclui a exibição de informações de exceção.

        Args:
            message (str): Mensagem a ser registrada no nível WARNING.

        Comportamento:
            - A mensagem será formatada com o nível de log e a data/hora.
            - Se o `FileHandler` ainda não tiver sido adicionado ao logger, ele será adicionado e a mensagem será registrada.
            - Informações de exceção (`exc_info=True`) serão incluídas no log.
        """
        formatter_warning_message = logging.Formatter(
            "{levelname} - {message} - {asctime}", style="{"
        )
        warning_file_handler = self._get_file_handler(
            "warning.log", formatter_warning_message
        )

        self.logger.handlers = [
            h for h in self.logger.handlers if not isinstance(h, logging.StreamHandler)
        ]
        self.logger.addHandler(warning_file_handler)
        self.logger.warning(message)

    def logging_error(self, message: str) -> None:
        """
        Registra uma mensagem de nível ERROR em um arquivo de log.

        Esta função utiliza um `FileHandler` para gravar as mensagens de erro em um arquivo de log.
        O arquivo é nomeado como "error_and_critical.log" e as mensagens são formatadas com o nível de log,
        a mensagem e o timestamp. Também inclui informações sobre a exceção e a pilha de execução.

        Args:
            message (str): Mensagem a ser registrada no nível ERROR.
            
        Comportamento:
            - A mensagem será formatada com o nível de log e a data/hora.
            - Se o `FileHandler` ainda não tiver sido adicionado ao logger, ele será adicionado e a mensagem será registrada.
            - Informações de exceção (`exc_info=True`) e da pilha de execução (`stack_info=True`) serão incluídas no log.
        """
        formatter_error_message = logging.Formatter(
            "{levelname} - {message} - {asctime}", style="{"
        )
        error_file_handler = self._get_file_handler(
            "error.log", formatter_error_message
        )

        self.logger.handlers = [
            h for h in self.logger.handlers if not isinstance(h, logging.StreamHandler)
        ]
        self.logger.addHandler(error_file_handler)
        self.logger.error(message, exc_info=True, stack_info=True)

    def logging_critical(self, message: str) -> None:
        """
        Registra uma mensagem de nível CRITICAL em um arquivo de log.

        Esta função utiliza um `FileHandler` para gravar as mensagens críticas em um arquivo de log.
        O arquivo é nomeado como "error_and_critical.log" e as mensagens são formatadas com o nível de log,
        a mensagem e o timestamp. Informações sobre exceção e a pilha de execução também são incluídas.

        Args:
            message (str): Mensagem a ser registrada no nível CRITICAL.

        Comportamento:
            - A mensagem será formatada com o nível de log e a data/hora.
            - Se o `FileHandler` ainda não tiver sido adicionado ao logger, ele será adicionado e a mensagem será registrada.
            - Informações de exceção (`exc_info=True`) e da pilha de execução (`stack_info=True`) serão incluídas no log.
        """
        formatter_critical_message = logging.Formatter(
            "{levelname} - {message} - {asctime}", style="{"
        )
        critical_file_handler = self._get_file_handler(
            "critical.log", formatter_critical_message
        )

        self.logger.handlers = [
            h for h in self.logger.handlers if not isinstance(h, logging.StreamHandler)
        ]
        self.logger.addHandler(critical_file_handler)
        self.logger.critical(message, exc_info=True, stack_info=True)
