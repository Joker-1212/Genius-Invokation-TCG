import Constant
from typing import NamedTuple


class Damage:
    """
    伤害类

    参数：
        dmg: 伤害值
        type: 伤害类型
    """

    def __init__(self, dmg: int, damage_type: int):
        """
        初始化伤害类
        参数：
            dmg: 伤害值
            damage_type: 伤害类型
        """
        self.dmg = dmg
        self.damage_type = damage_type


class ReactionType(NamedTuple):
    type1: int
    type2: int


def calculate_reaction_boost(dmg: Damage, reaction_type: ReactionType) -> Damage:
    """
    计算反应增幅

    参数：
        dmg: 伤害值
        reaction_type: 反应类型

    返回：
        增幅后的伤害值
    """
    if reaction_type in [(0, 1), (0, 3), (0, 5)]:
        dmg.dmg += 2
    else:
        dmg.dmg += 1
    return dmg
