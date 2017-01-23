from up.registrar import UpRegistrar


class Registrar(UpRegistrar):
    def __init__(self):
        super().__init__('mission_control_cog')

    def register(self):
        external_modules = self._load_external_modules()
        if external_modules is not None:
            self._register_module('MissionControlProvider', 'mission_control_cog.modules.mission_control_module')
            self._write_external_modules()
        return True
