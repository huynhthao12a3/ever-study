from ..utils import GameConfig
from .entity import Entity


class Floor(Entity):
    def __init__(self, config: GameConfig) -> None:
        super().__init__(config, config.images.base, 0, config.window.vh)
        self.vel_x = 4
        self.x_extra = self.w - config.window.w

    def stop(self) -> None:
        self.vel_x = 0

    def draw(self) -> None:
        # print(self.x)
        # print(self.vel_x)
        # print(self.x_extra)
        self.x = -((-self.x + self.vel_x) % self.x_extra)
        super().draw()
