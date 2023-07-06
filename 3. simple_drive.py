from ev3 import Ev3
import time

bot = Ev3("COM4")
bot.set_speed(Ev3.Motors.B, 100)
print("EncoderB=", bot.encoder(Ev3.Encoders.B))
bot.start(Ev3.Motors.B)
time.sleep(1)
bot.stop(Ev3.Motors.B, Ev3.Stop.FLOAT)
print("ButtonS3=", bot.button(Ev3.Ports.P3))
print("EncoderB=", bot.encoder(Ev3.Encoders.B))
bot.close()
