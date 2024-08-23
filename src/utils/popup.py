import pygame


class ErasablePopup:
    FOREGROUND_COLOUR = (86, 54, 8)  # dark chocolate brown
    BACKGROUND_COLOUR = (255, 255, 255, 128)  # white
    SIDE_MARGIN = 1  # size of corners and margin
    LINE_SPACING = 1  # pixels between lines

    def __init__(self, font, message):
        # First render the text to an image, line by line
        self.image = self.text_to_bitmap(font, message)
        self.rect = self.image.get_rect()
        self.under = None  # The underneath image when drawn

    def draw_at(self, screen, position):
        """ Draw the popup at the given location, saving the underneath """
        x, y = position
        self.rect.topleft = (x, y)
        self.under = pygame.Surface((self.rect.width, self.rect.height))  # create surface to save
        self.under.blit(screen, (0, 0), (x, y, self.rect.width, self.rect.height))  # copy the background
        screen.blit(self.image, self.rect)  # draw the rendered-text
        # pygame.draw.rect(self.image, (0,0,0), [x, y, self.rect.width, self.rect.height],1)

    def is_shown(self):
        """ Is this popup drawn to the screen? """
        return (self.under != None)  # if we're on-screen there's an under

    def un_draw(self, screen):
        """ Erase the pop-up by re-drawing the previous background """
        # Only erase if we're drawn
        if (self.under != None):
            screen.blit(self.under, self.rect)  # restore the background
            self.under = None  # release the RAM

    def text_to_bitmap(self, font, message):
        """ Given a (possibly) multiline text message
            convert it into a bitmap representation with the
            given font """

        height_tally = 2 * self.SIDE_MARGIN  # height-sum of message lines
        maximum_width = 0  # maximum message width
        message_lines = []  # the text-rendered image
        message_rects = []  # where it's painted to
        # cleanup messages, remove blank lines, et.al
        for line in message.split('\n'):  # for each line
            if len(line) == 0:
                line = ' '  # make empty lines non-empty
            # Make each line into a bitmap
            message_line = font.render(line, True, self.FOREGROUND_COLOUR)
            # message_line.set_alpha(127)
            message_lines.append(message_line)
            # do the statistics to determine the bounding-box
            maximum_width = max(maximum_width, message_line.get_width())
            height_tally += self.LINE_SPACING + message_line.get_height()
            # remember where to draw it later
            position_rect = message_line.get_rect()
            if len(message_rects) == 0:
                position_rect.move_ip(self.SIDE_MARGIN, self.SIDE_MARGIN)
            else:
                y_cursor = message_rects[-1].bottom + self.LINE_SPACING + 1
                position_rect.move_ip(self.SIDE_MARGIN, y_cursor)
            message_rects.append(position_rect)
        # Render the underlying text-box
        maximum_width += 2 * self.SIDE_MARGIN  # add the margin
        image = pygame.Surface((maximum_width, height_tally), pygame.SRCALPHA)  # transparent bitmap
        # image.fill(self.BACKGROUND_COLOUR) # remove background
        # draw the lines of text
        for i in range(len(message_lines)):
            image.blit(message_lines[i], message_rects[i])
        return image
