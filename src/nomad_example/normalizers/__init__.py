from pydantic import Field
from nomad.config.models.plugins import NormalizerEntryPoint


class MyNormalizerEntryPoint(NormalizerEntryPoint):
    parameter: int = Field(0, description='Config parameter for this plugin.')

    def load(self):
        from nomad_example.normalizers.mynormalizer import MyNormalizer

        return MyNormalizer(**self.dict())


mynormalizer = MyNormalizerEntryPoint(
    name='MyNormalizer',
    description='Normalizer defined using the new plugin mechanism.',
)