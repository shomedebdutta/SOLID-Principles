class Bird:
    def fly(self):
        print("Flying")


class Sparrow(Bird):
    pass


def make_bird_fly(bird: Bird):
    bird.fly()


if __name__ == "__main__":
    sparrow = Sparrow()
    make_bird_fly(sparrow)
