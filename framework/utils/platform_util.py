import platform


class PlatformUtil:
    @staticmethod
    def get_system_name():
        return platform.system()
