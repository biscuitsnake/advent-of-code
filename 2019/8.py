import matplotlib.pyplot as plt

data = open("8.txt").read()


def make_layers(digits, width, height):
    size = width * height
    layers = [digits[x:x + size] for x in range(0, len(digits), size)]
    return layers


def decode(layers, width, height):
    image = []
    for j in range(width*height):
        pixel = False
        x = 0
        while not pixel:
            if layers[x][j] == "0":
                image.append(0)
                pixel = True
            elif layers[x][j] == "1":
                image.append(1)
                pixel = True
            else:
                x += 1
    image = [image[x:x + width] for x in range(0, len(image), width)]
    return image


# Part 1 = 1703
counts = {}
layers = make_layers(data, 25, 6)
layer = 1
for i in layers:
    counts[layer] = [i.count("0"), i.count("1"), i.count("2")]
    layer += 1
print(sorted(counts.values())[0][1] * sorted(counts.values())[0][2])

# Part 2 = HCGFE
im = decode(layers, 25, 6)
plt.imshow(im, interpolation='nearest')
plt.show()
