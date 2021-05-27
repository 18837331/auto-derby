# -*- coding=UTF-8 -*-
# pyright: strict

from .. import action, templates

def buy_everything():
    action.click_image(templates.GO_TO_LIMITED_SALE)
    action.wait_image(templates.CLOSE_NOW_BUTTON)
    for _, pos in action.match_image_until_disappear(templates.EXCHANGE_BUTTON):
        action.click(pos)
        action.wait_click_image(templates.EXCHANGE_CONFIRM_BUTTON)
        action.wait_click_image(templates.CLOSE_BUTTON)
        action.wait_image(templates.CLOSE_NOW_BUTTON)
        with action.recover_cursor():
            action.move(pos)
            action.wheel(-2)

    # action.click_image(templates.CLOSE_NOW_BUTTON)
    for _, pos in action.match_image_until_disappear(templates.RETURN_BUTTON):
        action.click(pos)
