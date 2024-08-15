import sys

from sample_factory.enjoy import enjoy
from train_custom_env import parse_args, register_custom_env_envs


def main():
    """Script entry point."""
    register_custom_env_envs()
    cfg = parse_args(evaluation=True)
    status = enjoy(cfg)
    return status


if __name__ == "__main__":
    sys.exit(main())