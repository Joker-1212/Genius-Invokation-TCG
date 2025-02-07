import Function
import Constant


class Buff:
    """
    角色身上的buff

    参数：
        name: buff 名称
        duration: 持续时长
        lean: buff 倾向 (`True` 表示正面 buff, `Flase` 表示负面 buff)
        type: buff 类型
        countdown_type: 倒计时类型
    """

    def __init__(
        self, name: str, duration: int, lean: bool, type: int, countdown_type: int
    ) -> None:
        """
        初始化 Buff 对象

        参数：
            name: buff 名称
            duration: 持续时长
            lean: buff 倾向 (`True` 表示正面 buff, `False` 表示负面 buff)
            type: buff 类型
            countdown_type: 倒计时类型
        """
        self.name = name
        self.duration = duration
        self.lean = lean
        self.type = type
        self.countdown_type = countdown_type

    def effect(self, dmg: Function.Damage, lean: bool) -> Function.Damage:
        """
        影响伤害

        参数：
            dmg: 要作用的伤害
            lean: buff作用倾向, `Ture` 为攻击方，`False` 为被攻击方
        """
        pass

    def countdown(self) -> None:
        """
        使持续时间减一
        """
        self.duration -= 1
