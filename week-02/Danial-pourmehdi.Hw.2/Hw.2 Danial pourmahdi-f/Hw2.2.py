import json


class ConfigError(Exception):
    pass


class InvalidConfigError(ConfigError):
    pass


def main():
    try:
        config = {
            "api_key": "my_secret_key_123",
            "database_url": "postgresql://user:pass@localhost:5432/mydb",
            "mode": "debug"
        }

        required_keys = ['api_key', 'database_url', 'mode']
        for key in required_keys:
            if key not in config:
                raise InvalidConfigError(f"invalid config error {key}")

        valid_modes = ['debug', 'production']
        if config['mode'] not in valid_modes:
            raise InvalidConfigError(f"invalid mode: {valid_modes}")

        print("loaded succeessfully!")
        for key, value in config.items():
            print(f"  {key}: {value}")

    except InvalidConfigError as e:
        print(f"Config Error: {e}")
    except Exception as e:
        print(f"unexpected error: {e}")

main()

