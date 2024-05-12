
# O(2*N) => O(n)
'''ruby
def average_celsius(farenheit_readings)
    celsius_numbers = []
    farenheit_readings.each do |reading|
        celsius_numbers.push(reading - 32) / 1.8
    end

    sum 0.0
    celsius_numbers.each do |number|
        sum += number
    end

    return sum / celsius_numbers.length
end
'''


# O(n)
def average_celsius(farenheit_readings: list[float]) -> float:
    # celsius_numbers: list[float] = []
    average: float = 0.0
    for reading in farenheit_readings:
        average += (reading - 32) / 1.8
    return average / len(farenheit_readings)


def main() -> None:
    res: float = average_celsius([45.6, 65.45, 38.04])
    print(res)


if __name__ == '__main__':
    main()

