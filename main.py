import curses
import robot

robot = robot.Robot()

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)


def main():
    try:
        while True:
            char = screen.getch()

            if char == ord('q'):
                robot.stay_at_rest()
                break
            elif char == ord('w'):
                robot.go_forward(val=1)
            elif char == ord('s'):
                robot.go_forward(val=-1)
            elif char == ord('d'):
                robot.go_right(val=1)
            elif char == ord('a'):
                robot.go_right(val=-1)
            else:
                robot.stay_at_rest()

    except Exception as e:
        pass


if __name__ == '__main__':
    main()
