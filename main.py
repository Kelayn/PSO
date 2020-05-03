from swarm_alg import swarm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def fitness_function(position):
    return position[0][0] ** 2 + position[0][1] ** 2 + 1


def stop_condition(best_swarm_value):
    if abs(best_swarm_value - expected_value) < expected_error:
        return True


swarm_size = 30
dimension = 2
min_border = np.array([-40, -40])
max_border = np.array([40, 40]),
p_coef = 0.7
g_coef = 0.8
iter_amount = 50
expected_value = 1
expected_error = 1e-6

if __name__ == "__main__":
    new_swarm = swarm.Swarm(
        fitness_func=fitness_function,
        swarm_size=swarm_size,
        dimension=dimension,
        min_border=min_border,
        max_border=max_border,
        p_coef=p_coef,
        g_coef=g_coef,
        iter_amount=iter_amount,
        stop_condition=stop_condition
    )

    coord = new_swarm.run_optimization()

    print(coord[0][0])
    # отрисовываем
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)


    def animate(i):
        # получаем положения агентов на текущей итерации
        xs = coord[0][i]
        ys = coord[1][i]
        ax1.clear()
        plt.ylim(-200, 200)
        plt.xlim(-200, 200)
        ax1.plot(xs, ys, 'ro')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Положение агентов')


    ani = animation.FuncAnimation(fig, animate, interval=100, save_count=iter_amount)
    plt.show()
