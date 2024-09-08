import logging
import os

# Логирование для модуля masks
masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)

# Получаем путь к корневой директории проекта
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Создаем директорию logs в папке data
logs_dir = os.path.join(project_dir, "logs")
os.makedirs(logs_dir, exist_ok=True)

# Создаем обработчик файлов для masks
masks_file_handler = logging.FileHandler(os.path.join(logs_dir, "masks.log"), mode="w")

masks_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
masks_file_handler.setFormatter(masks_formatter)

masks_logger.addHandler(masks_file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.

    Args:
        card_number: Номер карты.

    Returns:
        Маскированный номер карты в формате XXXX XX** **** XXXX.
    """

    masks_logger.debug(f"Получен номер карты: {card_number}")

    if len(card_number) != 16:
        masks_logger.error("Номер карты должен быть 16-значным.")
        raise ValueError("Номер карты должен быть 16-значным.")

    masked_card_number = card_number[:4] + " " + card_number[4:6] + "**" + " " + "*" * 4 + " " + card_number[-4:]
    masks_logger.info(f"Маскированный номер карты: {masked_card_number}")
    return masked_card_number


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.

    Args:
        account_number: Номер счета.

    Returns:
        Маскированный номер счета в формате **XXXX.
    """

    masks_logger.debug(f"Получен номер счета: {account_number}")

    if len(account_number) < 6:
        masks_logger.error("Номер счета должен быть минимум 6-значным.")
        raise ValueError("Номер счета должен быть минимум 6-значным.")

    masked_account = "**" + account_number[-4:]
    masks_logger.info(f"Маскированный номер счета: {masked_account}")
    return masked_account


card_number = "1234567890123456"
print(get_mask_card_number(card_number))
