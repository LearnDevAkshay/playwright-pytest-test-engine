import  os
import json

def read_config():
    project_root = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(project_root, "data", "config.json")

    with open(config_path, "r") as f:
        config = json.load(f)

    env = config.get("environment")
    browser = config.get("browser")
    logging = config.get("logging")
    headless_mode = config.get("headless_mode")
    if env not in config:
        raise ValueError(f"Environment '{env}' not found in {config_path}")

    env_config = config[env]
    return env, browser, logging, headless_mode, env_config["url"], env_config["email"], env_config["password"]