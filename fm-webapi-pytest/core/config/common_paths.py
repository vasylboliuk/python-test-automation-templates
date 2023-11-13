import os


class CommonPaths:

    project_root = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                os.path.pardir,
                                                os.path.pardir))
    configs_path = os.path.join(project_root, "configurations")
    environment_path = os.path.join(configs_path, "environment")

    def list_environment_names(self):
        return [os.path.basename(folder) for folder in self._get_sub_folders(self.environment_path)]

    def _get_sub_folders(self, folder):
        subfolders = []
        try:
            dirs = os.listdir(folder)
            for item in dirs:
                item_path = os.path.join(folder, item)
                if os.path.isdir(item_path):
                    subfolders.append(item_path)
                    subfolders.extend(self._get_sub_folders(item_path))
            return subfolders
        except FileNotFoundError:
            return []
