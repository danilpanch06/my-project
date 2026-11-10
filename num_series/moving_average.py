from typing import List, Sequence


def check_window(window: int, n: int) -> None:
    """Функция валидации параметров окна."""
    if not isinstance(window, int) or window < 1:
        raise ValueError("Window должно быть целым числом >= 1.")
    if window > n:
        raise ValueError("window <= n (иначе окно больше ряда).")


def simple_moving_average(data: Sequence[float], window: int) -> List[float]:
    """SMA через бегущую сумму (O(n)) строго по методичке."""
    n = len(data)
    check_window(window, n)

    # 1. Вычисляем сумму для самого первого окна
    running = sum(data[:window])
    result = [running / window]

    # 2. Двигаем окно по всему ряду за O(1) на каждом шаге
    for i in range(window, n):
        running += data[i] - data[i - window]
        result.append(running / window)

    return result


def centered_moving_average(data: Sequence[float], window: int) -> List[float]:
    """Центрированное скользящее среднее (CMA)."""
    n = len(data)
    check_window(window, n)

    if window % 2 == 0:
        raise ValueError("Для центрированного скользящего среднего окно должно быть нечётным.")

    result = []
    half = window // 2

    for i in range(half, n - half):
        window_data = data[i - half : i + half + 1]
        result.append(sum(window_data) / window)

    return result


def exponential_moving_average(data: Sequence[float], alpha: float) -> List[float]:
    """Экспоненциальное скользящее среднее (EMA)."""
    if not (0.0 < alpha <= 1.0):
        raise ValueError(f"Коэффициент сглаживания alpha должен быть в диапазоне (0, 1], получено: {alpha}")

    if not data:
        return []

    result = [data[0]]
    for i in range(1, len(data)):
        ema_val = alpha * data[i] + (1.0 - alpha) * result[-1]
        result.append(ema_val)

    return result
