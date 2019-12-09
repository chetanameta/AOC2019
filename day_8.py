def create_image_chunk(inputstr, layer_size):
    for i in range(0, len(inputstr), layer_size):
        yield inputstr[i:i + layer_size]


width = 25
height = 6
layer_size = width * height

with open(r"day_8_input.txt", "r") as fd:
    lst = []
    chars = fd.read().rstrip()
    print(len(chars))
    image_layers = list(create_image_chunk(chars, layer_size))

    #sort image layer by min zeros
    sorted_by_min_zero = sorted(image_layers, key=lambda x: x.count("0"))
    no_of_one = sorted_by_min_zero[0].count("1")
    no_of_two = sorted_by_min_zero[0].count("2")
    output = no_of_one*no_of_two

    print("part 1 output: ", str(output))

    mapping = {"0": " ", "1": "*", "2": "2"}
    image = ["2" for _ in range(layer_size)]
    pixel = 0
    for layer in image_layers:
        for pixel in range(0, layer_size):
            image[pixel] = mapping[layer[pixel]] if image[pixel] == "2" else image[pixel]

    starTwo = "\n".join(create_image_chunk("".join(image), width))  # <5>
    print("Part 2 output: ")
    print(starTwo)
