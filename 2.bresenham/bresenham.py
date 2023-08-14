def get_line(x0, y0, x1, y1):
    points = [(x0, y0)]
    d_x = abs(x1 - x0)
    d_y = abs(y1 - y0)
    x_k = x0
    y_k = y0

    if x0 < x1:
        x_step = 1
    else:
        x_step = -1

    if y0 < y1:
        y_step = 1
    else:
        y_step = -1

    if d_y <= d_x:
        p_k = 2 * d_y - d_x
        while x_k != x1:
            x_k += x_step
            if p_k >= 0:
                y_k += y_step
                p_k -= 2 * d_x
            p_k += 2 * d_y
            points.append((x_k, y_k))
    else:
        p_k = 2 * d_x - d_y
        while y_k != y1:
            y_k += y_step
            if p_k >= 0:
                x_k += x_step
                p_k -= 2 * d_y
            p_k += 2 * d_x
            points.append((x_k, y_k))

    return points

if __name__ == "__main__":
    print(get_line(2, 2, 10, 5))
