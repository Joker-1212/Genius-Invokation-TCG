FACTION = [
    "Mondstadt",  #     0 蒙德
    "Liyue",  #         1 璃月
    "Inazuma",  #       2 稻妻
    "Sumeru",  #        3 须弥
    "Fontaine",  #      4 枫丹
    "Natlan",  #        5 纳塔
    "Fatui",  #         6 愚人众
    "Hilichurl",  #     7 丘丘人
    "The Eremites",  #  8 镀金旅团
    "Monster",  #       9 魔物
]  # 阵营
ELEMENTS = [
    "Pyro",  #              0 火
    "Hydro",  #             1 水
    "Anemo",  #             2 风
    "Electro",  #           3 雷
    "Dendro",  #            4 草
    "Cryo",  #              5 冰
    "Geo",  #               6 岩
    "No Elemental Type",  # 7 物理
    "Piercing",  #          8 穿透伤害
]  # 元素类型
WEAPONS = [
    "Sword",  #         0 单手剑
    "Claymore",  #      1 双手剑
    "Bow",  #           2 弓
    "Catalyst",  #      3 法器
    "Polearm",  #       4 长柄武器
    "Other Weapons",  # 5 其他武器
]  # 武器类型
REACTION = {
    (0, 1): "Vaporize",  # 蒸发
    (0, 2): "Pyro Swirl",  # 扩散(火)
    (0, 3): "Overloaded",  # 超载
    (0, 4): "Burning",  # 燃烧
    (0, 5): "Melt",  # 融化
    (0, 6): "Crystallize",  # 结晶
    (1, 2): "Hydro Swirl",  # 扩散(水)
    (1, 3): "Electro Charged",  # 感电
    (1, 4): "Bloom",  # 绽放
    (1, 5): "Frozen",  # 冻结
    (1, 6): "Crystallize",  # 结晶
    (2, 3): "Electro Swirl",  # 扩散(雷)
    (2, 5): "Cyro Swirl",  # 扩散(冰)
    (3, 4): "Quicken",  # 激化
    (3, 5): "Superconduct",  # 超导
    (3, 6): "Crystallize",  # 结晶
    (5, 6): "Crystallize",  # 结晶
}  # 元素反应
BUFFTYPE = [
    "Damage Boost",  #           0 增伤
    "Damage Reduce",  #          1 减伤/虚弱
    "Shield",  #                 2 护盾
    "Damage Resistance",  #      3 抗伤
    "Damage Susceptibility",  #  4 易伤
]
DURATION_TYPE = ["Time", "Round"]  # 0 次数 1 回合数
