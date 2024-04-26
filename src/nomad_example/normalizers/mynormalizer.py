from nomad.config import config
from nomad.normalizing.normalizer import Normalizer

configuration = config.get_plugin_entry_point('nomad_example.normalizers:mynormalizer')


class MyNormalizer(Normalizer):
    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        logger.info(f'MyNormalizer.normalize: parameter={configuration.parameter}')