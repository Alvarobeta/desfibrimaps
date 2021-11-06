from thelibrary_core.infrastructure.context_base import ContextBase


class SharedContext(ContextBase):

    def _path(self) -> str:
        return 'thelibrary_core/context/shared'
