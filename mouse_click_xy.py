from pynput import mouse

points = []

def on_click(x, y, button, pressed):
    if pressed:
        print(f"X: {x}, Y: {y}")
        points.append((x, y))

    # botão direito encerra
    if button == mouse.Button.right:
        print("\nFinalizado.\nPontos capturados:")

        for i, (px, py) in enumerate(points, start=1):
            print(f"{i}: x={px}, y={py}")

        return False  # para o listener


print("Clique ESQUERDO para capturar pontos")
print("Clique DIREITO para finalizar\n")

with mouse.Listener(on_click=on_click) as listener:
    listener.join()