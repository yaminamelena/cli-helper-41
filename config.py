from typing import Dict, Any

class Config:
    """Class to handle application configuration."""
    def __init__(self, settings: Dict[str, Any]) -> None:
        """Initialize configuration with provided settings.

        Args:
            settings (Dict[str, Any]): A dictionary containing configuration settings.
        """
        self.settings = settings

    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value by key.

        Args:
            key (str): The configuration key to retrieve.
            default (Any, optional): Default value if the key is not found. Default is None.

        Returns:
            Any: The configuration value or default if not found.
        """
        return self.settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Set a configuration value by key.

        Args:
            key (str): The configuration key to set.
            value (Any): The value to set for the key.
        """
        self.settings[key] = value

    def all(self) -> Dict[str, Any]:
        """Return all configuration settings.

        Returns:
            Dict[str, Any]: A dictionary of all configuration settings.
        """
        return self.settings