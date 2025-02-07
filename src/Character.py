import Constant
import Function
import Buff


class _Character:
    """
    角色父类

    参数：
        name: 角色名称
        element: 元素类型
        weapon: 武器类型
        charge_request: 大招充能需求
        faction: 所属阵营
        hp: 当前血量
        max_hp: 最大血量
    """

    def __init__(
        self,
        name: str,
        element: int,
        weapon: int,
        charge_request: int,
        faction: int,
        max_hp: int,
    ) -> None:
        """初始化一个新的角色用于《七圣召唤》卡牌游戏。

        参数:
            name (str): 角色的名字。
            element (int): 角色的元素类型 (0-6)。
            weapon (int): 角色的武器类型。
            charge_request (int): 角色的充能需求值。
            faction (int): 角色所属的阵营。
            max_hp (int): 角色的最大生命值。
        属性:
            name (str): 角色的名字。
            element (int): 角色的元素类型。
            weapon (str): 角色的武器类型。
            charge_request (int): 角色的充能需求值。
            faction (str): 角色所属的阵营。
            hp (int): 角色当前的生命值。
            max_hp (int): 角色的最大生命值。
            charge (int): 角色当前的充能值。
            normal_atk_cost (tuple): 普通攻击的费用。
            buff (list): 角色身上应用的增益效果列表。
            debuff (list): 角色身上应用的减益效果列表。
            alive (bool): 角色是否存活。
            active (bool): 角色当前是否处于激活状态。
        """
        self.name = name
        self.element = element
        self.weapon = weapon
        self.charge_request = charge_request
        self.faction = faction
        self.hp = self.max_hp = max_hp
        self.charge = 0
        self.normal_atk_cost = (2,) + tuple(1 if i == element else 0 for i in range(7))
        self.buff = []
        self.debuff = []
        self.alive = True
        self.active = False

    def normal_attack(self) -> Function.Damage:
        """
        普通攻击
        """
        pass

    def element_skill(self) -> Function.Damage:
        """
        元素战技
        """
        pass

    def element_brust(self) -> Function.Damage:
        """
        元素爆发
        """
        pass

    def dmg_out(self, dmg: Function.Damage) -> None:
        """
        造成伤害结算

        参数：
            dmg: 伤害值
        """
        for buff in self.buff:
            dmg = buff.effect(dmg, True)
        for debuff in self.debuff:
            dmg = debuff.effect(dmg, True)

    def dmg_in(self, dmg: Function.Damage):
        """
        接受伤害结算

        参数：
            dmg: 伤害值
        """
        for buff in self.buff:
            dmg = buff.effect(dmg, False)
        for debuff in self.debuff:
            dmg = debuff.effect(dmg, False)
        self.hp -= dmg.dmg
        if self.hp <= 0:
            self.alive = False

    def ending_phase(self) -> None:
        """
        结束阶段结算
        """
        for buff in self.buff:
            if buff.countdown_type == 1:
                buff.countdown()
            if buff.duration == 0:
                self.buff.remove(buff)
        for debuff in self.debuff:
            if debuff.countdown_type == 1:
                debuff.countdown()
            if debuff.duration == 0:
                self.debuff.remove(debuff)


class _MeleeCharacter(_Character):
    """
    近战角色
    """

    def normal_attack(self):
        if self.charge < self.charge_request:
            self.charge += 1
        return Function.Damage(dmg=2, type=7)


class _CatalystCharacter(_Character):
    """
    法器角色
    """

    def normal_attack(self):
        if self.charge < self.charge_request:
            self.charge += 1
        return Function.Damage(dmg=1, type=self.element)
