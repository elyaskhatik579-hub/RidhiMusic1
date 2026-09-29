import config
from VISHALMUSIC import app
from VISHALMUSIC.utils.colored_buttons import styled_button


def start_panel(_):
    # GROUP / WELCOME START BUTTONS
    return [
        [
            styled_button(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style="success",
            ),
            styled_button(
                text=_["S_B_2"],
                url=config.SUPPORT_CHANNEL,
                style="primary",
            ),
        ],
    ]


async def private_panel(_):
    # PRIVATE /START BUTTONS
    # 2 buttons per row — same clean design
    owner_id = config.OWNER_ID

    return [
        [
            styled_button(
                text=_["S_B_7"],
                url=f"tg://user?id={owner_id}",
                style="primary",
            ),
            styled_button(
                text=_["S_B_4"],
                url=config.SUPPORT_CHAT,
                style="success",
            ),
        ],
        [
            styled_button(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style="success",
            ),
            styled_button(
                text=_["S_B_3"],
                callback_data="open_help",
                style="primary",
            ),
        ],
    ]
