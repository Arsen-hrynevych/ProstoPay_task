import os
from dotenv import load_dotenv

load_dotenv()


def get_env_variable(variable_name: str) -> str:
    """
    Retrieves the value of the specified environment variable.

    Args:
    - variable_name (str): The name of the environment variable to retrieve.

    Returns:
    - str: The value of the specified environment variable.

    Raises:
    - KeyError: If the specified environment variable is not set.
    """
    try:
        var_value = os.environ[variable_name]
        return var_value
    except KeyError:
        error_msg = {'error': f'Set the {variable_name} environment variable'}
        raise KeyError(error_msg)
