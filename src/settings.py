from pathlib import Path
import yaml


__all__ = ('load_config',)


def load_config(config_file=None):
    default_config = Path(__file__).parent / 'config.yaml'
    config = {}
    cf_dict = {}

    with open(default_config, 'r') as f:
        config = yaml.safe_load(f)

    if config_file:
        cf_dict = yaml.safe_load(config_file)

    config.update(**cf_dict)

    return config
