# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import terminalio
import displayio
from adafruit_display_text import label
from adafruit_st7735r import ST7735R

#class for LCD:
class myLCD:
    """
    Initialize LCD instance
    chipSelect - pin for chipSelect (e.g. board.D5)
    spiData - pin for spiData (e.g. board.D6)
    """
    def __init__(self, chipSelect, spiData) -> None:
        # Release any resources currently in use for the displays
        displayio.release_displays()

        spi = board.SPI()
        tft_cs = chipSelect
        tft_dc = spiData

        display_bus = displayio.FourWire(
            spi, command=tft_dc, chip_select=tft_cs, reset=board.D9
        )

        self.display = ST7735R(display_bus, width=128, height=128, colstart=2, rowstart=1)

        # Make the display context
        self.splash = displayio.Group()
        self.display.show(self.splash)
    
    """
    refreshes the screen with a blank slate
    """
    def refresh(self):
        self.splash = displayio.Group()
        self.display.show(self.splash)
    """
    displays text on the lcd
    intext - text to display
    incolor - color in hex
    inx - x coordinate of the display
    iny - y coordinate of the display
    """
    def displayText(self, intext, incolor, inx, iny):
        text_area = label.Label(terminalio, text = intext, color = incolor, x=inx, y=iny)
        self.splash.append(text_area)

    """
    displays a bitmap image. 
    location - directory of bmp file
    """
    def displayBMP(self, location):
        with open(location, "rb") as bitmap_file:

            # Setup the file as the bitmap data source
            bitmap = displayio.OnDiskBitmap(bitmap_file)

            # Create a TileGrid to hold the bitmap
            tile_grid = displayio.TileGrid(
                bitmap,
                pixel_shader=getattr(bitmap, 'pixel_shader', displayio.ColorConverter())
            )

            # Add the TileGrid to the Group
            self.splash.append(tile_grid)
