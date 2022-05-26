from random_num_genrator import random_uniform

def predict_pi():
    """
    Here we genrate random number using function we created and predict the value of pi.
    The idea is to simulate random (x, y) points in a 2-D plane with domain as a square of side 1 unit. Imagine a circle inside the same domain with same diameter and inscribed into the square. We then calculate the ratio of number points that lied inside the circle and total number of generated points
    :return: Give a randomly predicted value of pi
    """
    INTERVAL = 1000

    circle_points = 0
    square_points = 0

    # Total Random numbers generated= possible x
    # values* possible y values
    for i in range(INTERVAL ** 2):

        # Randomly generated x and y values from a
        # uniform distribution
        # Range of x and y values is -1 to 1
        rand_x = random_uniform(-1, 1)
        rand_y = random_uniform(-1, 1)

        # Distance between (x, y) from the origin
        origin_dist = rand_x ** 2 + rand_y ** 2

        # Checking if (x, y) lies inside the circle
        if origin_dist <= 1:
            circle_points += 1

        square_points += 1

        # Estimating value of pi,
        # pi= 4*(no. of points generated inside the
        # circle)/ (no. of points generated inside the square)
        pi = 4 * circle_points / square_points
        return pi
