from core.config.common_paths import CommonPaths
from core.utils.environment_loader import EnvLoader


def pytest_runtest_setup(item):
    print("pytest_runtest_setup")


def pytest_addoption(parser):
    parser.addoption("--execution_env", action="store", default="qa", help="Please provide execution Environment")


def pytest_configure(config):
    env = config.getoption("execution_env")
    if env is None:
        env = 'qa'
    envs = CommonPaths().list_environment_names()
    if env is not None and env not in envs:
        raise ValueError(f"Environment name is not valid. Please choose from: {envs}")
    EnvLoader(env)