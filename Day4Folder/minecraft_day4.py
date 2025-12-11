# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
def on_on_chat(height, width):
    for index in range(width):
        for index2 in range(height):
            agent.place(FORWARD)
            agent.move(UP, 1)
        agent.move(DOWN, height)
        agent.move(RIGHT, 1)
player.on_chat("build", on_on_chat)

def on_on_chat2():
    agent.turn(RIGHT)
player.on_chat("tr", on_on_chat2)

def on_on_chat3(steps):
    agent.move(BACK, steps)
player.on_chat("bk", on_on_chat3)

def on_on_chat4(steps32):
    for index3 in range(steps32):
        agent.destroy(DOWN)
        agent.move(DOWN, 1)
player.on_chat("dd", on_on_chat4)

def on_on_chat5(steps2):
    agent.move(FORWARD, steps2)
player.on_chat("fw", on_on_chat5)

def on_on_chat6(steps322):
    agent.move(UP, steps322)
player.on_chat("up", on_on_chat6)

def on_on_chat7():
    agent.turn(LEFT)
player.on_chat("tl", on_on_chat7)

def on_on_chat8():
    for index4 in range(5):
        agent.move(FORWARD, 1)
player.on_chat("say", on_on_chat8)

def on_on_chat9():
    agent.teleport_to_player()
player.on_chat("come", on_on_chat9)

def on_on_chat10(steps4):
    agent.move(DOWN, steps4)
player.on_chat("dn", on_on_chat10)

def on_on_chat11(Legnth):
    for index5 in range(Legnth):
        agent.destroy(FORWARD)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.collect_all()
        agent.move(FORWARD, 1)
player.on_chat("mine", on_on_chat11)

def on_on_chat12(steps5):
    agent.move(LEFT, steps5)
player.on_chat("lt", on_on_chat12)

def on_on_chat13(steps3):
    for index6 in range(steps3):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    agent.move(DOWN, 6)
    agent.collect_all()
player.on_chat("chop", on_on_chat13)

def on_on_chat14(steps6):
    agent.move(RIGHT, steps6)
player.on_chat("rt", on_on_chat14)

def roof(width, legnth):
    for width in range(width):
        for legnth in range(legnth):
            agent.place(DOWN)
            agent.move(UP, 1)
        agent.move(RIGHT, 1)
        agent.move(DOWN, width)

def digdown():
    while agent.detect(AgentDetection.BLOCK, DOWN):
        agent.destroy(DOWN)
        agent.move(DOWN, 1)
player.on_chat("dig", digdown)
def collect():
    agent.collect_all()
player.on_chat("collect", collect)