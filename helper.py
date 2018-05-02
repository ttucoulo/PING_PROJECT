


def write_fifo(path, message):
        fifo = open(path, "w")

        fifo.write(message)
        fifo.close()

def read_fifo(path):
        fifo = open(path, "r")
        message=fifo.readline()
        fifo.close()
        return message

