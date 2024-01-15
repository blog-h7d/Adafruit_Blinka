# SPDX-FileCopyrightText: 2024 Chris Brown
#
# SPDX-License-Identifier: MIT
"""T-Head TH1520 pin names"""
from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin

GPIO0_0 = Pin((0, 0))
SPI1_SCLK = GPIO0_0
GPIO0_1 = Pin((0, 1))
SPI1_CS = GPIO0_1
GPIO0_2 = Pin((0, 2))
SPI1_MOSI = GPIO0_2
GPIO0_3 = Pin((0, 3))
SPI1_MISO = GPIO0_3
GPIO0_4 = Pin((0, 4))
GPIO0_5 = Pin((0, 5))
GPIO0_6 = Pin((0, 6))
GPIO0_7 = Pin((0, 7))
GPIO0_8 = Pin((0, 8))
GPIO0_9 = Pin((0, 9))
GPIO0_10 = Pin((0, 10))
UART1_TX = GPIO0_10
GPIO0_11 = Pin((0, 11))
UART1_RX = GPIO0_11
GPIO0_12 = Pin((0, 12))
GPIO0_13 = Pin((0, 13))
GPIO0_14 = Pin((0, 14))
GPIO0_15 = Pin((0, 15))
GPIO0_16 = Pin((0, 16))
UART3_TX = GPIO0_16
GPIO0_17 = Pin((0, 17))
UART3_RX = GPIO0_17
GPIO0_18 = Pin((0, 18))
GPIO0_19 = Pin((0, 19))
GPIO0_20 = Pin((0, 20))
GPIO0_21 = Pin((0, 21))
GPIO0_22 = Pin((0, 22))
GPIO0_23 = Pin((0, 23))
GPIO0_24 = Pin((0, 24))
GPIO0_25 = Pin((0, 25))
GPIO0_26 = Pin((0, 26))
GPIO0_27 = Pin((0, 27))
GPIO0_28 = Pin((0, 28))
GPIO0_29 = Pin((0, 29))
GPIO0_30 = Pin((0, 30))
GPIO0_31 = Pin((0, 31))
GPIO1_0 = Pin((1, 0))
GPIO1_1 = Pin((1, 1))
GPIO1_2 = Pin((1, 2))
GPIO1_3 = Pin((1, 3))
GPIO1_4 = Pin((1, 4))
GPIO1_5 = Pin((1, 5))
GPIO1_6 = Pin((1, 6))
GPIO1_7 = Pin((1, 7))
GPIO1_8 = Pin((1, 8))
GPIO1_9 = Pin((1, 9))
GPIO1_10 = Pin((1, 10))
GPIO1_11 = Pin((1, 11))
GPIO1_12 = Pin((1, 12))
GPIO1_13 = Pin((1, 13))
GPIO1_14 = Pin((1, 14))
GPIO1_15 = Pin((1, 15))
GPIO1_16 = Pin((1, 16))
GPIO1_17 = Pin((1, 17))
GPIO1_18 = Pin((1, 18))
GPIO1_19 = Pin((1, 19))
GPIO1_20 = Pin((1, 20))
GPIO1_21 = Pin((1, 21))
GPIO1_22 = Pin((1, 22))
GPIO1_23 = Pin((1, 23))
GPIO1_24 = Pin((1, 24))
GPIO1_25 = Pin((1, 25))
GPIO1_26 = Pin((1, 26))
GPIO1_27 = Pin((1, 27))
GPIO1_28 = Pin((1, 28))
GPIO1_29 = Pin((1, 29))
GPIO1_30 = Pin((1, 30))
GPIO1_31 = Pin((1, 31))
GPIO2_0 = Pin((2, 0))
UART0_TX = GPIO2_0
GPIO2_1 = Pin((2, 1))
UART0_RX = GPIO2_1
GPIO2_2 = Pin((2, 2))
GPIO2_3 = Pin((2, 3))
GPIO2_4 = Pin((2, 4))
GPIO2_5 = Pin((2, 5))
GPIO2_6 = Pin((2, 6))
GPIO2_7 = Pin((2, 7))
GPIO2_8 = Pin((2, 8))
GPIO2_9 = Pin((2, 9))
TWI2_SCL = GPIO2_9
UART2_TX = GPIO2_9
GPIO2_10 = Pin((2, 10))
TWI2_SDA = GPIO2_10
UART2_RX = GPIO2_10
GPIO2_11 = Pin((2, 11))
GPIO2_12 = Pin((2, 12))
GPIO2_13 = Pin((2, 13))
GPIO2_14 = Pin((2, 14))
GPIO2_15 = Pin((2, 15))
GPIO2_16 = Pin((2, 16))
GPIO2_17 = Pin((2, 17))
GPIO2_18 = Pin((2, 18))
GPIO2_19 = Pin((2, 19))
GPIO2_20 = Pin((2, 20))
GPIO2_21 = Pin((2, 21))
GPIO2_22 = Pin((2, 22))
GPIO2_23 = Pin((2, 23))
GPIO2_24 = Pin((2, 24))
GPIO2_25 = Pin((2, 25))
GPIO2_26 = Pin((2, 26))
GPIO2_27 = Pin((2, 27))
GPIO2_28 = Pin((2, 28))
GPIO2_29 = Pin((2, 29))
GPIO2_30 = Pin((2, 30))
GPIO2_31 = Pin((2, 31))
GPIO3_0 = Pin((3, 0))
GPIO3_1 = Pin((3, 1))
GPIO3_2 = Pin((3, 2))
GPIO3_3 = Pin((3, 3))
GPIO3_4 = Pin((3, 4))
GPIO3_5 = Pin((3, 5))
GPIO3_6 = Pin((3, 6))
GPIO3_7 = Pin((3, 7))
GPIO3_8 = Pin((3, 8))
GPIO3_9 = Pin((3, 9))
GPIO3_10 = Pin((3, 10))
GPIO3_11 = Pin((3, 11))
GPIO3_12 = Pin((3, 12))
GPIO3_13 = Pin((3, 13))
GPIO3_14 = Pin((3, 14))
GPIO3_15 = Pin((3, 15))
GPIO3_16 = Pin((3, 16))
GPIO3_17 = Pin((3, 17))
GPIO3_18 = Pin((3, 18))
GPIO3_19 = Pin((3, 19))
GPIO3_20 = Pin((3, 20))
GPIO3_21 = Pin((3, 21))
GPIO3_22 = Pin((3, 22))

uartPorts = (
    (0, UART0_TX, UART0_RX),
    (1, UART1_TX, UART1_RX),
    (2, UART2_TX, UART2_RX),
    (3, UART3_TX, UART3_RX),
)

i2cPorts = (
    (2, TWI2_SCL, TWI2_SDA),
)

spiPorts = ((0, SPI0_SCLK, SPI0_MOSI, SPI0_MISO),)

