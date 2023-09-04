import logging

logging.basicConfig(
    level=logging.DEBUG,  # Уровень логгирования (может быть DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="config/logs/my_app.log",  # Имя файла, в который будет записываться лог
)
logger = logging.getLogger(__name__)

logger.debug("Это сообщение с уровнем DEBUG")
logger.info("Это информационное сообщение")
logger.warning("Это предупреждение")
logger.error("Это сообщение об ошибке")
logger.critical("Это критическое сообщение")

console_handler = logging.StreamHandler()
logger.addHandler(console_handler)
