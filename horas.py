import datetime
import time

while True:
    # Obtém a data e hora atual
    agora = datetime.datetime.now()

    # Formata a data e hora como string
    hora_atual = agora.strftime("%H:%M:%S")

    # Limpa a tela (opcional, dependendo do seu ambiente)
    # Você pode remover essa linha se não quiser limpar a tela
    print("\033c", end="")

    # Imprime a hora atual
    print("Relógio:")
    print(hora_atual)

    # Aguarda um segundo antes de atualizar o relógio
    time.sleep(1)
