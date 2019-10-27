from ...utils.utils import utc


class Block:
    def __init__(self, *args, **kwargs):
        self.time_started = f"{utc()}"

    def calculate_block_hash(self):
        pass

