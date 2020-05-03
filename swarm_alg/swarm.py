import numpy as np
from swarm_alg.element import Element
from random import random


class Swarm():
    def __init__(
            self,
            fitness_func,
            swarm_size,
            dimension,
            min_border,
            max_border,
            iter_amount,
            stop_condition,
            p_coef=random(),  # Коэффициент влияния локальной лучшей точки
            g_coef=random(),  # Коэффициент влияния глобальной лучшей точки
    ):
        self.fitness_func = fitness_func
        self.b_swarm_pos = np.random.rand(dimension) \
                        * (max_border - min_border) + min_border
        self.b_swarm_val = float("inf")
        self.swarm_size = swarm_size
        self.swarm = [Element(dimension, min_border, max_border)
                      for _ in range(self.swarm_size)]
        self.dimension = dimension
        self.min_border = min_border
        self.max_border = max_border
        self.p_coef = p_coef
        self.g_coef = g_coef
        self.iter_amount = iter_amount
        self.stop_condition = stop_condition

    def calculate_new_velocity(self, particle):
        return 0.8 * particle.velocity + self.p_coef * random() * (
            particle.b_local_pos - particle.position
        ) + self.g_coef * random() * (self.b_swarm_pos - particle.position)

    def calculate_fitness_value(self, particle):
        fitness_value = self.fitness_func(particle.position)
        return (
            (fitness_value, particle.position)
            if fitness_value < self.b_swarm_val
            else (self.b_swarm_val, self.b_swarm_pos),
            (fitness_value, particle.position)
            if fitness_value < particle.b_local_val
            else (particle.b_local_val, particle.b_local_pos)
        )

    def run_optimization(self):
        x = []
        y = []
        for j in range(self.iter_amount):
            xi = []
            yi = []
            for i in range(self.swarm_size):
                particle = self.swarm[i]
                values = self.calculate_fitness_value(particle)

                self.b_swarm_val = values[0][0]
                self.b_swarm_pos = values[0][1]

                self.swarm[i].b_local_val = values[1][0]
                self.swarm[i].b_local_pos = values[1][1]

                if self.stop_condition(self.b_swarm_val):
                    break

                self.swarm[i].velocity = self.calculate_new_velocity(
                    particle
                )
                self.swarm[i].move()
                xi.append(self.swarm[i].position[0][0])
                yi.append(self.swarm[i].position[0][1])
            x.append(xi)
            y.append(yi)
            if self.stop_condition(self.b_swarm_val):
                break

        print(self.b_swarm_pos)
        print(self.b_swarm_val)
        return x, y

