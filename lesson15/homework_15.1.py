"""
Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:

сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:

Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод setattr.

"""


class Rhombus:
    def __init__(self, side_a, angle_a):

        if side_a <= 0:
            raise ValueError("The length of side should be greate than 0.")

        if not (0 < angle_a < 180):
            raise ValueError("Angle should be less then 180 and greater than 0.")

        setattr(self, 'side_a', side_a)
        setattr(self, 'angle_a', angle_a)
        setattr(self, 'angle_b', 180 - angle_a)

    def get_info(self):
        return (f"Ромб зі стороною: {self.side_a} і кутами: {self.angle_a}° і {self.angle_b}°")


romb = Rhombus(10, 60)
print(romb.get_info())

