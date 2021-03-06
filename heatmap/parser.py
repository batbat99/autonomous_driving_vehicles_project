def parser(path):
    """takes path for a txt file as string,
    and returns the parsed data"""

    lines = []
    with open(path) as f:
        lines = f.readlines()

    data = []

    for line in lines:
        frame_data = line.split()
        for i in range(len(frame_data)):
            frame_data[i] = int(frame_data[i])
        data.append(frame_data)

    return data
